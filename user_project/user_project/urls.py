""" user_project URL Configuration """

from email import message
from django.conf import settings
from django.conf.urls import handler404
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('userApp.urls')),
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True,
            template_name='registration/login.html'), name='login'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'userApp.views.error_404'
