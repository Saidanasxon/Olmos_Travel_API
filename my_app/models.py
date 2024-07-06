from django.db import models
from django.contrib.auth.models import User

class Tour_class(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Tour(models.Model):
    price = models.PositiveIntegerField()
    tour_class = models.ForeignKey(Tour_class, on_delete=models.CASCADE)
    aviacompany = models.CharField(max_length=255)
    duration = models.PositiveIntegerField()
    eating = models.PositiveIntegerField()
    visa = models.BooleanField(default=True)
    medical_care = models.BooleanField(default=True)
    instructor = models.BooleanField(default=True)
    water = models.BooleanField(default=True)
    jacked = models.BooleanField(default=True)
    bag_and_emblem = models.BooleanField(default=True)

    def __str__(self):
        return f'Tour: {self.tour_class.name}, Price: {self.price}' 