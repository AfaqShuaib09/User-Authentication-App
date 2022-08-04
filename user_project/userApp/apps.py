''' configuration for user app '''
from django.apps import AppConfig


class UserAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'userApp'

    def ready(self):
        import userApp.signals
