from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def booking(request):
    context = {}  
    return render(request, 'booking.html', context)
