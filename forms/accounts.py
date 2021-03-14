from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User

class UserCreationForm(UserCreationForm):
	REQUIRED_FIELDS = ['first_name', 'last_name', 'email',]
	class Meta:
		model = User
		fields = '__all__'