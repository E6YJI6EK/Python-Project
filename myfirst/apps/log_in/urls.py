from django.urls import path
from . import views

app_name = 'log_in'
urlpatterns  = [
	path('register/', views.register, name='register'),
	path('login/', views.user_login, name='user_login'),
]