from django.db import models

class District(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Branch(models.Model):
    name = models.CharField(max_length=50)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# Create your models here.
class DETAILS(models.Model):
        gender_choices=(('o','------'),('m','Male'),('f','Female'))
        account_choices=(('n','------'),('s','savings Account'),('c','current Account'))
        materials_choices=(('Nn','None'),('d','debit Card'),('cr','credit Card'),('ch','cheque Book'))
        NAME=models.CharField(max_length=25,blank=False)
        AGE=models.IntegerField(null=True,blank=False)
        DATE_OF_BIRTH=models.DateField()
        GENDER=models.CharField(max_length=1,choices=gender_choices,default='o')
        MAIL_ID = models.EmailField(blank=True,null=True)
        PHONE_NUMBER = models.CharField(max_length=15, blank=True, null=True)
        ADDRESS = models.TextField(default='',null=True)
        district = models.ForeignKey(District, on_delete=models.CASCADE, null=True, blank=True)
        branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True, blank=True)
        ACCOUNT_TYPE=models.CharField(max_length=1,choices=account_choices,default='n')
        MATERIALS_PROVIDED=models.CharField(max_length=2,choices=materials_choices,default='Nn')


        def __str__(self):
            return self.NAME

