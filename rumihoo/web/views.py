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
    tours = list(Tour.objects.all())
    if len(tours) % 4 :
        tours = tours + tours[0: 4-len(tours)%4 ]
    context['tours_list'] = grouped(tours, 4)

    des = list(Destination.objects.all())

    if len(des) % 3:
        des = des + des[0: 3 - len(des) % 3]

    destinations = list(grouped(des , 3 ))

    if (len(des)/3) % 2  :
        destinations = destinations + destinations[0]

    destinations_list = []
    destinations_list2 = []


    for a ,b in grouped(destinations,2) :
        destinations_list.append(a)
        destinations_list2.append(b)

    context['destinations_list'] = destinations_list
    context['destinations_list2'] = destinations_list2
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

    if not request.session.exists(request.session.session_key):
        request.session.create()
    sesssionkey = Session.objects.get(session_key=request.session.session_key)

    context['likesnumber'] = len(Like.objects.filter(RelPost = tour))

    if len(Like.objects.filter( RelPost=tour , User=sesssionkey ) ) == 0 :
        context['classattr'] = "far gray"
    else :
        context['classattr'] = "fa red"

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


@csrf_exempt
def like(request):
    if not request.session.exists(request.session.session_key):
        request.session.create()
    tour = Tour.objects.get(id=request.POST['tourid'])
    context = {}
    sesssionkey = Session.objects.get(session_key = request.session.session_key)
    likeobj = Like.objects.filter(RelPost=tour, User=sesssionkey)
    if len( likeobj) == 0 :
        l = Like( RelPost=tour , User=sesssionkey )
        l.save()
        context['response'] = '200'
        context['message'] = 'لایک کردی'
        context['count'] =  len(Like.objects.filter(RelPost=tour))
        return JsonResponse(context, encoder=JSONEncoder)
    else :
        Like.objects.filter(RelPost=tour, User=sesssionkey).delete()
        context['response'] = '200'
        context['message'] = 'لایک کرده بودی قبلا'
        context['count'] =  len(Like.objects.filter(RelPost=tour))
        return JsonResponse(context, encoder=JSONEncoder)
