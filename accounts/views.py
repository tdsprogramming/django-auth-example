from django.shortcuts import render, redirect
from django.contrib import messages

# Django imports
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def index_view(request):
    return render(request, "accounts/index.html")


def register_view(request):
    # validations
    errors = {}
    if len(request.POST['username']) < 2:
        errors['username'] = "Invalid username"

    if len(request.POST['email']) < 2:
        errors['email'] = "Invalid email"

    if request.POST['password'] != request.POST['confirmPassword']:
        errors['password'] = "Passwords don't match"

    if len(errors) > 0:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect('/accounts')
    else:
        try:
            new_user = User.objects.create_user(
                username=request.POST['username'], email=request.POST['email'], password=request.POST['password'])
        except:
            messages.error(request, "Choose a different username")
            return redirect('/accounts')
        login(request, new_user)
        return redirect('/accounts/success')


def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/accounts/success')
    messages.error(request, "Invalid Login")
    return redirect('/accounts')


def logout_view(request):
    logout(request)
    return redirect('/accounts')


@login_required
def success_view(request):
    return render(request, "accounts/success.html")
