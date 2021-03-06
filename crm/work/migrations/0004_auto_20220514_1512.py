# Generated by Django 3.2.8 on 2022-05-14 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0003_auto_20220514_0839'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_tg',
            name='coll_center',
            field=models.TextField(default=0, verbose_name='coll center'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user_tg',
            name='field_activiti',
            field=models.TextField(default=0, verbose_name='activiti'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user_tg',
            name='industri',
            field=models.TextField(default=0, verbose_name='industri'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user_tg',
            name='interes',
            field=models.TextField(default=0, verbose_name='interes'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user_tg',
            name='marketplace',
            field=models.TextField(default=0, verbose_name='marketplace'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user_tg',
            name='mpy',
            field=models.TextField(default=0, verbose_name='money per year'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user_tg',
            name='otdel_prod',
            field=models.TextField(default=0, verbose_name='status'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user_tg',
            name='production',
            field=models.TextField(default=0, verbose_name='production'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user_tg',
            name='staf_count',
            field=models.TextField(default=0, verbose_name='staf count'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user_tg',
            name='status',
            field=models.TextField(default=0, verbose_name='status'),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name='user_tg',
            table='work_users',
        ),
    ]
