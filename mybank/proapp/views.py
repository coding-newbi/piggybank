from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from proapp.forms import CustomerForm
from proapp.models import DETAILS

from proapp.models import District, Branch


# Create your views here.

def form(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            # Process the form data here
             NAME= form.cleaned_data['NAME']
             AGE= form.cleaned_data['AGE']
             DATE_OF_BIRTH = form.cleaned_data['DATE_OF_BIRTH']
             GENDER = form.cleaned_data['GENDER']
             MAIL_ID = form.cleaned_data['MAIL_ID']
             PHONE_NUMBER = form.cleaned_data['PHONE_NUMBER']
             ADDRESS= form.cleaned_data['ADDRESS']
             selected_district = form.cleaned_data['district']
             selected_branch = form.cleaned_data['branch']
             ACCOUNT_TYPE= form.cleaned_data['ACCOUNT_TYPE']
             MATERIALS_PROVIDED = form.cleaned_data['MATERIALS_PROVIDED']
            # Extract selected country and city from the form data



             cus=DETAILS(NAME=NAME,DATE_OF_BIRTH=DATE_OF_BIRTH,AGE=AGE,GENDER=GENDER,MAIL_ID=MAIL_ID,PHONE_NUMBER=PHONE_NUMBER,ADDRESS=ADDRESS,district=selected_district,branch=selected_branch,ACCOUNT_TYPE=ACCOUNT_TYPE,MATERIALS_PROVIDED=MATERIALS_PROVIDED,)

             cus.save()




        return render(request,'message.html')
    else:
        form = CustomerForm()

    return render(request,'form.html', {'form': form})


def load_branch(request):
    district_id = request.GET.get('district_id')
    print(f"Received district_id : {district_id}")  # Check if it's correct

    # Import models and check if they're available

    print(f"Branch model: {Branch}")
    print(f"District model: {District}")

    branches = Branch.objects.filter(district_id=district_id)

    print(f"Query result: {branches}")  # Check what cities are retrieved
    branch_list = [{'id': branch.id, 'name': branch.name} for branch in branches]
    return JsonResponse({'branches': branch_list})



