from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets

from .serializer import ControllerSerializer, Domotic_centralSerializer, SensorSerializer, ActuatorSerializer, SensorActuatorSerializer, ControllerSensorSerializer, ControllerActuatorSerializer, MediumControllerSerializer, CentralControllerSerializer, Transmission_mediumSerializer

from .models import Controller, Domotic_central,Sensor, Actuator, SensorActuator, ControllerSensor, ControllerActuator, MediumController, CentralController, Transmission_medium

# Create your views here.
class ControllerViewSet(viewsets.ModelViewSet):
    queryset= Controller.objects.all()
    serializer_class= ControllerSerializer

class DomoticCentralViewSet(viewsets.ModelViewSet):
    queryset=Domotic_central.objects.all()
    serializer_class=Domotic_centralSerializer
    
class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class ActuatorViewSet(viewsets.ModelViewSet):
    queryset = Actuator.objects.all()
    serializer_class = ActuatorSerializer

class SensorActuatorViewSet(viewsets.ModelViewSet):
    queryset = SensorActuator.objects.all()
    serializer_class = SensorActuatorSerializer

class ControllerSensorViewSet(viewsets.ModelViewSet):
    queryset = ControllerSensor.objects.all()
    serializer_class = ControllerSensorSerializer

class ControllerActuatorViewSet(viewsets.ModelViewSet):
    queryset = ControllerActuator.objects.all()
    serializer_class = ControllerActuatorSerializer

class TransmissionMediumViewSet(viewsets.ModelViewSet):
    queryset = Transmission_medium.objects.all()
    serializer_class = Transmission_mediumSerializer

class MediumControllerViewSet(viewsets.ModelViewSet):
    queryset = MediumController.objects.all()
    serializer_class = MediumControllerSerializer

class CentralControllerViewSet(viewsets.ModelViewSet):
    queryset = CentralController.objects.all()
    serializer_class = CentralControllerSerializer

def index(request):
    title='IOT Platform'

    # Page from the theme 
    return render(request, 'pages/dashboard.html', {
        'title':title,
        'centrals':DomoticCentralViewSet.queryset,
        'controllers':ControllerViewSet.queryset,
        'sensors':SensorViewSet.queryset,
        'actuators':ActuatorViewSet.queryset
    })
