from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from django.core import serializers
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import *
from json import JSONEncoder
from django.contrib.admin.views.decorators import staff_member_required
import json


import random


from .models import *


def grouped(l, n):
    for i in range(0, len(l), n):
        yield l[i:i+n]


def index(request):
    context = {}
    tours = Tour.objects.all()
    if len(tours)%3 :
        tours = tours + tours[0:(3-(len(tours)%3))]
    context['tours_list'] = grouped(tours, 3)
    context['destinations_list'] = grouped(Destination.objects.all(), 3)
    context['blog_list'] = grouped(Blog.objects.all(), 3)

    return render(request, 'index.html', context)

@csrf_exempt
def tour(request , id):
    context = {}
    tour = Tour.objects.get(id=id)
    if request.method =="POST":
        user = User.objects.create_user(username="Pass_"+request.POST['name']+str(random.randint(1,1000000)), email=request.POST['email'], password="1234")
        user.save()
        passenger = Passenger(Email=request.POST['email'] , PhoneNumber=request.POST['phone'] , User=user)
        passenger.save()
        booking = Booking(Passenger=passenger , Tour = tour , Date=request.POST['date'] , Persons=int(request.POST['number']))
        booking.save()
        context['bookmessage'] = 'Successfully booked'


    context['tour'] = tour
    context['comments'] = CommentTour.objects.filter(Tour=tour)
    context['rout'] = tour.DistinationList.split('\n')
    context['itinerary'] = Itinerary.objects.filter(Tour=tour)

    context['includes'] = tour.Includes.split('\n')
    context['excludes'] = tour.Excludes.split('\n')
    return render(request, 'tour.html', context)

def destination(request , name)  :
    context = {}
    destination = Destination.objects.get(Name = name)
    context['destination'] = destination
    context['localfoods'] = LocalFood.objects.filter(Destination=destination)
    context['mustsees'] = MustSee.objects.filter(Destination=destination)
    context['natures'] = Nature.objects.filter(Destination=destination)
    context['wheres'] = WhereToEat.objects.filter(Destination=destination)
    context['handicrafts'] = Handicraft.objects.filter(Destination=destination)
    context['unescos'] = UnescoSite.objects.filter(Destination=destination)


    tours = Tour.objects.all()

    if len(tours) :
        toursinfo = []
        for tour in tours :
            tour_i = tour
            tour_i.commentcount = CommentTour.objects.filter(Tour= tour).count()
            toursinfo.append(tour_i)

        i=0
        context['tours'] = toursinfo



    return render(request, 'destination.html', context)
