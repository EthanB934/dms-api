from django.db import models

class CoolerType(models.Model):
    coolers = models.ForeignKey("Cooler", on_delete=models.CASCADE, related_name="Coolers")
    types = models.ForeignKey("Type", on_delete=models.CASCADE, related_name="Types")