from django.urls import path, include
from rest_framework import routers
from home import views


router = routers.DefaultRouter()

router.register(r'domotic-centrals',views.DomoticCentralViewSet)
router.register(r'sensors', views.SensorViewSet)
router.register(r'controllers', views.ControllerViewSet)
router.register(r'actuators', views.ActuatorViewSet)
router.register(r'sensor-actuators', views.SensorActuatorViewSet)
router.register(r'controller-sensors', views.ControllerSensorViewSet)
router.register(r'controller-actuators', views.ControllerActuatorViewSet)
router.register(r'medium-controllers', views.MediumControllerViewSet)
router.register(r'central-controllers', views.CentralControllerViewSet)
router.register(r'transmission-medium', views.TransmissionMediumViewSet)

urlpatterns = [
    path('', views.index, name='index'),
        path('', include(router.urls)),

]
