from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('diabriskpred/', views.diabriskpred, name='diabriskpred'),
    path('bloodprofile/', views.bloodprofile, name='bloodprofile'),
    path('diabetes_result/', views.diabetes_report, name='diabetes_report'),
    path('blood_result/', views.blood_report, name='blood_report'),
    path('coronavirus/', views.coronavirus, name='coronavirus'),
    path('coronavirus/covid19_risk_result/', views.coronavirus_result, name='coronavirus_result'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
