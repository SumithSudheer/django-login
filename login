from multiprocessing import context
from django.http import HttpResponse
from . import models
from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect(home)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if len(username) < 4:
            messages.error(request, ("username should contain atleast 4 char"))
            return render(request, 'login.html')
        # for i in username:
        #     if i == " ":
        #         messages.error(request, ("username should not contain spaces"))
        #         return render(request, 'login.html')
        # if len(password) < 8:
        #     messages.error(request, ("password should contain atleast 8 char"))
        #     return render(request, 'login.html')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if request.user.is_authenticated:
                # if request.user.is_staff():
                #     print("HI")
                #     return HttpResponse("<h1>admin</h1>")
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

    return render(request, 'login.html')
