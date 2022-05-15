from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from baseapp.models import Contact
from django.contrib import messages


# copied from urls.py of demoapp
def home(request):
    return render(request,'baseapp/home.html')

def about(request):
    return render(request,'baseapp/about.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request,"Thanks, form has been submitted succesfully!!")

    return render(request,'baseapp/contact.html')

def explore(request):
    return render(request,'baseapp/explore.html')