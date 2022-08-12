''' Views (User Interface) Definitions to be used in the User App '''

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.views.generic import View
from django.utils.decorators import method_decorator

from userApp.form import SignupForm, ProfileUpdateForm, EmailUpdateForm
from userApp.middlewares import AuthMiddleware

# Create your views here.
class SignupView(View):
    '''
    Display Signup form view to the user
    '''
    @method_decorator(AuthMiddleware)
    def get(self, request):
        ''' Returns the signup page to add the details for new user to register himself '''
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
            messages.info(request, "Registered Successfully. ✅. You are now logged in.")
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return redirect('/profile')
        else:
            return render(request, 'registration/signup.html', {'user_creation_form': form})


class LogoutView(View):
    '''
    Logout the user from the application and returns the user to login page
    '''
    @method_decorator(AuthMiddleware)
    def get(self, request):
        ''' Logs out the user and redirects to the login page '''
        logout(request)
        messages.success(request, "User Logout Successfully ✅")
        return redirect('/login')


class ProfileView(View):
    '''
    Display user profile details to the user
    '''
    @method_decorator(AuthMiddleware)
    def get(self, request):
        ''' Returns the profile page to display the user details '''
        user = request.user
        context = {
            'profile': user.profile
        }
        return render(request, 'userApp/profile.html', context=context)


class EditView(View):
    '''
    Handles the get and post request of profile edit view
    '''
    @method_decorator(AuthMiddleware)
    def get(self, request):
        ''' Returns the edit profile page to edit the user details '''
        user = request.user
        form = ProfileUpdateForm(instance=user.profile)
        context = {
            'edit_form': form
        }
        return render(request, 'userApp/edit_profile.html', context=context)

    def post(self, request):
        ''' Updates the user details and redirects to the profile page '''
        user_profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        user_email_form = EmailUpdateForm(request.POST, instance=request.user)
        if user_profile_form.is_valid():
            user_profile_form.save()
        if user_email_form.is_valid():
            user_email_form.save()
            messages.success(request, 'User profile updated successfully. ✅')
            return redirect('/profile/')
        else:
            messages.warning(request, 'User profile update failed. ❌')
            return redirect('/profile/edit/')

def error_404(request, exception):
    ''' Returns the error page for 404 error if the page is not found '''
    response = render(request,"userApp/404.html")
    return response
