from django.contrib import admin
from .models import User
from forms import accounts
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

class UserAdmin(UserAdmin):
	add_form = accounts.UserCreationForm
	add_fieldsets = (
		    	('Login Credentials', {
	            'description': '',
	            'classes': ('wide',),
	            'fields': ('username', 'password1', 'password2', ),
	        }),
		        ('Personal Info', {
	            'description': '',
	            'classes': ('wide',),
	            'fields': ('first_name', 'last_name', 'email',),
	        }),

		)
	fieldsets = (

		    ('Login Credentials', {
	            'description': '',
	            'classes': ('wide',),
	            'fields': ('username','password'),
	        }),
			('Personal Info', {
	            'description': '',
	            'classes': ('wide',),
	            'fields': ('first_name', 'last_name', 'email',),
	        }),

		)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)