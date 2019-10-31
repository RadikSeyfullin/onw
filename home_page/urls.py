from django.urls import path
from home_page import views

urlpatterns = [
    path('', views.index, name="HomePage"),
    path('about/', views.about, name="AboutPage"),
]
