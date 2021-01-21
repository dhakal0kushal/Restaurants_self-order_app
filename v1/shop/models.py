from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class BranchType(models.Model):
  name = models.CharField(max_length=16)

  def __str__(self):
    return self.name

class Shop(models.Model):
  name = models.CharField(max_length=255)
  owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

class Country(models.Model):
  name = models.CharField(max_length = 255)
  alpha_two_code = models.CharField(max_length = 2, blank=True, null=True)

  def __str__(self):
      return self.name
  

class ShopBranch(models.Model):
  shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
  branch_type = models.ForeignKey(BranchType, on_delete=models.DO_NOTHING,blank=True, null=True)
  location = models.CharField(max_length=255, blank=True, null=True)
  city = models.CharField(max_length=255)
  country = models.ForeignKey(Country, on_delete=models.DO_NOTHING)
  description = models.TextField()
  opening_time = models.TimeField()
  closing_time = models.TimeField()

def __str__(self):
    return self.shop.name
