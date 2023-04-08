from django.urls import path
from forum_app import views


urlpatterns = [
    path('', views.login, name='login')    
]
