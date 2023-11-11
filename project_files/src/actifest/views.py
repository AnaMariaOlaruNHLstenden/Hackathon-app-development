from django.http import  HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import *
from django.urls import reverse

def index(request) :
    return render(request,'index.html')
def login(request) :
    return HttpResponse("login page")
def registerPage(request) :
    return HttpResponse("register page")
def profile (request) :
    return HttpResponse("profile page")
