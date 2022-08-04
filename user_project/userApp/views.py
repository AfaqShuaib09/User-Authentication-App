''' Views (User Interface) Definitions to be used in the User App '''

from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.shortcuts import redirect, render
from django.views.generic import View

from userApp.form import ProfileUpdateForm, SignupForm


# Create your views here.
class SignupView(View):
    '''
    Display Signup form view to the user
    '''
    def get(self, request):
        ''' Returns the signup page to add the details for new user to register himself '''
        if request.user.is_authenticated:
            return redirect('/profile')
        else:
            form = SignupForm()
            context = {
                'user_creation_form': form
            }
            return render(request, 'registration/signup.html', context = context)

    def post(self, request):
        ''' Creates a new user and redirects to the login page '''
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User Registered Successfully. ✅')
            return redirect('/login')
        else:
            return render(request, 'registration/signup.html', {'user_creation_form': form})


class LogoutView(View):
    '''
    Logout the user from the application and returns the user to login page
    '''
    def get(self, request):
        ''' Logs out the user and redirects to the login page '''
        logout(request)
        messages.success(request, "User Logout Successfully ✅")
        return redirect('/login')


class ProfileView(View):
    '''
    Display user profile details to the user
    '''
    def get(self, request):
        ''' Returns the profile page to display the user details '''
        if request.user.is_authenticated:
            user = request.user
            context = {
                'profile': user.profile
            }
            return render(request, 'userApp/profile.html', context=context)
        else:
            return redirect('/login')


class EditView(View):
    '''
    Handles the get and post request of profile edit view
    '''
    def get(self, request):
        ''' Returns the edit profile page to edit the user details '''
        if request.user.is_authenticated:
            user = request.user
            form = ProfileUpdateForm(instance=user.profile)
            context = {
                'edit_form': form
            }
            return render(request, 'userApp/edit_profile.html', context=context)
        else:
            messages.warning(request, 'User not logged in !')
            return redirect('/login')

    def post(self, request):
        ''' Updates the user details and redirects to the profile page '''
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'User profile updated successfully. ✅')
            return redirect('/profile/')
        else:
            return render(request, 'userApp/edit_profile.html', {'profile_form': form})


def error_404(request, exception):
    ''' Returns the error page for 404 error if the page is not found '''
    response = render(request,"userApp/404.html")
    return response
