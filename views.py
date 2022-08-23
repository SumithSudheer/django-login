from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout


def index(request):
    # dict {'admin':'admin'}
    if request.user.is_authenticated:
        return redirect(home)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if len(username)<4:
            messages.error(request, ("username should contain atleast 4 char"))
            return render(request, 'login.html')
        for i in username:
            if i== " ":
                messages.error(request, ("username should not contain spaces"))
                return render(request, 'login.html')
        if len(password)<1:
            messages.error(request, ("password should contain atleast 8 char"))
            return render(request, 'login.html')




        user = authenticate(request, username=username, password=password)
        if user is not None:
            if request.user.is_authenticated:
                return redirect(home)
            login(request, user)
            return home(request)
            # Redirect to a success page.
            ...
        else:
            messages.error(request, ("username or password not correct"))
            return render(request, 'login.html')

            # Return an 'invalid login' error message.
            ...
    else:
        if request.user.is_authenticated:
            return redirect(home)
        return render(request, 'login.html')


def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    return redirect(index)
    # if request.method == 'POST':
    #     return redirect(request, 'login.html')
    # else:
    #     return render(request, 'home.html')

# Create your views here.
def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
    messages.success(request, ("you have been logged out"))
    return index(request)
