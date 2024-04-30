from django.contrib import admin
from .models import Sensor,Actuator,SensorActuator, Controller, ControllerSensor, ControllerActuator, MediumController, CentralController, Domotic_central,Transmission_medium
from django.contrib.auth.models import Group

admin.site.unregister(Group)
admin.site.register(Sensor)
admin.site.register(Actuator)
admin.site.register(Controller)
admin.site.register(SensorActuator)
admin.site.register(ControllerSensor)
admin.site.register(ControllerActuator)
admin.site.register(MediumController)
admin.site.register(Transmission_medium)
admin.site.register(CentralController)
admin.site.register(Domotic_central)
