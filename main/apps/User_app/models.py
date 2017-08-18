from __future__ import unicode_literals
from django.db import models

# Create your models here.
# =================================================================
# Model Functions
# =================================================================

# =================================================================
# Models
# =================================================================
#this is the Model for our users ==================
class User(models.Model):
#Users
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email =  models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # objects = UserManager()
