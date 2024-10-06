from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from author.managers import CustomUserManager
from django.contrib.auth.hashers import make_password


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, null=True, blank=True)
    username = models.CharField(unique=True, null=True, blank=True, max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    class Meta:
        ordering = ('-id',)

    objects = CustomUserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if self.password and not self.password.startswith(('pbkdf2_sha256$', 'bcrypt$', 'argon2')):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)


class Author(models.Model):
    full_name = models.CharField(max_length=250)
    about = models.CharField(max_length=340, blank=True, null=True)
    image = models.ImageField(upload_to='authors/', null=True, blank=True)
    user = models.OneToOneField('author.User', models.CASCADE, related_name='author')

    def __str__(self):
        return self.full_name


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='articles/')
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='articles', null=True, blank=True)
    quiz = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
