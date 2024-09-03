from django import forms
from api.models import Contact_Enquriy

class ContactForm(forms.ModelForm):
    # name=forms.CharField(label="enter your name",max_length=50)
    # email=forms.CharField(label="enter your Email",max_length=50)
    # phone=forms.CharField(label="Enter your Phone no",max_length=15)
    # message=forms.CharField(max_length=200)
    class Meta:
        model=Contact_Enquriy
        fields='__all__'