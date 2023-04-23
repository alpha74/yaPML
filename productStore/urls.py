from django.urls import path
from productStore import views

urlpatterns = [
	path('', views.ProductListCreate.as_view()),
	path('<str:pk>/', views.ProductDetail.as_view())
]