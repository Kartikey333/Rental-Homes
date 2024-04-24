from django.db import models
from django.contrib.auth.models import User

class RoomType(models.Model):

    room_type_name = models.CharField(max_length=50,default="Single Room")
    
    def __str__(self):
        return self.room_type_name

class Property_Type(models.Model):

    property_type_name = models.CharField(max_length=50,default="Non-independent house")
    
    def __str__(self):
        return self.property_type_name

class Area(models.Model):

    area_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.area_name

class Budget_Range(models.Model):

    budget_range = models.CharField(max_length=50)
    
    def __str__(self):
        return self.budget_range


class House(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    house_no = models.CharField(max_length=10, null=True)
    house_name = models.CharField(max_length=20, null=True)
    owner_name = models.CharField(max_length=30)
    contact_no = models.IntegerField()
    address = models.TextField()
    area = models.ForeignKey('Area', on_delete=models.CASCADE, null=True)
    property_type = models.ForeignKey('Property_Type', on_delete=models.CASCADE, null=True)

    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    

    def __str__(self):
        return self.house_no

class Room(models.Model):

    house = models.ForeignKey('House',on_delete=models.CASCADE)
    
    room_type = models.ForeignKey('RoomType',on_delete=models.CASCADE, null=True)

    furnished = models.BooleanField(default=False)

    available = models.BooleanField(default=False)

    balcony = models.BooleanField(default=False)

    lat_bath = models.CharField(max_length=20)                            #change 1

    rent = models.IntegerField()

    budget_range = models.ForeignKey("Budget_Range", on_delete=models.CASCADE, null=True)  #4

    electricity_bill_per_unit = models.IntegerField(null=True,blank=True)       #2

    room_for = models.CharField(max_length=10,default="For Boys")               #3


    deposite_money = models.IntegerField(default=1000)


    def __str__(self):
        return f"{self.room_type} in {self.house}"
