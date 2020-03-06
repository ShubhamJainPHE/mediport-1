from django.shortcuts import render
from django.shortcuts import render_to_response
from .forms import *
from django.http import HttpResponseRedirect
# from django.core.mail import send_mail
from django.contrib import messages
import request
from django.shortcuts import get_object_or_404

# Create your views here.


def home(request):
    return render(request, 'home/home.html', {'':''})

def diabetes_report(request):

    return render(request, 'Diabetes/Report.html',)

def diabriskpred(request):

    if request.method == 'POST':
        form = Diabetes(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            gender = form.cleaned_data['gender']
            age = form.cleaned_data['age']
            total_cholestrol = form.cleaned_data['total_cholestrol']
            hdl_cholestrol = form.cleaned_data['hdl_cholestrol']
            weight =  form.cleaned_data['weight']
            height =  form.cleaned_data['height']
            waist =  form.cleaned_data['waist']
            hip =  form.cleaned_data['hip']
            physically_active =  form.cleaned_data['physically_active']
            eat = form.cleaned_data['eat']
            bp = form.cleaned_data['bp']
            relative_diabetes = form.cleaned_data['relative_diabetes']
            parent_diabetes = form.cleaned_data['parent_diabetes']
            glucose = form.cleaned_data['glucose']
            smoking = form.cleaned_data['smoking']
            heart_disease = form.cleaned_data['heart_disease']
            depression = form.cleaned_data['depression']
            HbA1c = form.cleaned_data['HbA1c']
            haem = form.cleaned_data['haem']
            context = diabetes.objects.create(name =name,
                                              gender=gender,
                                              age=age,
                                              total_cholestrol=total_cholestrol,
                                              hdl_cholestrol=hdl_cholestrol,
                                              weight=weight,
                                              height=height,
                                              waist=waist,
                                              hip=hip,
                                              physically_active=physically_active,
                                              eat=eat,
                                              bp=bp,
                                              relative_diabetes=relative_diabetes,
                                              parent_diabetes=parent_diabetes,
                                              glucose=glucose,
                                              smoking=smoking,
                                              heart_disease=heart_disease,
                                              depression=depression,
                                              HbA1c=HbA1c,
                                              haem=haem)

            context.save()
            g = (weight*10000) / (height * height)
            bmi_calc = float("{0:.2f}".format(g))
            bmi_chart = (bmi_calc/24.9)*10
            print(bmi_chart)
            # while gender == 'Male':
            #     if total_cholestrol > 30 & total_cholestrol <65:
            #         cholestrol_chart =

            dic = {'name':name,'age':age, 'gender':gender, 'total_cholestrol':total_cholestrol,'hdl_cholestrol':hdl_cholestrol,
                   'weight':weight,'height':height,'waist':waist,'hip':hip,'physically_active':physically_active,'eat':eat,
                   'parent_diabetes':parent_diabetes,'relative_diabetes':relative_diabetes, 'bp':bp, 'glucose':glucose,
                   'smoking':smoking,'heart_disease':heart_disease,'depression':depression,'HbA1c':HbA1c,'haem':haem,
                   'bmi_calc':bmi_calc,'bmi_chart':bmi_chart,
                   }

            return render_to_response('Diabetes/Report.html', dic)
        else:
            form = Diabetes()

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