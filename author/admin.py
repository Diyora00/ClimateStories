from django.contrib import admin

from author.models import Author, Article

# Register your models here.
admin.site.register(Author)
admin.site.register(Article)
