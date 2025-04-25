from django.db import models

class Door(models.Model):
    shelves = models.IntegerField()
    slots = models.IntegerField()
    cooler = models.ForeignKey("Cooler", on_delete=models.CASCADE)
    type = models.ForeignKey("Type", on_delete=models.CASCADE)

    @property
    def door_quantity(self):
        """Calculates the total quantity of doors by multiplying shelves and slots."""
        return self.shelves * self.slots
