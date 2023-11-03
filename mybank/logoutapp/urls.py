from . import views
from django.urls import path



urlpatterns = [


     path('logout/',views.logout,name='logout'),


 ]