from django.urls import path, include
from core import views
from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.login_view, name='login'),  
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.view_profile, name='view_profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('', include('core.urls')),
    
]
