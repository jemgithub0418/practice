from django.contrib import admin
from .models import User
from forms import accounts
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

class UserAdmin(UserAdmin):
	model = User
	add_form = accounts.UserCreationForm

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)