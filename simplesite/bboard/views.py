from django.shortcuts import render
from django.http import HttpResponse

# Create your views here. ~ Controllers
def index(requests):
  return HttpResponse('Здесь будет список объявлений')