# Generated by Django 3.2.8 on 2022-05-07 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='channel_manage',
            field=models.BooleanField(null=True, verbose_name='manage channel'),
        ),
        migrations.AlterField(
            model_name='user',
            name='chat_manage',
            field=models.BooleanField(null=True, verbose_name='manage chat'),
        ),
        migrations.AlterField(
            model_name='user',
            name='manage',
            field=models.BooleanField(null=True, verbose_name='manage personel'),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.TextField(null=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.TextField(null=True, verbose_name='phone'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_manage',
            field=models.BooleanField(null=True, verbose_name='manage user'),
        ),
    ]