from django.shortcuts import render
from django.http import HttpResponse
from ..api import key

# Create your views here.
def home(request):
    return HttpResponse("Hello")

print(key.key_log_read())
