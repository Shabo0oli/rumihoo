from django.db import models
from django.contrib.auth.models import User
from colorfield.fields import ColorField


# Create your models here.


class Location(models.Model):
    Name = models.CharField(max_length=100)

    def __str__(self):
        return "{}".format(self.Name)


class Type(models.Model):
    Name = models.CharField(max_length=100)
    Color = ColorField(default='#FFFFFF')

class Meal(models.Model):
    Name = models.CharField(max_length=100)


class Transport(models.Model):
    Name = models.CharField(max_length=100)

class Accomodation(models.Model):
    Name = models.CharField(max_length=100)

class Language(models.Model):
    Name = models.CharField(max_length=100)

class Tour(models.Model):
    Title = models.CharField(max_length=100)
    Distance = models.IntegerField(blank=True , null=True)

    DistinationList = models.TextField(blank=True , null=True)

    Monthduration = models.IntegerField(blank=True, null=True)
    Dayduration = models.IntegerField(blank=True, null=True)
    Hoursduration = models.IntegerField(blank=True, null=True)

    Tourtype = models.ForeignKey(Type , blank=True, null=True , on_delete=models.CASCADE)

    MinGroupSize = models.IntegerField(blank=True ,null=True)
    MaxGroupSize = models.IntegerField(blank=True , null=True)

    PhysicalRate = models.IntegerField(blank=True ,null=True)

    Meal = models.ManyToManyField(Meal , blank=True, null=True )
    Transport = models.ManyToManyField(Transport , blank=True, null=True)
    Language = models.ManyToManyField(Language , blank=True, null=True )
    Accomodation = models.ManyToManyField(Accomodation , blank=True, null=True )

    Overview = models.TextField(blank=True , null=True)

    Includes = models.TextField(blank=True , null=True)
    Excludes = models.TextField(blank=True , null=True)

    MinPrice = models.IntegerField(blank=True ,null=True)
    Price = models.IntegerField(blank=True ,null=True)

    MainImage = models.ImageField(upload_to='web/static/image/tourImage/', null=True , blank=True)

    Googlemap = models.CharField(blank=True , null=True , max_length=900)




    def __str__(self):
        return "{}".format(self.Title)



class Itinerary(models.Model):
    Title = models.CharField(max_length=100)
    Tour = models.ForeignKey(Tour , blank=True, null=True , on_delete=models.CASCADE)
    Text = models.TextField(blank=True , null=True)
    Highlight = models.TextField(blank=True , null=True)

class TourImage(models.Model):
    Caption = models.CharField(max_length=100)
    Tour = models.ForeignKey(Tour , blank=True, null=True , on_delete=models.CASCADE)
    Image = models.ImageField(upload_to='web/static/image/tourImage/')

class CommentTour(models.Model):
    Text = models.CharField(max_length=200)
    Author = models.CharField(max_length=60)
    Tour = models.ForeignKey(Tour , on_delete=models.CASCADE)