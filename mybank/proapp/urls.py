from django.urls import path
from . import views, admin

urlpatterns = [
    # Your main view for the form

    path('form/', views.form, name='form'),

    # Endpoint for dynamically loading cities based on selected country
    path('load_branch/', views.load_branch, name='load_branch'),



]
