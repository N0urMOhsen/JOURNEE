from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.


class TravelGroup(models.Model):
    TGID = models.AutoField(primary_key=True)
    TGCategory = models.CharField(max_length=100)

    def __str__(self):
        return self.TGCategory

class TravelStyle(models.Model):
    TSID = models.AutoField(primary_key=True)
    Theme = models.CharField(max_length=100)

    def __str__(self):
        return self.Theme

class Destination(models.Model):
    Country = models.CharField(max_length=100)
    City = models.CharField(max_length=100)

    class Meta:
        unique_together = ('Country', 'City')

    def __str__(self):
        return f"{self.City}, {self.Country}"

class Plan(models.Model):
    PlanID = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    destination_country = models.CharField(max_length=100)
    destination_city = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    travel_group = models.ForeignKey(TravelGroup, on_delete=models.CASCADE)
    travel_style = models.ForeignKey(TravelStyle, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.destination_city}, {self.destination_country} ({self.start_date} - {self.end_date})'

class Accommodation(models.Model):
    AccommodationID = models.AutoField(primary_key=True)
    PlanID = models.ForeignKey(Plan, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    Description = models.TextField()
    Category = models.CharField(max_length=100)
    PriceRange = models.CharField(max_length=50)
    Location = models.CharField(max_length=100)

    def __str__(self):
        return self.Name

class Transportation(models.Model):
    TransportationID = models.AutoField(primary_key=True)
    PlanID = models.ForeignKey(Plan, on_delete=models.CASCADE)
    Type = models.CharField(max_length=100)
    Origin = models.CharField(max_length=100)
    Destination = models.CharField(max_length=100)
    Duration = models.DurationField()
    EstimatedCost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.Type} from {self.Origin} to {self.Destination}"

class Review(models.Model):
    ReviewID = models.AutoField(primary_key=True)
    PlanID = models.ForeignKey(Plan, on_delete=models.CASCADE)
    Comment = models.TextField()
    Rating = models.IntegerField()

    def __str__(self):
        return f"Review {self.ReviewID} for Plan {self.PlanID.PlanID}"

class Activity(models.Model):
    ActivityID = models.AutoField(primary_key=True)
    PlanID = models.ForeignKey(Plan, on_delete=models.CASCADE)
    Duration = models.DurationField()

    def __str__(self):
        return f"Activity {self.ActivityID} for Plan {self.PlanID.PlanID}"

