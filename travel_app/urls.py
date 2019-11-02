from django.urls import path
from .views import *

urlpatterns = [
    path('', viewAllTravels, name="TravelsPage"),
    path('mytravels/', viewMyTravels, name="TravelsMy"),
    path('<int:travel_id>/', viewOneTravel, name="TravelPage"),
    path('<int:travel_id>/sign', userToMembers, name="TravelSign"),
    path('<int:travel_id>/unsign', unSignUser, name="TravelUnsign"),
    path('<int:travel_id>/delete', deleteTravel, name="TravelDelete"),
]
