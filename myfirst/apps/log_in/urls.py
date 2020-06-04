from django.urls import path
from . import views
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

app_name = 'log_in'
urlpatterns  = [
	path('register/', views.register, name='register'),
	path('', views.user_login, name='user_login'),
	path('edit/', views.edit, name='edit_profile'),
	path('logout/', views.LogoutView.as_view(next_page = '/logged_out'), name='logout'),
	path('logged_out', views.logout_page, name='logged_out')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)