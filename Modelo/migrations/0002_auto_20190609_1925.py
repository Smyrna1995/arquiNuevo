# Generated by Django 2.2.1 on 2019-06-10 00:25

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Modelo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='registro',
            table='Registro',
        ),
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_alumno', models.CharField(max_length=254)),
                ('matricula_alumno', models.IntegerField()),
                ('motherslast_alumno', models.CharField(max_length=254)),
                ('fatherslast_alumno', models.CharField(max_length=254)),
                ('delete_alumno', models.BooleanField(default=False)),
                ('create_alumno', models.DateTimeField(default=django.utils.timezone.now)),
                ('rfid_alumno', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Modelo.Registro')),
            ],
            options={
                'db_table': 'Alumno',
            },
        ),
    ]
