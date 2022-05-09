from django.db import models


class Channel(models.Model):
    name = models.CharField(verbose_name='Название канала', max_length=50)
    link = models.CharField(verbose_name='Ссылка', max_length=100)
    desc = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Канал'
        verbose_name_plural = 'Каналы'