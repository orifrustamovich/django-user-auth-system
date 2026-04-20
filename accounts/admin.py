
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import RegistrationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = RegistrationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email','first_name','last_name','is_staff']



admin.site.register(CustomUser, CustomUserAdmin)



