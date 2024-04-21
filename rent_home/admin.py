from django.contrib import admin
from rent_home.models import Room, RoomType, House, Property_Type, Area, Budget_Range

admin.site.register(RoomType)
admin.site.register(Room)
admin.site.register(House)
admin.site.register(Budget_Range)
admin.site.register(Property_Type)
admin.site.register(Area)


