from django.contrib import admin
from .models import DETAILS
from .forms import CustomerForm  # Import your CustomerForm here
from django import forms
from .models import District, Branch  # Import the Country and City models

class CustomerAdmin(admin.ModelAdmin):
    form = CustomerForm  # Use your custom form for the admin interface
    list_display = ['NAME', 'AGE',  'DATE_OF_BIRTH','GENDER', 'MAIL_ID', 'PHONE_NUMBER', 'ADDRESS','district', 'branch','ACCOUNT_TYPE','MATERIALS_PROVIDED']

    # Customize the display of the country and city fields
    def district_name(self, obj):
        return obj.district.name if obj.district else ""

    def branch_name(self, obj):
        return obj.branch.name if obj.branch else ""

    district_name.short_description = 'District'
    branch_name.short_description = 'Branch'

admin.site.register(DETAILS, CustomerAdmin)

class DistrictAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(District, DistrictAdmin)

class BranchAdmin(admin.ModelAdmin):
    list_display = ['name', 'district']

admin.site.register(Branch, BranchAdmin)



