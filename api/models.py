from pyexpat import model
from django.db import models


class RoomModel(models.Model):
    code = models.CharField(max_length=8, default="", unique=True) 
    host = models.CharField(max_length=50, unique=True)
    guest_can_pause = models.BooleanField(null=False, default=False)
    votes_to_skip = models.IntegerField(null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'Room'
    
    def __str__(self):
        return self.code