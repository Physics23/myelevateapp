from django.db import models
from django.contrib.auth.models import User

class Myclients(models.Model):
    
    name = models.CharField(max_length = 255)
    firstname = models.CharField(max_length = 255)
    email = models.EmailField(max_length = 255)
    adress1 = models.CharField(max_length = 255)
    city = models.CharField(max_length = 255)
    country = models.CharField(max_length = 255)
    profession = models.CharField(max_length = 255)
    date_created = models.DateTimeField( )
    
    def __str__(self):
        return self.name + ""+ self.firstname
    
    
    class Meta():
        verbose_name = 'Myclients'
        verbose_name_plural = 'Myclients'
        
        
        
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length = 255, null=True)
    adress1 = models.CharField(max_length = 255, null=True)
    city = models.CharField(max_length = 255,null=True)
    country = models.CharField(max_length = 255,null=True)
    profession = models.CharField(max_length = 255, null=True)

    # Add any other fields you want for the user profile

    def __str__(self):
        return self.user.username
    
    

class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length = 255, null=True)
    content= models.TextField()
    

    # Add any other fields you want for the user profile

    def __str__(self):
        return self.name
    
    
    
    
        
   
