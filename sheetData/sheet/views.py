from django.shortcuts import render
from django.http import HttpResponse
from .key import key_log_read

# Create your views here.
def home(request):
    return HttpResponse(key_log_read)

print(key_log_read())
