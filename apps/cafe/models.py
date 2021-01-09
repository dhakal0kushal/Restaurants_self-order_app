from django.db import models
from django.contrib.auth.models import User

# models here

class Cafe(models.Model):
  user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE)
  name = models.CharField(max_length=255)
  address = models.TextField(blank=True, null=True)

  class Meta:
    verbose_name_plural='Cafe'
    
  def __str__(self):
    return self.name