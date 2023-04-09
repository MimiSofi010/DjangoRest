from django.shortcuts import render
from django.http import HttpResponse
from passenger.models import Passenger
from django.db.models import Q
from django.db.models import Max


# Create your views here.

'Assigment 1'
def passengerData(request):
    passengers = Passenger.objects.all()
    return HttpResponse(passengers)


'Assigment 2'
def passengerNameData(request):
    passengers = Passenger.objects.all().values('firstName', 'lastName')
    return HttpResponse(passengers)


'Assigment 3'
def passengerNameDataFiltered(request):
    passengers = Passenger.objects.filter(Q(firstName__startswith='M') | Q(lastName__startswith='G')).values('firstName', 'lastName')
    return HttpResponse(passengers)


'Assigment 4'
def passengerRewardRank(request):
    'Orders from lower to greatter'
    passengers = Passenger.objects.all().order_by('rewardPoints')
    return HttpResponse(passengers)


'Assigment 5'
def passengerMaxReward(request):
    passenger = Passenger.objects.all().aggregate(Max('rewardPoints'))
    return HttpResponse(passenger)