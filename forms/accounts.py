from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User

class UserCreationForm(UserCreationForm):
	def __init__(self, *args, **kwargs):
		super(UserCreationForm, self).__init__(*args, **kwargs)

		self.fields['email'].required = True
		self.fields['first_name']. required = True
		self.fields['last_name'].required = True

	class Meta:
		model = User
		fields = [
			'email', 'first_name', 'last_name', 'username','password', 'password2',
		]