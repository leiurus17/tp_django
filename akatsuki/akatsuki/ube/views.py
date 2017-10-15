from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def hello(request):
    text = """<h1>Welcome to my Ube app!</h1>"""
    return HttpResponse(text)