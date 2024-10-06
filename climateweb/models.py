from django.db import models


class EchoChoice(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='echo_img/')
    about = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
