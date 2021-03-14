from django.shortcuts import render
from forms import accounts


def register(request):
	userform = accounts.UserCreationForm()
	if request.method == 'POST':
		pass
	else:
		pass

	context = {
		'form': userform,
	}

	return render(request, 'accounts/register.html', context)