''' Custom Authentication Middleware '''
from django.contrib import messages
from django.shortcuts import redirect

from userApp.constant import PROFILE_ROUTES, REGISTRATION_ROUTES


class AuthMiddleware(object):
    ''' Middleware to check whether the user is uthenticated or not'''
    def __init__(self, get_response):
        """
        Initialization method of AuthMiddleware
        """
        self.get_response = get_response

    def __call__(self, request):
        """
        If user is not logged in then it will passed on the the request to passing registration
        related page (i.e, login, signup) else it will redirect to profile page or if user is
        logged in and try to access registration url then it will redirect to profile page
        """
        if request.user.is_authenticated:
            if request.get_full_path() in REGISTRATION_ROUTES:
                messages.warning(request, 'User already logged in !')
                return redirect('/profile')
            else:
                response = self.get_response(request)
                return response
        else:
            if request.get_full_path() in PROFILE_ROUTES:
                messages.warning(request, 'User not logged in !')
                return redirect('/login')
            else:
                response = self.get_response(request)
                return response
