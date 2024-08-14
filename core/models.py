from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Item(models.Model):
    user_name = models.ForeignKey(User, on_delete= models.CASCADE, default= 1)
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length= 500, default= "https://tse1.mm.bing.net/th/id/OIP.kz5A86qjMCk6lHYchAsRZAHaHa?rs=1&pid=ImgDetMain")
    
    
    
    def __str__(self):
        return self.item_name
    
    
    # whenever we create an item we want to be redirected to this page thats why we have created this func
    def get_absolute_url(self):
        return reverse("core:detail", kwargs={"pk": self.pk})
    

