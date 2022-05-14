from django.db import models


class Channel(models.Model):
    """Модель каналов"""
    name = models.CharField(verbose_name='Название канала', max_length=50)
    link = models.CharField(verbose_name='Ссылка', max_length=100)
    desc = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Канал'
        verbose_name_plural = 'Каналы'


class Chat(models.Model):
    """Модель гильдий"""
    name = models.CharField(verbose_name='Название чата', max_length=50)

    class Meta:
        verbose_name = 'Гильдия'
        verbose_name_plural = 'Гильдии'


class User_tg(models.Model):
    """Пользователь телегарм"""
    phone = models.CharField(verbose_name='phone', max_length=50)
    username = models.CharField(verbose_name='username', max_length=50, null=True)
    name = models.CharField(verbose_name='name', max_length=50, null=True)
    surname = models.CharField(verbose_name='surname', max_length=50, null=True)
    about = models.TextField(verbose_name='description', null=True)
    photo = models.TextField(verbose_name='photo_id', null=True)

    class Meta:
        verbose_name = 'Пользователь тг'
        verbose_name_plural = 'Пользователи тг'
