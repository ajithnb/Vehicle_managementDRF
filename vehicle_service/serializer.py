from rest_framework import serializers
from vehicle_service.models import VehicleDb, ServiceBookingDb


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleDb
        fields = "__all__"


class ServiceBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceBookingDb
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
