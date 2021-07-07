from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import EmailField

# Create your models here.

class perfil(models.Model):

    user=models.OneToOneField(User,on_delete=models.CASCADE)

    phone_number=models.CharField(max_length=20,blank=True)
    picture=models.ImageField(
        upload_to='usuarios/pictures',
        blank=True,
        null=True
    )

    # email=EmailField(max_length=30,blank=True)

    created=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username