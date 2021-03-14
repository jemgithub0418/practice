from django.shortcuts import render
from forms import accounts

def register(request):
	form = accounts.UserCreationForm()

	context = {
		'form': form,
	}
	return render(request, 'accounts/register.html',context)