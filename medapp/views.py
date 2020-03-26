from django.shortcuts import render
from django.shortcuts import render_to_response
from .forms import *
from django.http import HttpResponseRedirect
# from django.core.mail import send_mail
from django.contrib import messages
import request
from django.shortcuts import get_object_or_404
import tabula
from tabula import read_pdf
import pandas as pd
import os
import numpy as np
from django.http import JsonResponse
# Create your views here.

def home(request):
    return render(request, 'home/home.html', {'':''})

def diabetes_report(request):

    return render(request, 'Diabetes/Report.html',)

def coronavirus_result(request):

    return render(request, 'Coronavirus/risk_result_covid19.html',{"Title":"Risk Score:COVID-19"})

def coronavirus(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Coronaform(request.POST)
        # check whether xit's valid:
        if form.is_valid():
            email = request.POST.get('email')
            sex = request.POST.get('sex')
            age = request.POST.get('age')
            smoking = request.POST.get('smoking')
            travel = request.POST.get('travel')
            temp= request.POST.get('temp')
            any_comorbidity = request.POST.get('any_comorbidity')
            curr_comorbidity = request.POST.get('curr_comorbidity')
            context = corona_model.objects.create(
                email=email,
                sex=sex,
                age=age,
                smoking=smoking,
                travel=travel,
                temp=temp,
                any_comorbidity=any_comorbidity,
                curr_comorbidity=curr_comorbidity
            )

            lis = []
            sex_value = [25.43, 0]
            if sex == 'Male':
                lis.append(sex_value[0])
            else:
                lis.append(sex_value[1])

            age_value = [18.84, 0]
            if age == '>50':
                lis.append(age_value[0])
            else:
                lis.append(age_value[1])

            smoking_value = [10.03, 0]
            if smoking == 'Yes':
                lis.append(smoking_value[0])
            else:
                lis.append(smoking_value[1])

            travel_value = [0,30,40,0]
            if travel == 'Contact with someone with dry cough fever or visible difficuly in breathing':
                lis.append(travel_value[1])
            elif travel == 'History of travel or meeting in affected geographical area on or after (T-14 days)':
                lis.append(travel_value[2])
            else:
                lis.append(0)

            temp_value = [0, 30, 40]
            if temp == 'Fever(98.6-102)':
                lis.append(temp_value[1])
            elif temp == 'High Fever(>102)':
                lis.append(temp_value[2])
            else:
                lis.append(0)

            any_comorbidity_value = [26.78, 0]
            if any_comorbidity == 'None':
                lis.append(any_comorbidity_value[1])
            elif any_comorbidity == 'High Fever(>102)':
                lis.append(any_comorbidity_value[2])
            else:
                lis.append(0)

            curr_comorbidity_value = [34.9, 46.26, 27.74, 18.61, 36.09, 29.86, 0]
            if curr_comorbidity == 'None':
                lis.append(curr_comorbidity_value[6])
            elif curr_comorbidity == 'Kidney Disease':
                lis.append(curr_comorbidity_value[0])
            elif curr_comorbidity == 'Asthma or Lung Disease':
                lis.append(curr_comorbidity_value[1])
            elif curr_comorbidity == 'Cerebrovascular Disease':
                lis.append(curr_comorbidity_value[2])
            elif curr_comorbidity == 'Tumor':
                lis.append(curr_comorbidity_value[3])
            elif curr_comorbidity == 'Diabetes':
                lis.append(curr_comorbidity_value[4])
            else:
                lis.append(curr_comorbidity_value[5])
            value = str(sum(lis))
            result = {"risk_score":value}
            print(result)
            return render(request, 'Coronavirus/risk_result_covid19.html', result)

        # return JsonResponse(response_data)
        return render(request, 'Coronavirus/risk_result_covid19.html')


    return render(request, 'Coronavirus/coronavirus.html',)



def bloodprofile(request):

    if request.method == 'POST':
        form = Bloodreport(request.POST, request.FILES)
        if form.is_valid():
            report = request.FILES.get('report')
            df = tabula.read_pdf(report, pages='all')
            page = list(df[0].columns.values)
            a = page[0]
            b = page[1]
            c = page[2]
            d = page[3]
            df[0].rename(columns={a: "Test Name", b: "RESULT", c: "Unit", d: "Bio Ref.Interval"}, inplace=True)
            # page[4] = 'Method'
            page = df[0]
            list_values = {}

            for name in page.columns.values:
                a = page[page[name].astype(str).str.contains('Hemoglobin', na=False, regex=True)]
                b = page[page[name].astype(str).str.contains(r'(?i)RBC', na=False, regex=True)]
                c = page[page[name].astype(str).str.contains(r'(?i)Total Leucocyte Count', na=False, regex=True)]
                d = page[page[name].astype(str).str.contains(r'(?i)Platelet Count', na=False, regex=True)]
                e = page[page[name].astype(str).str.contains(r'(?i)PCV', na=False, regex=True)]
                f = page[page[name].astype(str).str.contains(r'(?i)MCV', na=False, regex=True)]
                g = page[page[name].astype(str).str.contains(r'(?i)MCH', na=False, regex=True)]
                h = page[page[name].astype(str).str.contains(r'(?i)Monocytes', na=False, regex=True)]
                i = page[page[name].astype(str).str.contains(r'(?i)MCHC', na=False, regex=True)]
                j = page[page[name].astype(str).str.contains(r'(?i)RDW-SD', na=False, regex=True)]
                k = page[page[name].astype(str).str.contains(r'(?i)RDW-CV', na=False, regex=True)]
                l = page[page[name].astype(str).str.contains(r'(?i)Neutrophils', na=False, regex=True)]
                m = page[page[name].astype(str).str.contains(r'(?i)Lymphocytes', na=False, regex=True)]
                n = page[page[name].astype(str).str.contains(r'(?i)Neutrophils', na=False, regex=True)]
                o = page[page[name].astype(str).str.contains(r'(?i)Eosinophils', na=False, regex=True)]
                p = page[page[name].astype(str).str.contains(r'(?i)Basophils', na=False, regex=True)]
                q = page[page[name].astype(str).str.contains(r'(?i)MPV', na=False, regex=True)]
                r = page[page[name].astype(str).str.contains(r'(?i)PDW', na=False, regex=True)]
                s = page[page[name].astype(str).str.contains(r'(?i)Immature Granulocyte Count', regex=True)]

                try:
                    value1 = a['RESULT'].values
                    list_values['Hemoglobin'] = value1.item(0)
                    value2 = b['RESULT'].values
                    list_values['RBC'] = value2.item(0)
                    value3 = c['RESULT'].values
                    list_values['Leucocyte'] = value3.item(0)
                    value4 = d['RESULT'].values
                    list_values['Platelet'] = value4.item(0)
                    value5 = e['RESULT'].values
                    list_values['PCV'] = value5.item(0)
                    value6 = f['RESULT'].values
                    list_values['MCV'] = value6.item(0)
                    value7 = g['RESULT'].values
                    list_values['MCH'] = value7.item(0)
                    value8 = h['RESULT'].values
                    list_values['Monocytes'] = value8.item(0)
                    value9 = i['RESULT'].values
                    list_values['MCHC'] = value9.item(0)
                    value10 = j['RESULT'].values
                    list_values['RDWSD'] = value10.item(0)
                    value11 = k['RESULT'].values
                    list_values['RDWCV'] = value11.item(0)
                    value12 = l['RESULT'].values
                    list_values['Neutrophils'] = value12.item(0)
                    value13 = m['RESULT'].values
                    list_values['Lymphocytes'] = value13.item(0)
                    value14 = n['RESULT'].values
                    list_values['Neutrophils'] = value14.item(0)
                    value15 = o['RESULT'].values
                    list_values['Eosinophils'] = value15.item(0)
                    value16 = p['RESULT'].values
                    list_values['Basophils'] = value16.item(0)
                    value17 = q['RESULT'].values
                    list_values['MPV'] = value17.item(0)
                    value18 = r['RESULT'].values
                    list_values['PDW'] = value18.item(0)
                    value19 = s['RESULT'].values
                    list_values['Granulocyte'] = value19.item(0)
                except IndexError:
                    pass
            return render(request, 'Blood Profile/Report.html', list_values)
            # print(df[df['TEST NAME'].str.contains(r'TOTAL CHOLESTEROL(?!$)')])
            # context.save()
        else:
            print('hoooo')
            form.save()
            return render(request, 'Blood Profile/bloodprofile.html',
                          {'message': 'Some error occurred. Please try again. '})
    else:
        Bloodreport()

    return render(request, 'Blood Profile/bloodprofile.html',)

def diabriskpred(request):
    if request.method == 'POST':
        form = Diabetesreport(request.POST, request.FILES)
        if form.is_valid():
            report = request.FILES.get('report')
            df = tabula.read_pdf(report, pages='all')
            value_cholesterol = []
            value_hemoglobin = []
            for n in range(len(df)):
                page = df[n]
                for name in page.columns.values:
                    c = page[page[name].astype(str).str.contains(r'(?i)total cholesterol ', na=False, regex=True)]
                    d = page[page[name].astype(str).str.contains('HEMOGLOBIN', na=False, regex=True)]
                    value1 = c['VALUE'].values
                    value2 = d['VALUE'].values
                    for i in value1:
                        value_cholesterol.append(i)
                    for i in value2:
                        value_hemoglobin.append(i)
            cholesterol = value_cholesterol[0]
            hemoglobin = value_hemoglobin[0]
            dic = {'cholesterol':cholesterol,'hemoglobin':hemoglobin }
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


def blood_report(request):

    return render(request, 'Blood Profile/Report.html',)

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

