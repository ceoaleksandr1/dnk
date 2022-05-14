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
    # Личные данные
    phone = models.CharField(verbose_name='phone', max_length=50)
    username = models.CharField(verbose_name='username', max_length=50, null=True)
    tg_id = models.TextField(verbose_name='tg_id')
    name = models.CharField(verbose_name='name', max_length=50, null=True)
    surname = models.CharField(verbose_name='surname', max_length=50, null=True)
    photo = models.TextField(verbose_name='photo_id', null=True)

    # О компании
    about = models.TextField(verbose_name='description', null=True)
    status = models.TextField(verbose_name='status')
    mpy = models.TextField(verbose_name='money per year')
    industri = models.TextField(verbose_name='industri')
    staf_count = models.TextField(verbose_name='staf count')
    field_activiti = models.TextField(verbose_name='activiti')

    # Оценка себя как специалиста
    otdel_prod = models.TextField(verbose_name='status')
    coll_center = models.TextField(verbose_name='coll center')
    production = models.TextField(verbose_name='production')
    marketplace = models.TextField(verbose_name='marketplace')

    # Интерес к продукту
    interes = models.TextField(verbose_name='interes')

    class Meta:
        db_table = 'work_users'
        verbose_name = 'Пользователь тг'
        verbose_name_plural = 'Пользователи тг'
