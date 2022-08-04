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
                                help_text='Profile image for the user')
    full_name = models.CharField(max_length=100, help_text='Full name of the user')
    cnic = models.CharField(max_length=15 , help_text='CNIC of the user format: xxxxxx-xxxxxxx-x',
                            validators=[ CNIC_VALIDATOR ])
    contact_number = models.CharField(max_length=13, help_text='Phone number of the user format: +xxxxxxxxxxx',
                                validators=[ CONTACT_NO_VALIDATOR ])
    address = models.CharField(max_length=100, help_text='Address of the user')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='', blank=True)
    country = CountryField(blank_label='(select country)', help_text='Country of the user')

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
