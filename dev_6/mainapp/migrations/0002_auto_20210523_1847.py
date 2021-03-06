# Generated by Django 2.2 on 2021-05-23 13:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo',
            options={'verbose_name': 'Фотография', 'verbose_name_plural': 'Фотографии'},
        ),
        migrations.RemoveField(
            model_name='photo',
            name='model_img',
        ),
        migrations.AddField(
            model_name='photo',
            name='images',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='img', verbose_name='Фотография'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photo',
            name='name',
            field=models.CharField(blank=True, max_length=64, verbose_name='Название'),
        ),
    ]
