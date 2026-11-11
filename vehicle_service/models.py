from django.db import models
from django.db import models

# Create your models here.

class VehicleDb(models.Model):
    owner_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    vehicle_number = models.CharField(max_length=20, unique=True)
    vehicle_name = models.CharField(max_length=100)
    vehicle_type = models.CharField(max_length=50)

    def __str__(self):
        return self.vehicle_number


class ServiceBookingDb(models.Model):
    vehicle = models.ForeignKey(VehicleDb, on_delete=models.CASCADE, related_name="service_bookings")
    service_type = models.CharField(max_length=100)
    booking_date = models.DateField()
    problem = models.TextField()
    service_charge = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=30, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.service_type

