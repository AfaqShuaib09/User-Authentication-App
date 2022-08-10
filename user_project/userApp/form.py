''' Forms Definition to be used in the User App '''
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from userApp.constant import GENDER_CHOICES
from userApp.models import Profile


class SignupForm(UserCreationForm):
    ''' User Creation Form overrides to add extra fields i.e; Email'''

    email = forms.EmailField(label='Email', required=True, widget=forms.EmailInput())
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password2'].label = 'Confirm Password'
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
            

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control my-2'

    class Meta:
        ''' Meta class declares here overrides to add extra fields '''
        model = User
        fields = ('username', 'email')
        error_messages = {
            'password2': {
                'password_mismatch': 'Passwords do not match.'
            }
        }

    def save(self, commit=True):
        ''' custom save method '''
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class ProfileUpdateForm(forms.ModelForm):
    ''' User Profile Update Form '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control my-2 w-100'
        self.fields['cnic'].widget.attrs['pattern'] = '^[0-9]{5}-[0-9]{7}-[0-9]$'
        self.fields['contact_number'].widget.attrs['pattern'] = '^\+\d{12}$'
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect(), required=False)

    class Meta:
        ''' Meta class add to select the model to be used and determine order of form to be displayed '''
        model = Profile
        fields = ['full_name', 'cnic', 'contact_number', 'address', 'country', 'image', 'gender']


class EmailUpdateForm(forms.ModelForm):
    ''' User Email Update Form '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['class'] = 'form-control my-2 w-100'

    class Meta:
        model = User
        fields = ['email']
        error_messages = {
            'email': {
                'unique': 'This email is already in use.'
            }
        }
