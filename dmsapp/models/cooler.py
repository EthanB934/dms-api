from django.db import models
from django.apps import apps

class Cooler(models.Model):

    @property
    def total_capacity(self):
        """Calculates the total capacity of the cooler based on its doors."""
        Door = apps.get_model("dmsapp", "Door")
        doors = Door.objects.filter(cooler=self)
        capacity = 0
        for door in doors:
            capacity += door.door_quantity
        return capacity