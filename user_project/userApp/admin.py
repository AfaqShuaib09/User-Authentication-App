''' Admin Panel View for User App '''
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.utils.html import format_html

from userApp.models import Profile


# Register your models here.
class CustomProfileAdmin(admin.ModelAdmin):
    ''' Custom Profile Model to be used in the Admin Panel '''
    list_display = ('user', 'full_name', 'gender', 'country', 'address', 'cnic', 'get_profile_image',
                        'contact_number', 'edit_details')
    list_select_related = ('user', )
    fields = ['user', 'full_name', 'cnic', 'contact_number', 'gender' ,'country',
                'address', 'image', 'get_profile_image']
    search_fields = ['user__username', 'full_name']
    radio_fields = {'gender': admin.HORIZONTAL}
    readonly_fields=('user', 'get_profile_image')

    def edit_details(self, obj):
        ''' Link to edit the profile of the user '''
        return format_html(f'<a href="/admin/userApp/profile/{obj.id}/change/">Edit</a>')

    def get_profile_image(self, obj):
        ''' Returns the profile image of the user as a field '''
        return format_html(f'<image src="/media/{obj.image}" style="width:150px;height:100px;">')


class ProfileInline(admin.StackedInline):
    ''' Inline Profile Model associated with the User '''
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    ''' Custom User Model to be used in the Admin Panel '''
    inlines = (ProfileInline, )
    list_display = ('username', 'email', 'get_gender' ,'is_staff', 'is_superuser', 'is_active',
                        'date_joined', 'last_login', 'edit_details')
    list_select_related = ('profile', )
    fieldsets = [
        ('Personal Information', {'fields': ['username' ,'email', 'is_staff', 'is_superuser',
            'is_active', 'date_joined', 'last_login']}),
    ]
    readonly_fields=('username', )

    search_fields = ['username', 'email']
    ordering = ['date_joined']
    list_filter = ['is_staff', 'is_superuser', 'is_active', 'date_joined', 'last_login']

    def get_gender(self, instance):
        ''' Returns the gender of the user '''
        return instance.profile.gender
    get_gender.short_description = 'Gender'

    def edit_details(self, obj):
        ''' Link to edit the details of the user '''
        return format_html(f'<a href="/admin/auth/user/{obj.id}/change/">Edit</a>')

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile, CustomProfileAdmin)
