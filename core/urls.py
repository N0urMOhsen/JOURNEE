from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('base/', views.base, name='base'), 
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
]
