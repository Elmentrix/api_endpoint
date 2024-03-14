from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .serializers import itemsSerializer
from rest_framework.decorators import api_view
from . import key
from .models import items
from rest_framework.response import Response
from rest_framework import status 

# reading from spreasheet file to db
@api_view(['POST'])
def sheet_data_read():
    # loop through data
    data = key.key_log_read()
    for row in data[1:]:
            itm = row[0]
            des = row[1]
            img = row[2]

            new_data = items.objects.create(title=itm, description=des, image=img) # mapping each row to the columns in the db
            new_data.save() # saving data to db
            # return HttpResponse("it was a success")

# sheet_data_read() # sheet read function

# db to json - read
@api_view(['GET', 'POST'])
def itemSel(request):
    if request.method == 'GET':
        items_data = items.objects.all() # getting data
        serial = itemsSerializer(items_data, many=True) # serializing the data
        return Response(serial.data) # returning serialized data as json

    if request.method == 'POST':
        serial = itemsSerializer(data=request.data)

        # check if the data is valid
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)

# CRUD
# delete, update/edit
@api_view(['GET', 'PUT', 'DELETE'])
def del_up_det(request, id):
    try:
        itm = items.objects.get(pk=id)
    except items.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # conditional check
    if request.method == 'GET': # performing a get request
        serializer = itemsSerializer(itm)
        return Response(serializer.data)
   
    elif request.method == 'PUT': # performing a put request for updating
        serializer = itemsSerializer(itm, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE': # performing delete
        itm.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)