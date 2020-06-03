from django.urls import path
from . import views

app_name = 'articles'
urlpatterns  = [
	path('index', views.index, name = 'index'),
	path('<int:articleId>/', views.detail, name = 'detail'),
	path('<int:articleId>/leaveComment/', views.leaveComment, name = 'leaveComment'),
]