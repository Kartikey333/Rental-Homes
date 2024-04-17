from django.db import models

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

    house_no = models.CharField(max_length=10, null=True)
    house_name = models.CharField(max_length=20, null=True)
    owner_name = models.CharField(max_length=30)
    contact_no = models.IntegerField()
    address = models.TextField()
    area = models.ForeignKey('Area', on_delete=models.CASCADE)
    property_type = models.ForeignKey('Property_Type', on_delete=models.CASCADE)


    def __str__(self):
        return self.house_no

class Room(models.Model):

    house = models.ForeignKey('House',on_delete=models.CASCADE)
    
    bhk = models.ForeignKey('RoomType', on_delete=models.CASCADE)

    furnished = models.BooleanField(default=False)

    available = models.BooleanField(default=False)

    balcony = models.BooleanField(default=False)

    lat_bath = models.TextField(max_length=20)

    budget_range = models.ForeignKey("Budget_Range", on_delete=models.CASCADE)
    rent = models.IntegerField()

    electricity = models.TextField(max_length=15)

    def __str__(self):
        return f"{self.room_type} in {self.house}"
