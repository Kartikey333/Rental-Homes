from django.db import models

class RoomType(models.Model):

    room_type_name = models.CharField(max_length=50,default="Single Room")
    
    def __str__(self):
        return self.room_type_name

class House(models.Model):

    house_no = models.CharField(max_length=10, null=True)
    house_name = models.CharField(max_length=20, null=True)
    owner_name = models.CharField(max_length=30)
    contact_no = models.IntegerField()
    address = models.TextField()
    area_belong = models.TextField()
    # room_types = models.ManyToManyField("Type", related_name="houses")

    def __str__(self):
        return self.house_no

class Room(models.Model):

    house = models.ForeignKey('House',on_delete=models.CASCADE)
    room_type = models.ForeignKey('RoomType', on_delete=models.CASCADE)
    bhk = models.IntegerField(null=True)
    available = models.BooleanField(default=False)
    balcony = models.BooleanField()
    lat_bath = models.TextField(max_length=20)
    rent = models.DecimalField(max_digits=10, decimal_places=2)
    electricity = models.TextField(max_length=15)

    def __str__(self):
        return f"{self.room_type} in {self.house}"
