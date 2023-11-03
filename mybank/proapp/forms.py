from django import forms
from proapp.models import DETAILS, District, Branch

class CustomerForm(forms.ModelForm):
    district = forms.ModelChoiceField(
        queryset=District.objects.all(),
        empty_label="Select District",
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    branch = forms.ModelChoiceField(
        queryset=Branch.objects.all(),
        empty_label="Select Branch ",
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = DETAILS
        fields = ['NAME', 'AGE', 'DATE_OF_BIRTH', 'GENDER', 'MAIL_ID', 'PHONE_NUMBER', 'ADDRESS','district', 'branch', 'ACCOUNT_TYPE', 'MATERIALS_PROVIDED']
        widgets = {
            'NAME': forms.TextInput(attrs={'placeholder': 'enter your name', 'type': 'text'}),
            'AGE': forms.NumberInput(attrs={'placeholder': 'enter your age'}),
            'DATE_OF_BIRTH': forms.DateInput(attrs={'type': 'date'}),
            'GENDER': forms.Select(choices=DETAILS.gender_choices, attrs={'class': 'form-select'}),
            'MAIL_ID': forms.EmailInput(attrs={'placeholder': 'enter your e-mail'}),
            'PHONE_NUMBER': forms.TextInput(attrs={'placeholder': 'enter your phone number'}),
            'ADDRESS': forms.Textarea(attrs={'placeholder': 'enter your address'}),
            'ACCOUNT_TYPE': forms.Select(choices=DETAILS.account_choices, attrs={'class': 'form-select'}),
            'MATERIALS_PROVIDED': forms.RadioSelect(choices=DETAILS.materials_choices),
        }
