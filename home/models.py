from django.db import models
from django.utils import timezone
import uuid


# Create your models here.
def generar_id_aleatorio():
       return uuid.uuid4().hex[:16]

# Creamos un modelo abstracto para campos comunes
class BaseModel(models.Model):
    activate_date = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=False)



    class Meta:
        abstract = True
# Creamos un modelo para representar las centrales domóticas
class Domotic_central(BaseModel):
    name_domotic_central = models.CharField(max_length=20, unique=True, verbose_name="Nombre de la central domótica")
    detail_domotic_central = models.CharField(max_length=100, default=False, verbose_name="Detalle de la central domótica")
    interface_domotic_central = models.CharField(max_length=50, verbose_name="Interfaz de la central domótica")

    def __str__(self):
        return self.name_domotic_central


class Sensor(BaseModel):
    name_sensor = models.CharField(max_length=100, verbose_name="Nombre del sensor")
    type_sensor = models.CharField(max_length=50, verbose_name="Tipo de sensor")
    value_sensor = models.FloatField(blank=True, default=0, verbose_name="Valor del sensor")
    ubication_sensor = models.ForeignKey(Domotic_central, on_delete=models.CASCADE, to_field='name_domotic_central', verbose_name="Ubicación del sensor")
    random_id = models.CharField(max_length=16, default=generar_id_aleatorio, verbose_name="Id aleatorio")
    def __str__(self):
        # retorno el nombre del sensor
        return self.name_sensor

class Actuator(BaseModel):
    name_actuator = models.CharField(max_length=50, verbose_name="Nombre del actuador")
    type_actuator = models.CharField(max_length=50, verbose_name="Tipo de actuador")
    value_actuator = models.BooleanField(default=False, verbose_name="Valor del actuador")
    ubication_actuator = models.ForeignKey(Domotic_central, on_delete=models.CASCADE, to_field='name_domotic_central', default='', verbose_name="Ubicación del actuador")
    random_id = models.CharField(max_length=16, default=generar_id_aleatorio, verbose_name="Id aleatorio")
    def __str__(self):
        # retorno el nombre del actuador
        return self.name_actuator

class Controller(BaseModel):
    name_controller = models.CharField(max_length=50, verbose_name="Nombre del controlador")
    logical_controller = models.CharField(max_length=50, verbose_name="Lógica del controlador")
    ubication_controller = models.ForeignKey(Domotic_central, on_delete=models.CASCADE, to_field='name_domotic_central', default='', verbose_name="Ubicación del controlador")
    random_id = models.CharField(max_length=16, default=generar_id_aleatorio, verbose_name="Id aleatorio")
    def __str__(self):
        # retorno el nombre del controlador
        return self.name_controller

class Transmission_medium(BaseModel):
    name_transmission_medium = models.CharField(max_length=30, verbose_name="Nombre del medio de transmisión")
    type_transmission_medium = models.CharField(max_length=50, verbose_name="Tipo del medio de transmisión")

    def __str__(self):
        # retorno el nombre del medio
        return self.name_transmission_medium
    

class SensorActuator(BaseModel):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='name_actuator', verbose_name="Sensor")
    actuator = models.ForeignKey(Actuator, on_delete=models.CASCADE, related_name='name_sensor', verbose_name="Actuador")
    condition = models.CharField(max_length=50, verbose_name="Condición")

    # Definimos la clave primaria compuesta por los dos campos anteriores
    class Meta:
        unique_together = (('sensor', 'actuator'),)


class ControllerSensor(BaseModel):
    controller = models.ForeignKey(Controller, on_delete=models.CASCADE, related_name='name_sensor', verbose_name="Controlador")
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='name_controller', verbose_name="Sensor")

    class Meta:
        unique_together = (('controller', 'sensor'),)


class ControllerActuator(BaseModel):
    controller = models.ForeignKey(Controller, on_delete=models.CASCADE, related_name='name_actuator', verbose_name="Controlador")
    actuator = models.ForeignKey(Actuator, on_delete=models.CASCADE, related_name='name_controller', verbose_name="Actuador")

    class Meta:
        unique_together = (('controller', 'actuator'),)

class MediumController(BaseModel):
    medium = models.ForeignKey(Transmission_medium, on_delete=models.CASCADE)
    controller = models.ForeignKey(Controller, on_delete=models.CASCADE, related_name='controller')

    # Definimos la clave primaria compuesta por los dos campos anteriores
class Meta:
  unique_together = (('medium', 'controller'),)

class CentralController(BaseModel):
  central = models.ForeignKey(Domotic_central, on_delete=models.CASCADE)
  controller = models.ForeignKey(Controller, on_delete=models.CASCADE)

    # Definimos la clave primaria compuesta por los dos campos anteriores
class Meta:
  unique_together = (('central', 'controller'),)