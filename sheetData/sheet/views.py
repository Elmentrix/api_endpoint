from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .serializers import itemsSerializer
from . import key
from .models import items

# reading from spreasheet file to db
def sheet_data_read():
    # loop through data
    data = key.key_log_read()
    for row in data[1:]:
            itm = row[0]
            des = row[1]
            img = row[2]

            new_data = items.objects.create(title=itm, description=des, image=img) # mapping each row to the columns in the db
            new_data.save() # saving data to db   

# db to json
def itemSel(request):
    # calling the above class here
    sheet_data_read()

    # tasks
    # 1. get all items from db
    # 2. serialize them
    # 3. return json 

    items_data = items.objects.all() # getting data
    serial = itemsSerializer(items_data, many=True) # serializing

    return JsonResponse(serial.data, safe=False)
