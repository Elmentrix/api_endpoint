from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .serializers import itemsSerializer
from .key import key_log_read
from .models import items


# # sheet data
# data = key_log_read()
# for row in data[1:]:
#         print(str(row(0)))

# # reading from excel file to db
# def home(request):
#     # loop through data
    
        
#     return HttpResponse("key_log_read")

def itemSel(request):
    # tasks
    # 1. get all items from db
    # 2. serialize them
    # 3. return json 

    # getting all items from the db and passing it through serializer
    items_data = items.objects.all()
    serial = itemsSerializer(items_data, many=True)

    return JsonResponse(serial.data, safe=False)
