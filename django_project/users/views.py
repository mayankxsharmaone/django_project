from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserReisterForm 


def register(request):
    if request.method == 'POST':
        form = UserReisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
    else:
        form = UserReisterForm()
    return render(request, 'users/register.html', {'form': form})

