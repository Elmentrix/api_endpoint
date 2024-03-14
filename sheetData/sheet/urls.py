from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('items/',  views.itemSel),
    path('sheet_read/',  views.sheet_data_read, name = "reader"),
    path('sheet_read/<int:id>',  views.del_up_det, name = "del_up_det")
]
