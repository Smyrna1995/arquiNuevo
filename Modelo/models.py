from django.db import models
from django.utils import timezone

class Registro(models.Model):
    name_registro = models.CharField(max_length=254, null=False)
    delete_registro = models.BooleanField(default=False)
    create_registro = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'Registro'

class Alumno(models.Model):
    rfid_alumno = models.OneToOneField(Registro, null=True, blank=True, on_delete=models.CASCADE)
    name_alumno = models.CharField(max_length=254, null=False)
    matricula_alumno = models.IntegerField(null=False)
    motherslast_alumno = models.CharField(max_length=254, null=False)
    fatherslast_alumno = models.CharField(max_length=254, null=False)
    delete_alumno = models.BooleanField(default=False)
    create_alumno = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'Alumno'