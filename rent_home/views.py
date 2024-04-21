from django.shortcuts import render
from rent_home.models import Room, RoomType, House, Property_Type, Budget_Range, Area
from .filters import RoomFilter

def room_index(request):

    f = RoomFilter(request.GET, queryset=Room.objects.all())

    context = {
        "rooms":f,
    }

    return render(request,"rent_home/room_index.html",context)

def house_index(request, id):
    house = House.objects.get(id = id)
    property_types = Property_Type.objects.all()

    context = {
        "house" : house,
        "property_types" : property_types,
    }
    return render(request,"rent_home/house_index.html",context)

def room_details(request):

    return render(request,"rent_home/room_details.html")