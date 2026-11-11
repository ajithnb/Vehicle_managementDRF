from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from vehicle_service.models import VehicleDb, ServiceBookingDb
from vehicle_service.serializer import VehicleSerializer, ServiceBookingSerializer

# Create your views here.


class VehicleListCreateView(APIView):

    def get(self, request):
        qs = VehicleDb.objects.all()
        serializer_instance = VehicleSerializer(qs, many=True)
        return Response(data=serializer_instance.data)

    def post(self, request):
        form_data = request.data
        serializer_instance = VehicleSerializer(data=form_data)

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data, status=201)
        else:
            return Response(data=serializer_instance.errors, status=400)


class VehicleRetrieveUpdateDeleteView(APIView):

    def get(self, request, pk):
        qs = get_object_or_404(VehicleDb, id=pk)
        serializer_instance = VehicleSerializer(qs)
        return Response(data=serializer_instance.data)

    def put(self, request, pk):
        vehicle_object = get_object_or_404(VehicleDb, id=pk)
        serializer_instance = VehicleSerializer(instance=vehicle_object, data=request.data)

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors, status=400)

    def delete(self, request, pk):
        vehicle_object = get_object_or_404(VehicleDb, id=pk)
        vehicle_object.delete()
        return Response(data={"message": "Vehicle deleted successfully"})


class ServiceBookingListCreateView(APIView):

    def get(self, request):
        qs = ServiceBookingDb.objects.all()
        serializer_instance = ServiceBookingSerializer(qs, many=True)
        return Response(data=serializer_instance.data)

    def post(self, request):
        form_data = request.data
        serializer_instance = ServiceBookingSerializer(data=form_data)

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data, status=201)
        else:
            return Response(data=serializer_instance.errors, status=400)


class ServiceBookingRetrieveUpdateDeleteView(APIView):

    def get(self, request, pk):
        qs = get_object_or_404(ServiceBookingDb, id=pk)
        serializer_instance = ServiceBookingSerializer(qs)
        return Response(data=serializer_instance.data)

    def put(self, request, pk):
        booking_object = get_object_or_404(ServiceBookingDb, id=pk)
        serializer_instance = ServiceBookingSerializer(instance=booking_object, data=request.data)

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors, status=400)

    def delete(self, request, pk):
        booking_object = get_object_or_404(ServiceBookingDb, id=pk)
        booking_object.delete()
        return Response(data={"message": "Booking deleted successfully"})
