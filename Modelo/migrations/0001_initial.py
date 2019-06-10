# Generated by Django 2.2.1 on 2019-06-09 23:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_registro', models.CharField(max_length=254)),
                ('delete_registro', models.BooleanField(default=False)),
                ('create_registro', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
