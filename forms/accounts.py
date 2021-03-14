from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from accounts.models import User

class EmailRequiredMixin(object):
    def __init__(self, *args, **kwargs):
        super(EmailRequiredMixin, self).__init__(*args, **kwargs)
        # make user email field required
        self.fields['email'].required = True
        self.fields['username'].help_text = "Read only."		


class UsernameDisableMixin(object):
	def __init__(self, *args, **kwargs):
		super(UsernameDisableMixin, self).__init__(*args, **kwargs)
		self.fields['username'].disabled = True


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


class UserChangeForm(EmailRequiredMixin, UsernameDisableMixin, UserChangeForm):
	def __init__(self, *args, **kwargs):
		super(UserChangeForm, self).__init__(*args, **kwargs)
		# make some attributes field required
		self.fields['first_name'].required = True
		self.fields['last_name'].required = True\

	class Meta:
		model = User
		fields = []
