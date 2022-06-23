from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Test(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=0)

    def __str__(self):
        return self.name

class Patient(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='selected')
    # patient_id = models.IntegerField()
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length = 254)
    age = models.DecimalField(max_digits=6, decimal_places=0)
    gender = models.CharField(max_length=100)
    phone = models.DecimalField(max_digits=6, decimal_places=0)
    # test_id = models.IntegerField()
    # test_name = models.CharField(max_length=100)
    total_price = models.DecimalField(max_digits=6, decimal_places=0)
    advance = models.DecimalField(max_digits=6, decimal_places=0)
    due = models.DecimalField(max_digits=6, decimal_places=0)
    #status = models.BooleanField()
    #report_status = models.BooleanField()
    role = models.CharField(max_length=100,default='Patient')