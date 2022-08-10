'''
Custom management command to create a user.
'''

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    '''
    User Creation Command
    '''
    help = 'Create User command : create_user <username> <email> <password>'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='Username of the user')
        parser.add_argument('email', type=str, help='Email of the user')
        parser.add_argument('password', type=str, help='Password of the user')

    def handle(self, *args, **kwargs):
        try:
            username = kwargs['username']
            email = kwargs['email']
            password = kwargs['password']
            user = User.objects.create_user(username, email, password)
            user.save()
            self.stdout.write(self.style.SUCCESS('User created successfully'))
        except IntegrityError as e:
            self.stdout.write(self.style.ERROR('User Already Exists'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(e))
