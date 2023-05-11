from django.urls import path
from forum_app import views
from .views import  BeitragDetail


urlpatterns = [
    path('', views.user_login, name='login'),  
    path('register/', views.register, name='register'),
    
    path('beitrag/<int:pk>/', BeitragDetail.as_view(), name='beitrag-detail'),
]
