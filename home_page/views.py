from django.shortcuts import render
from travel_app.models import Travel

current_page = ''

def is_auth(request):
    if request.user.is_authenticated:
        return True
    else:
        return False

# Create your views here.
def index(request):
    current_page = 'Home'
    travels = Travel.objects.all()
    return render(request, 'index.html', {'is_auth': is_auth(request), 'current_page': current_page, 'travels': travels,})

def about(request):
    current_page = 'About'
    return render(request, 'about.html', {'is_auth': is_auth(request), 'current_page': current_page,})
