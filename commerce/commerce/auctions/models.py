from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    name = models.CharField(max_length=64)
    category = models.CharField(max_length=64)
    startingbid = models.DecimalField(max_digits=64, decimal_places=2)
    description = models.TextField()
    image = models.URLField()

class Bid(models.Model):
    user = models.CharField(max_length=64)
    bid = models.DecimalField(max_digits=64, decimal_places=2)
    listingid = models.IntegerField()

class Comment(models.Model):
    user = models.CharField(max_length=64)
    comment = models.CharField(max_length=64)
    listingid = models.IntegerField()

class Watchlist(models.Model):
    user = models.CharField(max_length=64)
    listingid = models.IntegerField()

class Winner(models.Model):
    owner = models.CharField(max_length=64)
    winner = models.CharField(max_length=64)
    winprice = models.IntegerField()
    title = models.CharField(max_length=64, null=True)
    listingid = models.IntegerField()
