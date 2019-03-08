from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class PersonalRecord(models.Model):
    exercise = models.CharField(max_length=50)
    weight = models.FloatField()
    reps = models.IntegerField(default=1)
    date = models.DateField(default=date.today)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)