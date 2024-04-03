# Generated by Django 4.2.10 on 2024-03-10 13:07

import catalogapp.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventsClass',
            fields=[
                ('events_set_id', models.CharField(default=catalogapp.models.initial_events_set_id, editable=False, max_length=50, primary_key=True, serialize=False)),
                ('events_set_name', models.CharField(max_length=50, verbose_name='EventSet')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(verbose_name='Comments')),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
        migrations.CreateModel(
            name='ModelsClass',
            fields=[
                ('models_id', models.AutoField(primary_key=True, serialize=False)),
                ('models_name', models.CharField(max_length=50, verbose_name='Models')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('models_location', models.CharField(max_length=150, verbose_name='Location')),
                ('description', models.TextField(verbose_name='Comments')),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
        migrations.CreateModel(
            name='ObjectType',
            fields=[
                ('object_type_id', models.AutoField(default=catalogapp.models.initial_object_type_id, primary_key=True, serialize=False, unique=True)),
                ('object_type_name', models.CharField(max_length=50, unique=True, verbose_name='ObjectType')),
            ],
            options={
                'ordering': ['-object_type_id'],
            },
        ),
        migrations.CreateModel(
            name='ServersClass',
            fields=[
                ('server_id', models.AutoField(primary_key=True, serialize=False)),
                ('server_name', models.CharField(max_length=50)),
                ('server_url', models.CharField(max_length=250)),
                ('server_status', models.CharField(max_length=50)),
                ('description', models.TextField(verbose_name='Description')),
            ],
            options={
                'ordering': ['-server_id'],
            },
        ),
        migrations.CreateModel(
            name='TrendsClass',
            fields=[
                ('trends_set_id', models.CharField(default=catalogapp.models.initial_trends_set_id, editable=False, max_length=50, primary_key=True, serialize=False)),
                ('trends_set_name', models.CharField(max_length=50, verbose_name='Trends')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(verbose_name='Comments')),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
        migrations.CreateModel(
            name='ScenarioClass',
            fields=[
                ('scenario_id', models.CharField(default=catalogapp.models.initial_scenario_id, editable=False, max_length=50, primary_key=True, serialize=False)),
                ('scenario_name', models.CharField(max_length=50, verbose_name='Scenario')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=50)),
                ('description', models.TextField(verbose_name='Description')),
                ('events_set_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogapp.eventsclass')),
                ('models_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogapp.modelsclass')),
                ('server', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalogapp.serversclass')),
                ('trends_set_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogapp.trendsclass')),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
        migrations.CreateModel(
            name='ObjectTypeProperty',
            fields=[
                ('object_type_property_id', models.AutoField(default=catalogapp.models.initial_object_type_property_id, primary_key=True, serialize=False, unique=True)),
                ('object_type_property_name', models.CharField(max_length=50, unique=True, verbose_name='ObjectTypeProperty')),
                ('object_type_property_category', models.CharField(max_length=50, verbose_name='Cataloge')),
                ('object_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogapp.objecttype')),
            ],
            options={
                'ordering': ['-object_type_property_id'],
            },
        ),
        migrations.CreateModel(
            name='ObjectInstance',
            fields=[
                ('object_instance_id', models.AutoField(default=catalogapp.models.initial_object_instance_id, primary_key=True, serialize=False, unique=True)),
                ('object_instance_name', models.CharField(max_length=50, unique=True, verbose_name='ObjectInstance')),
                ('object_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogapp.objecttype')),
            ],
            options={
                'ordering': ['-object_instance_id'],
            },
        ),
        migrations.CreateModel(
            name='MainClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_source_type', models.CharField(choices=[('SC', 'ScenarioClass'), ('EV', 'EventsClass'), ('TR', 'TrendsClass')], max_length=2)),
                ('data_source_id', models.CharField(max_length=50)),
                ('value', models.DecimalField(db_column='value', decimal_places=2, max_digits=10, null=True)),
                ('date_time', models.CharField(db_column='date', max_length=50, verbose_name='Date')),
                ('sub_data_source', models.CharField(max_length=50, null=True, verbose_name='Category')),
                ('object_instance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogapp.objectinstance')),
                ('object_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogapp.objecttype')),
                ('object_type_property', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogapp.objecttypeproperty')),
            ],
            options={
                'ordering': ['-data_source_id'],
            },
        ),
    ]
