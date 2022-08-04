''' Models Definitions to be used in the User App '''

from django.contrib.auth.models import User
from django.db import models
from django_countries.fields import CountryField
from PIL import Image

from userApp.constant import (CNIC_VALIDATOR, CONTACT_NO_VALIDATOR,
                              GENDER_CHOICES)


# Create your models here.
class Profile(models.Model):
    ''' User Profile Model '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='upload/', default='upload/default.png',
                                help_text='your profile picture')
    full_name = models.CharField(max_length=100, help_text='your full name', blank=True)
    cnic = models.CharField(max_length=15 , help_text='your CNIC in the following format: xxxxx-xxxxxxx-x',
                            validators=[ CNIC_VALIDATOR ], blank=True)
    contact_number = models.CharField(max_length=13,
                                        help_text='your contact number in the following format: +xxxxxxxxxxx',
                                        validators=[ CONTACT_NO_VALIDATOR ], blank=True)
    address = models.CharField(max_length=200, help_text='your home address', blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='', blank=True)
    country = CountryField(blank_label='(select country)', help_text='your country', blank=True)

    def __str__(self):
        ''' Overrides the str method to return the name of the user '''
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        ''' Overrides the save method to resize the image to fit the requirements '''
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
