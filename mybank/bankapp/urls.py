from django.urls import path

from bankapp import views

urlpatterns = [

    path('',views.home,name='home'),




]