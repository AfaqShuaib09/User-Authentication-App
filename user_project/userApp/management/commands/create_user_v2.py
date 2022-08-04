'''
Custom management command to create a user.
'''

from time import sleep
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    '''
    User Creation Command VERSION 2 (with optional args)
    '''
    help = 'Create User command : create_user_v2 <username> <email> <password>'

    def add_arguments(self, parser):
        parser.add_argument('--username', type=str, help='Username of the user', required=False)
        parser.add_argument('--email', type=str, help='Email of the user', required=False)
        parser.add_argument('--password', type=str, help='Password of the user', required=False)

    def handle(self, *args, **kwargs):
        if kwargs.get('username') and kwargs.get('email') and kwargs.get('password'):
            username = kwargs['username']
            email = kwargs['email']
            password = kwargs['password']
        else:
            self.stdout.write('Please provide all the required arguments')
            print("Enter your credentials")
            username = input("Username: ")
            email = input("Email: ")
            password = input("Password: ")
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
            self.stdout.write(self.style.SUCCESS('User created successfully'))
        except Exception as IntegrityError:
            self.stdout.write(self.style.ERROR('User Already Exists'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(e))
