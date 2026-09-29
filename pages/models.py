from django.db import models
from django.urls import reverse
from django.db import models

# Create your models here.

class Pokemon(models.Model):
    name = models.CharField(max_length=50)
    
    type = models.CharField(max_length=50)

    dexNum = models.CharField(max_length=4)

    gen = models.CharField(max_length=20)

    cover = models.ImageField(upload_to="images/")


    def __str__(self):
        return self.name 

    def get_absolute_url(self):
        return reverse("pokemon_detail", kwargs={"pk": self.pk})





