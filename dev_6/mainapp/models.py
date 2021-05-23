from django.db import models


class Photo(models.Model):
    name = models.CharField(verbose_name='Название', max_length=64, blank=True)
    image = models.ImageField(verbose_name='Фотография', upload_to='img/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
