from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse


def index(request):
    return render(request, 'ADTAA/index.html')


def reg_page(request):
    return render(request, 'ADTAA/reg.html')

def root_home_page(request):
    return render(request, 'ADTAA/rootHome.html')

def admin_home_page(request):
    return render(request, 'ADTAA/adminHome.html')

def scheduler_home_page(request):
    return render(request, 'ADTAA/schedulerHome.html')

def password_page(request):
    return render(request, 'ADTAA/password.html')

def setup_instructor(request):
    return render(request, 'ADTAA/instrSetup.html')

def setup_classes(request):
    return render(request, 'ADTAA/classSetup.html')