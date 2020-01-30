from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignUpForm


def index(request):
    return render(request, "users/index.html", {})

def signup(request):
    if request.method == "POST":
        form  = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username} your account is created successfully!')
            return redirect('users:login')
    else:
        forms = SignUpForm
        return render(request, "users/signup.html", {'forms' : forms})

@login_required
def home(request):
    return render(request, "users/home.html", {})