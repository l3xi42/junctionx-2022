from django.db import models
from django.forms.models import modelform_factory

# Create your models here.
class known_vendors(models.Model):
    #place, merchant name
    merchant_name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    def __str__(self):
        return self.merchant_name


class item(models.Model):
    #receipt_name, date, cash_register, total, place, merchant name
    receipt_name = models.CharField(max_length=200)
    date = models.DateTimeField('date published')
    cash_register = models.CharField(max_length=100)
    total = models.FloatField()
    merchant_name = models.ForeignKey(known_vendors, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.receipt_name
    
"""
form = modelform_factory(, fields=('gender', 'gender_na', 'height', 'height_na',))
populated_form = form(data=my_json)

if populated_form.is_valid():
    populated_form.save()
else:
    populated_form.errors = '-1'
    populated_form.save()
    
"""
