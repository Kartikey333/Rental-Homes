from django.shortcuts import render
from rent_home.models import Room,RoomType,House

def room_index(request, id = 0):

    room_types = RoomType.objects.all()
    rooms = None
    if id == 0:
        rooms = Room.objects.all().order_by('-available') 
    else:
        # l = args
        # print(type(args))
        # print(args)
        rooms = Room.objects.filter(room_type = id)


    context = {
        "rooms" : rooms,
        "room_types" : room_types,
    }

    # print(room_types)
    # for room in room_types:
    #     print(room.id)
    return render(request,"rent_home/room_index.html",context)

def house_index(request, id):
    house = House.objects.get(id = id)

    context = {
        "house" : house,
    }
    return render(request,"rent_home/house_index.html",context)


    

