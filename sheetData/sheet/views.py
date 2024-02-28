from django.shortcuts import render
from django.http import HttpResponse
from .serializers import itemsSerializer
from .key import key_log_read

# Create your views here.
def home(request):
    return HttpResponse("key_log_read")

def itemSel(request):

    # tasks
    # 1. get all items from db
    # 2. serialize them
    # 3. return json 

    return HttpResponse()
