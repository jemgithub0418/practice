from django.contrib import admin
from .models import User
from forms import accounts
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group


class UserAdmin(UserAdmin):
	# form = accounts.UserChangeForm
	add_form = accounts.UserCreationForm
	form = accounts.UserChangeForm
	# REQUIRED_FIELDS = ['first_name', 'last_name']
	fieldsets = (
	        ('Login Credentials', {'fields': ('email','username', 'password',)}),
	        ('Personal Information', { 'fields': ('first_name', 'last_name', )}),
		)
	add_fieldsets = (
	        ('Login Credentials', {'fields': ('email','username', 'password',)}),
	        ('Personal Information', { 'fields': ('first_name', 'last_name', 'address')}),
		)

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)