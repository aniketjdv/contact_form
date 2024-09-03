from django import forms
from api.models import Contact_Enquriy

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact_Enquriy
        fields=['name','email','phone','message']
        widgets={
            'name': forms.TextInput(attrs={'placeholder': 'Enter your name', 'class': 'form-control', 'aria-label': 'Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email', 'class': 'form-control', 'aria-label': 'Email'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Enter your phone number', 'class': 'form-control', 'aria-label': 'Phone'}),
            'message': forms.Textarea(attrs={'placeholder': 'Enter your message', 'class': 'form-control', 'aria-label': 'Message'}),
            }


# class ContactForm(forms.Form):
#     name=forms.CharField(label="Enter your name",max_length=50,help_text="Name")
#     email=forms.CharField(label="Enter your Email",max_length=50)
#     phone=forms.CharField(label="Enter your Phone no",max_length=15)
#     message=forms.Textarea()