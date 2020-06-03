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
	path('edit/', views.edit, name='edit_profile')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)