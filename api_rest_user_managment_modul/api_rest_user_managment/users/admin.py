from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, UsersContact

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'is_staff', 'date_joined')

@admin.register(UsersContact)
class UserContactsAdmin(admin.ModelAdmin):
    list_display = ('user', 'country_code', 'phone_number', 'updated_at')
