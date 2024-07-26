from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class destination(models.Model):
    type=(('adventure','adventure'),('wildlife','wildlife'),('beach','beach'),('religeous','religeous'),('archaeological','archaeological'),('Trek','Trek'))
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='destination_image')
    description = models.TextField()
    price = models.IntegerField()
    category=models.CharField(max_length=200,choices=type)
    
    
class book_now(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    destination=models.ForeignKey(destination,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phone=models.CharField(max_length=100)
    total_price=models.IntegerField()
    person=models.IntegerField()

class feedback(models.Model):
    
    type=((1,1),(2,2),(3,3),(4,4),(5,5))
    destination=models.ForeignKey(destination,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    content=models.CharField(max_length=200)
    rating=models.IntegerField(choices=type)
    image=models.ImageField(upload_to='review_image')

    
    
    
    

    
    
