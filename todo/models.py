from django.db import models
from authentication.models import User
from helpers.models import TrackingModel
# from django.contrib.auth import get_user_model



class Todo(TrackingModel):
    title = models.CharField(max_length=255)
    describition = models.TextField()
    is_completed = models.BooleanField(default=False)
    owner = models.ForeignKey(to=User,on_delete=models.CASCADE)
    
    
    
    
    def __str__(self):
        return self.title

        
    