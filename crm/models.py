from django.db import models

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
        
   
