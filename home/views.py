from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render, redirect
def index(request):

    # Page from the theme 

    return redirect('/home')