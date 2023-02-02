from django.conf import settings
from django.db import models


class Boat(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    model = models.CharField(max_length=100, verbose_name='Модель лодки')
    description = models.TextField(verbose_name='Описание')

    length = models.PositiveSmallIntegerField(default=0,
                                              verbose_name='Длина в футах')
    year = models.PositiveSmallIntegerField(default=0,
                                            verbose_name='Год производства')
    price = models.DecimalField(max_digits=15, decimal_places=2, default=0,
                                verbose_name='Цена в рублях')

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.model}'

    class Meta:
        verbose_name = 'лодка'
        verbose_name_plural = 'лодки'

    def delete(self, *args, **kwargs):
        self.is_active = False
        self.save()


class OldOwner(models.Model):
    boat = models.ForeignKey(Boat, on_delete=models.CASCADE)
    start_year = models.PositiveSmallIntegerField(default=0,
                                                  verbose_name='Год начала владения')
    end_year = models.PositiveSmallIntegerField(default=0,
                                                verbose_name='Год окончания владения')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.boat} {self.start_year} - {self.end_year if self.end_year != 0 else "до сих пор"}'

    class Meta:
        verbose_name = 'старый дряхлый владелец'
        verbose_name_plural = 'старые дряхлые владельцы'
