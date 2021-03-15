from django.shortcuts import render, redirect
from forms import accounts
from django.contrib import messages


def register(request):
    if request.method == "POST":
        form = accounts.UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            #capitalize() or .title() will work
            messages.success(request, f'Welcome, {first_name.capitalize()} {last_name.capitalize()}!')
            return redirect('register')
    if request.method == "GET":
        form = accounts.UserCreationForm()

    context = {
		'form': form,
	}
    return render(request, 'accounts/register.html',context)
