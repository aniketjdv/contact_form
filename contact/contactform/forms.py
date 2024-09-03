from django import forms
from api.models import Contact_Enquriy

class ContactForm(forms.Form):
    name=forms.CharField(label="enter your name",max_length=50)
    email=forms.CharField(label="enter your Email",max_length=50)
    phone=forms.CharField(label="Enter your Phone no",max_length=15)
    message=forms.Textarea(label="Enter your query",)
    