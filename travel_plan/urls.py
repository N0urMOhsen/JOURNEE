from django.urls import path
from . import views 

app_name = 'travel_plan'

urlpatterns = [
    path('booking/', views.booking, name='booking'),
]
