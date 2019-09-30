from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

