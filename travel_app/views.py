from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from .models import *
from user_manager.models import CustomUser

current_page = 'Travels'

def is_user_on_travel(travel_id, user_id):
    if TravelMembers.objects.filter(travel_id=travel_id, user_id=user_id).exists():
        return True
    else:
        return False

def is_auth(r):
    if r.user.is_authenticated:
        return True
    else:
        return False

# Create your views here.
def viewAllTravels(request):
    all_travels = Travel.objects.all()
    return render(request, 'travels.html', {'is_auth': is_auth(request), 'travels': all_travels, 'current_page': current_page})

def viewMyTravels(request):
    travels = Travel.objects.all()
    members = TravelMembers.objects.filter(user_id=request.user.id)
    return render(request, 'mytravels.html', {'is_auth': is_auth(request), 'travels': travels, 'members': members})

def viewOneTravel(request, travel_id):
    singed_user = False
    if is_user_on_travel(travel_id, request.user.id):
        singed_user = True
    find_travel = Travel.objects.get(id=travel_id)
    creator = CustomUser.objects.get(email=str(find_travel.creator_id))
    members = TravelMembers.objects.filter(travel_id=travel_id)
    users = CustomUser.objects.all()
    return render(request, 'travel.html', {'is_auth': is_auth(request), 'travel': find_travel, 'current_page': current_page, 'travel_creator': creator, 'members': members, 'users': users,
    'signed_user': singed_user,})

def userToMembers(request, travel_id):
    if not is_user_on_travel(travel_id, request.user.id):
        travel = Travel.objects.get(id=travel_id)
        user = CustomUser.objects.get(id=request.user.id)
        new_add = TravelMembers(travel_id=travel, user_id=user)
        new_add.save()
        return redirect('/travel/' + str(travel_id))
    else:
        return redirect('/travel/' + str(travel_id))

def unSignUser(request, travel_id):
    TravelMembers.objects.filter(travel_id=travel_id, user_id=request.user.id).delete()
    return redirect('/travel/' + str(travel_id))

def deleteTravel(request, travel_id):
    travel = Travel.objects.get(id=travel_id)
    creator = CustomUser.objects.get(email=str(travel.creator_id))
    if (creator.id == request.user.id):
        travel.delete()
    return redirect('TravelsPage')
