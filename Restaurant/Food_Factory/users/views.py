from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from django.contrib import messages 

def register(request):

    if request.method == 'POST':
        print('In if ')
        form = RegisterForm(request.POST)       # (request.POST) It will have all the request data filled up users
        if form.is_valid():
            form.save()
            print("in form valid")
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}, Your account is created')
            return redirect('login')

    else: 
        form = RegisterForm()       #This will have empty form
    return render(request, 'users/register.html', {'form': form})

@login_required
def profilepage(request):
    return render(request, 'users/profile.html')