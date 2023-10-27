
from django import forms

class MyForm(forms.Form):
     name=forms.CharField(label='Name',max_length=100)
     email=forms.EmailField(label='Email')
     coursename=forms.CharField(label='course name',max_length=100)
     joiningdate=forms.CharField(label='joining date')
