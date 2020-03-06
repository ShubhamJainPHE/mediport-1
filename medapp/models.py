from django.conf import settings
from django.db import models
from django.utils import timezone
gender_choices = [
        (None,'Gender'),
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
]

choices = [
    (None,'Select'),
    ('Yes', 'Yes'),
    ('No', 'No'),
    ('Maybe','Maybe')
]
smoking_choices = [
    (None,'Select'),
    ('Never smoked', 'Never smoked'),
    ('Ex-smoker', 'Ex-smoker'),
    ('Low-smoker(<=10/month)','Low-smoker(<=10/month)'),
    ('Mid-smoker(11-20/month)', 'Mid-smoker(11-20/month)'),
    ('High-smoker(>20/month)','High-smoker(>20/month)')
]
class contact(models.Model):
    fname = models.CharField(max_length=100, null=True, blank=True,default=None)
    lname = models.CharField(max_length=100, null=True, blank=True,default=None)
    email = models.EmailField(blank=True)
    message = models.CharField(max_length=2000, null=True, blank=True,default=None)

class diabetes(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True, default=None)
    gender = models.CharField(max_length=100, choices=gender_choices, null=True)
    age = models.IntegerField(null=True, blank=True)
    total_cholestrol = models.IntegerField(null=True, blank=True)
    hdl_cholestrol = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    waist = models.IntegerField(null=True, blank=True)
    hip = models.IntegerField(null=True, blank=True)
    physically_active = models.CharField(max_length=100, choices=choices, null=True)
    eat = models.CharField(max_length=100, choices=choices, null=True)
    bp = models.CharField(max_length=100, choices=choices, null=True)
    relative_diabetes = models.CharField(max_length=100, choices=choices, null=True)
    parent_diabetes = models.CharField(max_length=100, choices=choices, null=True)
    glucose = models.CharField(max_length=100, choices=choices, null=True)
    smoking = models.CharField(max_length=100, choices=smoking_choices, null=True)
    heart_disease = models.CharField(max_length=100, choices=choices, null=True)
    depression = models.CharField(max_length=100, choices=choices, null=True)
    HbA1c = models.IntegerField(null=True, blank=True)
    haem = models.IntegerField(null=True, blank=True)
