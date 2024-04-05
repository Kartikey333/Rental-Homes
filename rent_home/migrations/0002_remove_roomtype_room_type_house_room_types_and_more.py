# Generated by Django 5.0.3 on 2024-03-17 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rent_home", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="roomtype", name="room_type",),
        migrations.AddField(
            model_name="house",
            name="room_types",
            field=models.ManyToManyField(related_name="houses", to="rent_home.type"),
        ),
        migrations.AlterField(
            model_name="house", name="contact_no", field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="roomtype",
            name="available",
            field=models.BooleanField(default=False),
        ),
    ]
