from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Optionally log the user in after registration:
            login(request, user)
            return redirect('home')  # or wherever you want to redirect
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
