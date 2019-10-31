from django.shortcuts import render

current_page = ''

def is_auth(request):
    if request.user.is_authenticated:
        return True
    else:
        return False

# Create your views here.
def index(request):
    current_page = 'Home'
    return render(request, 'index.html', {'is_auth': is_auth(request), 'current_page': current_page,})

def about(request):
    current_page = 'About'
    return render(request, 'about.html', {'is_auth': is_auth(request), 'current_page': current_page,})
