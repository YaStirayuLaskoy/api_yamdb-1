# Generated by Django 3.2 on 2023-06-05 10:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='score',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1, 'Рейтинг не может быть меньше 1!'), django.core.validators.MaxValueValidator(10, 'Рейтинг не может быть больше 10!')], verbose_name='Оценка произведения'),
        ),
    ]