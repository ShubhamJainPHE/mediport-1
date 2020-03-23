from django.shortcuts import render
from django.shortcuts import render_to_response
from .forms import *
from django.http import HttpResponseRedirect
# from django.core.mail import send_mail
from django.contrib import messages
import request
from django.shortcuts import get_object_or_404
import tabula
import pandas as pd
import os
import numpy as np
# Create your views here.


def home(request):
    return render(request, 'home/home.html', {'':''})

def diabetes_report(request):

    return render(request, 'Diabetes/Report.html',)

def blood_report(request):

    return render(request, 'Blood Profile/Report.html',)

def bloodprofile(request):

    return render(request, 'Blood Profile/bloodprofile.html',)

def diabriskpred(request):
    if request.method == 'POST':
        form = Diabetesreport(request.POST, request.FILES)
        if form.is_valid():
            report = request.FILES.get('report')
            df = tabula.read_pdf(report, pages='all')
            list_values = []
            for n in range(len(df)):
                page = df[n]
                for name in page.columns.values:
                    c = page[page[name].astype(str).str.contains(r'(?i)total cholesterol ', na=False, regex=True)]
                    d = page[page[name].astype(str).str.contains('HEMOGLOBIN', na=False, regex=True)]
                    value1 = c['VALUE'].values
                    value2 = d['VALUE'].values
                    for i in value1:
                        list_values.append(i)
                    for i in value2:
                        list_values.append(i)
            cholesterol = list_values[0]
            hemoglobin = list_values[1]
            dic = {'cholesterol':cholesterol,'hemoglobin':hemoglobin }
            print(list_values)
            return render(request, 'Diabetes/Report.html',dic)
            # print(df[df['TEST NAME'].str.contains(r'TOTAL CHOLESTEROL(?!$)')])
            # context.save()
        else:
            print('hoooo')
            form.save()
            return render(request, 'Diabetes/diabriskpred.html', {'message':'Some error occurred. Please try again. '})
    else:
        Diabetesreport()
    return render(request, 'Diabetes/diabriskpred.html')

def contact(request):

    if request.method == 'POST':
        form = Contact(request.POST)
        if form.is_valid():
            fname = form.cleaned_data['fname']
            lname = form.cleaned_data['lname']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            form.save()
    return render(request, 'contact/contact.html', {'Title':'Contact Us'},{'':'','message':"Your form was submitted successfully!"})

