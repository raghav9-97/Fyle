from django.db import models

class Branches(models.Model):
    ifsc = models.CharField(max_length=15,primary_key=True)
    bank_id = models.IntegerField()
    branch = models.CharField(max_length=75)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=30)