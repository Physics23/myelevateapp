from django.db import models

# Create your models here.

from django.contrib.auth.models import User



class ReceiverShipCase(models.Model):
    
    title = models.CharField(max_length=255)
    court =  models.CharField(max_length=255)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, 
            choices=[
                ('active', 'Active'),
                ('closed', 'Closed'),  
    ])
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.court
        