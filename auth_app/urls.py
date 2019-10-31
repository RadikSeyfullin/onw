from django.urls import path
from auth_app import views

urlpatterns = [
    path('logout/', views.logout, name="AuthLogout"),
    path('', views.viewLoginPage, name="LoginPage"),
    path('register/', views.register, name="Registr"),
    path('login/', views.login, name="Login"),
]
