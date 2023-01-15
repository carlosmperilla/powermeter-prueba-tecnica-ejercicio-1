from statistics import mean

from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Medidor(models.Model):
    llave = models.CharField(blank=False, null=False, max_length=30, verbose_name="Llave identificadora")
    nombre = models.CharField(blank=False, null=False, max_length=150, verbose_name="Nombre")
    alta = models.BooleanField(default=True, null=False, verbose_name="¿Esta de alta?")
    max_consumo = models.DecimalField(default=0.0, null=False, max_digits=15, decimal_places=7, validators=[MinValueValidator(0.0)])
    min_consumo = models.DecimalField(default=0.0, null=False, max_digits=15, decimal_places=7, validators=[MinValueValidator(0.0)])
    total_consumo = models.DecimalField(default=0.0, null=False, max_digits=15, decimal_places=7, validators=[MinValueValidator(0.0)])
    media_consumo = models.DecimalField(default=0.0, null=False, max_digits=15, decimal_places=7, validators=[MinValueValidator(0.0)])

    class Meta:
        verbose_name = "Medidor"
        verbose_name_plural = "Medidores"
        ordering = ['nombre', 'llave']

    def __str__(self):
        return self.nombre + ' - ' + self.llave

    def __init__(self, *args, **kwargs) -> None:
        super(Medidor, self).__init__(*args, **kwargs)
        self.consumos = [0]

    def actualizar_max_consumo(self, consumos_personalizados=None):
        if consumos_personalizados:
            self.max_consumo = max(consumos_personalizados)
        else:
            self.max_consumo = max(self.consumos)

    def actualizar_min_consumo(self, consumos_personalizados=None):
        if consumos_personalizados:
            self.min_consumo = min(consumos_personalizados)
        else:
            self.min_consumo = min(self.consumos)

    def actualizar_total_consumo(self, consumos_personalizados=None):
        if consumos_personalizados:
            self.total_consumo = sum(consumos_personalizados)
        else:
            self.total_consumo = sum(self.consumos)
    
    def actualizar_media_consumo(self, consumos_personalizados=None):
        if consumos_personalizados:
            self.media_consumo = mean(consumos_personalizados)
        else:
            self.media_consumo = mean(self.consumos)

    def actualizar_data(self):
        self.consumos = self.mediciones.values_list('consumo', flat=True)
        self.actualizar_max_consumo()
        self.actualizar_min_consumo()
        self.actualizar_total_consumo()
        self.actualizar_media_consumo()


class Medicion(models.Model):
    fecha_y_hora =  models.DateTimeField(null=False, verbose_name="Fecha y hora")
    consumo = models.DecimalField(null=False, max_digits=15, decimal_places=7, validators=[MinValueValidator(0.0)], verbose_name="Consumo (kwh)")
    medidor = models.ForeignKey(Medidor, editable=True, verbose_name='Medidor', related_name="mediciones",  on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Medicion"
        verbose_name_plural = "Mediciones"
        ordering = ['medidor__nombre', 'fecha_y_hora']

    def __str__(self):
        return str(self.pk) + ' - ' + self.medidor.nombre + ' - ' + self.medidor.llave