from django.db import models
from django.contrib.auth.models import User
from colorfield.fields import ColorField
from django.contrib.sessions.models import Session



# Create your models here.


class Location(models.Model):
    Name = models.CharField(max_length=100)

    def __str__(self):
        return "{}".format(self.Name)


class Type(models.Model):
    Name = models.CharField(max_length=100)
    Color = ColorField(default='#FFFFFF')

    def __str__(self):
        return "{}".format(self.Name)

class Meal(models.Model):
    Name = models.CharField(max_length=100)

    def __str__(self):
        return "{}".format(self.Name)


class Transport(models.Model):
    Name = models.CharField(max_length=100)

    def __str__(self):
        return "{}".format(self.Name)

class Accomodation(models.Model):
    Name = models.CharField(max_length=100)

    def __str__(self):
        return "{}".format(self.Name)

class Language(models.Model):
    Name = models.CharField(max_length=100)

    def __str__(self):
        return "{}".format(self.Name)

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
    PriceText = models.CharField(max_length=100 , null=True , blank=True)

    MainImage = models.ImageField(upload_to='web/static/image/tourImage/', null=True , blank=True)

    Googlemap = models.CharField(blank=True , null=True , max_length=900)

    def __str__(self):
        return "{}".format(self.Title)



class Itinerary(models.Model):
    Title = models.CharField(max_length=100)
    Tour = models.ForeignKey(Tour , blank=True, null=True , on_delete=models.CASCADE)
    Text = models.TextField(blank=True , null=True)
    Highlight = models.TextField(blank=True , null=True)

    def __str__(self):
        return "{} - {}".format(self.Title , self.Tour.Title)

class TourImage(models.Model):
    Caption = models.CharField(max_length=100)
    Tour = models.ForeignKey(Tour , blank=True, null=True , on_delete=models.CASCADE)
    Image = models.ImageField(upload_to='web/static/image/tourImage/')

    def __str__(self):
        return "{} - {}".format(self.Caption, self.Tour.Title)

class CommentTour(models.Model):
    Text = models.CharField(max_length=200)
    Author = models.CharField(max_length=60)
    Tour = models.ForeignKey(Tour , on_delete=models.CASCADE)
    Date = models.DateField(null=True , blank=True)



class Destination(models.Model):
    Name = models.CharField(max_length=100)
    Image = models.ImageField(upload_to='web/static/image/DistImage/')
    Population = models.IntegerField(blank=True, null=True)
    Climate = models.CharField(max_length=20 , blank=True , null=True)
    Type = models.ForeignKey(Type , blank=True, null=True , on_delete=models.CASCADE)
    Distance = models.IntegerField(blank=True , null=True)
    ReviewText = models.TextField(blank=True , null=True)
    Meal = models.ManyToManyField(Meal, blank=True, null=True)
    Transport = models.ManyToManyField(Transport, blank=True, null=True)
    Language = models.ManyToManyField(Language, blank=True, null=True)
    Accomodation = models.ManyToManyField(Accomodation, blank=True, null=True)

    def __str__(self):
        return "{}".format(self.Name)




class LocalFood(models.Model):
    Name = models.CharField(max_length=100)
    Image = models.ImageField(upload_to='web/static/image/DistImage/')
    Destination = models.ForeignKey(Destination , blank=True, null=True , on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.Name)


class MustSee(models.Model):
    Name = models.CharField(max_length=100)
    Image = models.ImageField(upload_to='web/static/image/DistImage/')
    Destination = models.ForeignKey(Destination , blank=True, null=True , on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.Name)


class Nature(models.Model):
    Name = models.CharField(max_length=100)
    Image = models.ImageField(upload_to='web/static/image/DistImage/')
    Destination = models.ForeignKey(Destination , blank=True, null=True , on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.Name)


class WhereToEat(models.Model):
    Name = models.CharField(max_length=100)
    Image = models.ImageField(upload_to='web/static/image/DistImage/')
    Destination = models.ForeignKey(Destination , blank=True, null=True , on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.Name)


class Handicraft(models.Model):
    Name = models.CharField(max_length=100)
    Image = models.ImageField(upload_to='web/static/image/DistImage/')
    Destination = models.ForeignKey(Destination , blank=True, null=True , on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.Name)


class UnescoSite(models.Model):
    Name = models.CharField(max_length=100)
    Image = models.ImageField(upload_to='web/static/image/DistImage/')
    Destination = models.ForeignKey(Destination , blank=True, null=True , on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.Name)




class Blog(models.Model):
    Text = models.TextField()
    Image = models.ImageField(upload_to='web/static/image/DistImage/')
    Title = models.CharField(max_length=100)
    Date = models.DateField(null=True , blank=True)
    Lead = models.CharField(max_length=200,blank=True,null=True)

    def __str__(self):
        return "{}".format(self.Title)



class Passenger(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    PhoneNumber = models.CharField(max_length=30 , null=True , blank=True)
    Email = models.CharField(max_length=50 , null=True , blank=True)

    def __str__(self):
        return "{}".format(self.User)




class Booking(models.Model):
    Tour = models.ForeignKey(Tour , on_delete=models.CASCADE)
    Passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    Date = models.DateField(null=True,blank=True)
    ResrvTime = models.DateTimeField(auto_now_add=True)
    Status = models.CharField(max_length=50 , null=True, blank=True)
    Persons = models.IntegerField(null=True,blank=True)
    PyamentStatus = models.CharField(max_length=100, null=True, blank=True)
    Track = models.CharField(max_length=50, null=True, blank=True)
    Order = models.CharField(max_length=20)

    def __str__(self):
        return "{} - {}".format(self.Passenger.User.username , self.Passenger.PhoneNumber )

class Like(models.Model):
    RelPost = models.ForeignKey(Tour,on_delete=models.CASCADE)
    User = models.ForeignKey(Session, on_delete=models.SET_NULL , null=True)



class MainPageSlider(models.Model):
    Image = models.ImageField(upload_to='web/static/image/SliderImage/')
    Title = models.CharField(max_length=100 , null=True , blank=True)
    Link = models.URLField(null=True,blank=True)