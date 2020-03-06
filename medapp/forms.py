from .models import *
from django import forms

class Contact(forms.ModelForm):
    class Meta:
        model = contact
        fields = ['fname', 'lname', 'email', 'message']

class Diabetes(forms.ModelForm):
    class Meta:
        model = diabetes
        fields = ['name','gender', 'age','total_cholestrol','hdl_cholestrol', 'weight', 'height', 'waist', 'hip', 'physically_active',
                  'eat', 'bp', 'relative_diabetes','parent_diabetes', 'glucose', 'smoking', 'heart_disease', 'depression',
                  'HbA1c', 'haem']