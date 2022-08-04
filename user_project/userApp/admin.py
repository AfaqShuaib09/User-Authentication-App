''' Admin views for User App '''
from django.contrib import admin

from userApp.models import Profile

# Register your models here.
admin.site.register(Profile)
