from author.models import User, Author, Article
from django import forms


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def clean_password(self):
        password = self.cleaned_data.get('password')
        password2 = self.data.get('password2')
        if password2 != password:
            raise forms.ValidationError(f'Passwords did not match {password}, {password2}')
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

    def clean_username(self):
        username = self.data.get('username')
        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError('Email does not exist')
        return username

    def clean_password(self):
        username = self.cleaned_data.get('username')
        password = self.data.get('password')
        try:
            user = User.objects.get(username=username)
            if not user.check_password(password):
                raise forms.ValidationError('Password did not match')
        except User.DoesNotExist:
            raise forms.ValidationError(f'{username} does not exists')
        return password


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('full_name', 'about', 'image')


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'content', 'image')
