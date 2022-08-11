'''
Custom management command to create a user.
'''
import re
from getpass import getpass

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
            while not re.match(r'^[a-zA-Z0-9-@.+-_]+$', username):
                self.stdout.write(self.style.ERROR
                                    ('Username may contain only letters, numbers, and @/./+/-/_ characters.'))
                username = input("Username: ")
            email = input("Email: ")
            while not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
                self.stdout.write(self.style.ERROR('Please enter a valid email'))
                email = input("Email: ")
            while(True):
                password = getpass("Password: ")
                confirm_password = getpass("Confirm Password: ")
                if password == confirm_password:
                    break
                else:
                    self.stdout.write(self.style.ERROR('Passwords do not match'))
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
            self.stdout.write(self.style.SUCCESS('User created successfully'))
        except IntegrityError as e:
            self.stdout.write(self.style.ERROR('User Already Exists'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(e))
