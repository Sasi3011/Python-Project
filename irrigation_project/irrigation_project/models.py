from django.db import models

class Plant(models.Model):
    name = models.CharField(max_length=100)
    water_required_lph = models.FloatField()  # Litres per hour

class UserInput(models.Model):
    location = models.CharField(max_length=100)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    irrigation_time = models.DateTimeField(auto_now_add=True)
    water_used = models.FloatField()  # AI-calculated based on plant

class IrrigationLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=100)
    plant_name = models.CharField(max_length=100)
    water_given = models.FloatField()
