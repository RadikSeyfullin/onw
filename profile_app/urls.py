from django.urls import path
from profile_app import views

urlpatterns = [
    path('', views.profile_view, name='ProfilePage')
]
