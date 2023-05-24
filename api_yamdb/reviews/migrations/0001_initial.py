# Generated by Django 3.2 on 2023-05-23 20:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название категории', max_length=256, verbose_name='Название категории')),
                ('slug', models.SlugField(help_text='Создайте идентификатор для категории', unique=True, verbose_name='Идентификатор категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название жанра', max_length=256, verbose_name='Название жанра')),
                ('slug', models.SlugField(help_text='Создайте идентификатор для жанра', unique=True, verbose_name='Идентификатор жанра')),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='GenreTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.genre')),
            ],
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название произведения', max_length=256, verbose_name='Название произведения')),
                ('year', models.IntegerField(help_text='Введите год создания произведения', verbose_name='Год создания')),
                ('description', models.TextField(blank=True, help_text='Введите краткое описание произведения', max_length=256, null=True, verbose_name='Краткое описание произведения')),
                ('category', models.ForeignKey(help_text='Введите название категории', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='titles', to='reviews.category', verbose_name='Название категории')),
                ('genre', models.ManyToManyField(help_text='Введите название жанра', through='reviews.GenreTitle', to='reviews.Genre', verbose_name='Название жанра')),
            ],
            options={
                'verbose_name': 'Произведение',
                'verbose_name_plural': 'Произведения',
                'ordering': ('category', 'name'),
            },
        ),
        migrations.AddField(
            model_name='genretitle',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.title'),
        ),
    ]