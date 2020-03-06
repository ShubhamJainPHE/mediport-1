from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('diabriskpred/', views.diabriskpred, name='diabriskpred'),
    path('diabetes_result/', views.diabetes_report, name='diabetes_report'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
