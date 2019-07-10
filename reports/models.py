from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from djgeojson.fields import PointField


estadoreporte = (
	('0','Reportado'),
	('1','En proceso'),
	('2','Resuelto'),
	('3','Descartado'),
)

class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    asunto = models.CharField(max_length=30)
    imagen = models.ImageField(upload_to='reports/')
    descripcion = models.TextField(max_length=200)
    fechacreacion = models.DateField(default=timezone.now)
    estado = models.CharField(max_length=1, choices=estadoreporte, default=estadoreporte[0][0]) 
    geom = PointField()

    def publish(self):
        self.fechacreacion = timezone.now()
        self.save()

    def __str__(self):
        return self.asunto

    @property
    def imagen_url(self):
        return self.imagen.url