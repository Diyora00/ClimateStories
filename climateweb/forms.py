from django import forms
from climateweb.models import EchoChoice


class EchoChoiceForm(forms.ModelForm):
    class Meta:
        model = EchoChoice
        fields = '__all__'
