from django.urls import path

from HospitalApp import views

urlpatterns = [
   path('adbk', views.addbooking, name='ab2'),
   path('nwpg', views.newpg, name='np')

]