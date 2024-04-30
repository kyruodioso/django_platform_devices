# Generated by Django 4.1.12 on 2024-02-02 19:22

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Controller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activate_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_active', models.BooleanField(default=False)),
                ('name_controller', models.CharField(max_length=50, verbose_name='Nombre del controlador')),
                ('logical_controller', models.CharField(max_length=50, verbose_name='Lógica del controlador')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Domotic_central',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activate_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_active', models.BooleanField(default=False)),
                ('name_domotic_central', models.CharField(max_length=20, unique=True, verbose_name='Nombre de la central domótica')),
                ('detail_domotic_central', models.CharField(default=False, max_length=100, verbose_name='Detalle de la central domótica')),
                ('interface_domotic_central', models.CharField(max_length=50, verbose_name='Interfaz de la central domótica')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activate_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_active', models.BooleanField(default=False)),
                ('name_sensor', models.CharField(max_length=100, verbose_name='Nombre del sensor')),
                ('type_sensor', models.CharField(max_length=50, verbose_name='Tipo de sensor')),
                ('value_sensor', models.FloatField(blank=True, default=0, verbose_name='Valor del sensor')),
                ('ubication_sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.domotic_central', to_field='name_domotic_central', verbose_name='Ubicación del sensor')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Transmission_medium',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_transmission_medium', models.CharField(max_length=30, verbose_name='Nombre del medio de transmisión')),
                ('type_transmission_medium', models.CharField(max_length=50, verbose_name='Tipo del medio de transmisión')),
            ],
        ),
        migrations.CreateModel(
            name='MediumController',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('controller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='controller', to='home.controller')),
                ('medium', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.transmission_medium')),
            ],
        ),
        migrations.AddField(
            model_name='controller',
            name='ubication_controller',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='home.domotic_central', to_field='name_domotic_central', verbose_name='Ubicación del controlador'),
        ),
        migrations.CreateModel(
            name='CentralController',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('central', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.domotic_central')),
                ('controller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.controller')),
            ],
        ),
        migrations.CreateModel(
            name='Actuator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activate_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_active', models.BooleanField(default=False)),
                ('name_actuator', models.CharField(max_length=50, verbose_name='Nombre del actuador')),
                ('type_actuator', models.CharField(max_length=50, verbose_name='Tipo de actuador')),
                ('value_actuator', models.BooleanField(default=False, verbose_name='Valor del actuador')),
                ('ubication_actuator', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='home.domotic_central', to_field='name_domotic_central', verbose_name='Ubicación del actuador')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SensorActuator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition', models.CharField(max_length=50, verbose_name='Condición')),
                ('actuator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='name_sensor', to='home.actuator', verbose_name='Actuador')),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='name_actuator', to='home.sensor', verbose_name='Sensor')),
            ],
            options={
                'unique_together': {('sensor', 'actuator')},
            },
        ),
        migrations.CreateModel(
            name='ControllerSensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('controller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='name_sensor', to='home.controller', verbose_name='Controlador')),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='name_controller', to='home.sensor', verbose_name='Sensor')),
            ],
            options={
                'unique_together': {('controller', 'sensor')},
            },
        ),
        migrations.CreateModel(
            name='ControllerActuator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actuator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='name_controller', to='home.actuator', verbose_name='Actuador')),
                ('controller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='name_actuator', to='home.controller', verbose_name='Controlador')),
            ],
            options={
                'unique_together': {('controller', 'actuator')},
            },
        ),
    ]