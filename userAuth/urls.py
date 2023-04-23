from django.urls import path
from userAuth import views

urlpatterns = [
	path('register/', views.registerUser),
	path('login/', views.loginUser),
]