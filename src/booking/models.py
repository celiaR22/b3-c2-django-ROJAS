from django.db import models

class schoolLessons (models.Model):
    schoolName = models.CharField(max_length=128)
    title = models.CharField(max_length=128, default= 'test')
    image = models.ImageField(upload_to="image", blank=True, null =True)
    nbPerson = models.IntegerField(default = 0)
    price = models.FloatField(default = 0.0)
    date =models.DateField(auto_now= True)
    description = models.TextField(blank=True)

def __str__(self):
    return self.title
