from django.db import models
from django.utils import timezone

# Create your models here.
class equip(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=500)
    desc = models.CharField(max_length=500)
    add1 = models.CharField(max_length=200)
    add2 = models.CharField(max_length=200)
    add3 = models.CharField(max_length=200)
    km = models.IntegerField(default=0)
    ano = models.IntegerField()
    data = models.DateTimeField(default=timezone.now)
    valor = models.DecimalField(max_digits=8, decimal_places=2)

    def __int__(self):
        return self.id