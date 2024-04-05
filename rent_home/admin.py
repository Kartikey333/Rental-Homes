from django.contrib import admin
from rent_home.models import Room,RoomType,House

admin.site.register(RoomType)
admin.site.register(Room)
admin.site.register(House)
