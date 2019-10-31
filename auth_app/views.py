from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

current_page = ''

def is_auth(request):
    if request.user.is_authenticated:
        return True
    else:
        return False

# Create your views here.
def viewLoginPage(request):
    current_page = 'Auth'
    if is_auth(request):
        return redirect('HomePage')
    else:
        return render(request, 'login.html', {'is_auth': is_auth(request), 'current_page': current_page})

def logout(request):
    auth_logout(request)
    return redirect('HomePage')

def register(request):
    username = request.POST['name'].split(' ')
    email = request.POST['email']
    password = request.POST['password']
    r_password = request.POST['r_password']
    if len(username) <= 1:
        return redirect('LoginPage')
    elif password == r_password:
        all = CustomUser.objects.all()
        for i in all:
            if email == i.email:
                return redirect('LoginPage')
        CustomUser.objects.create_user(email, password, first_name=username[0].capitalize(), last_name=username[1].capitalize())
        user = authenticate(request, password=password, email=email)
        if user is not None:
            auth_login(request, user)
            return redirect('HomePage')
        else:
            return redirect('LoginPage')
    else:
        return redirect('LoginPage')

def login(request):
    email = request.POST['email']
    password = request.POST['password']
    user = authenticate(request, password=password, email=email)
    if user is not None:
        auth_login(request, user)
        return redirect('HomePage')
    else:
        return redirect('LoginPage')
