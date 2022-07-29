''' Urls related/ associated to the userApp '''
from django.urls import path

from userApp.views import EditView, LogoutView, ProfileView, SignupView

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/edit/', EditView.as_view(), name='profile_edit'),
]
