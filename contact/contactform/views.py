from django.shortcuts import redirect, render
from .forms import ContactForm
from api.models import Contact_Enquriy
from api.urls import router
import requests
# Create your views here.

def contact_form(request):
    enq=None
    if request.method == 'POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success') 
    else:
        form=ContactForm()
    return render(request,'contact.html',{'form':form})

def success(request):
    if request.method == 'POST':
        return redirect('contact_form')
    return render(request,'success.html')

def query(request):
    response = requests.get('http://127.0.0.1:8000/api/v1/contacts/')
    data = response.json()  # Assuming the API returns JSON data
    return render(request,'queries.html',{'data':data})