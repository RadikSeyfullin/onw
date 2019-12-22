from django.shortcuts import render, redirect

current_page = 'Profile'

# Create your views here.
def profile_view(request):
    if (request.user.is_authenticated):
        return render(request, 'profile.html', context={'current_page': current_page})
    else:
        return redirect('LoginPage')