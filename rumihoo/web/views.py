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





from .models import *




def index(request):
    context = {}
    tours = Tour.objects.all()

    if len(tours) :
        toursinfo = []
        for tour in tours :
            tour_i = tour
            tour_i.commentcount = CommentTour.objects.filter(Tour= tour).count()
            toursinfo.append(tour_i)

        i=0
           # while len(toursinfo) < 4 :
           #  toursinfo.append(toursinfo[i])
           #  i = i+1
        context['tours'] = toursinfo

        if len(tours) > 4 :
            toursinfo = []
            for tour in tours[4:]:
                tour_i = tour
                tour_i.commentcount = CommentTour.objects.filter(Tour=tour).count()
                toursinfo.append(tour_i)
            i = 0
            # while len(toursinfo) < 4:
            #     toursinfo.append(toursinfo[i])
            #     i = i + 1
            context['tours2'] = toursinfo
    return render(request, 'index.html', context)


def tour(request , id):
    context = {}
    tour = Tour.objects.get(id = id)
    context['tour'] = tour
    context['comments'] = CommentTour.objects.filter(Tour=tour)
    context['rout'] = tour.DistinationList.split('\n')
    context['itinerary'] = Itinerary.objects.filter(Tour=tour)

    context['includes'] = tour.Includes.split('\n')
    context['excludes'] = tour.Excludes.split('\n')
    return render(request, 'tour.html', context)
