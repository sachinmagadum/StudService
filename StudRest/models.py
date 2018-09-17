from django.db import models
from django_countries.fields import CountryField

class StudentModel(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=50)
    #skills = models.ManyToManyField()
    country = CountryField()
    remarks = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    isactive = models.BooleanField(default=False)

    def __str__(self):
        return self.name