from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User

class UserCreationForm(UserCreationForm):
	# first_name = forms.CharField(required=True)
	def __init__(self, *args, **kwargs):
		super(UserCreationForm, self).__init__(*args, **kwargs)

		self.fields['first_name'].required = True
		self.fields['last_name'].required = True
		self.fields['email'].required = True

	class Meta:
		model = User
		fields = [
				'username','password', 'password2', 'first_name', 'last_name', 
				'email', 'address'
			]