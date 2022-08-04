'''
Custom management command to create a user.
'''

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    '''
    User Creation Command
    '''
    help = 'Create User command : create_user <username> <password> <email>'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='Username of the user')
        parser.add_argument('password', type=str, help='Password of the user')
        parser.add_argument('email', type=str, help='Email of the user')

    def handle(self, *args, **kwargs):
        username = kwargs['username']
        password = kwargs['password']
        email = kwargs['email']
        user = User.objects.create_user(username = username, email = email,
                                        password=password)
        user.save()
