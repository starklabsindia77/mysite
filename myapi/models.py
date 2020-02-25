# models.py
from django.db import models

class Driver(models.Model):
    name = models.CharField(max_length=60)
    mobile = models.CharField(max_length=60)
    vehicle_type = models.CharField(max_length=60)
    password = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '%s %s' % (self.name, self.mobile)