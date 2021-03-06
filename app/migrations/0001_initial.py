# Generated by Django 2.2.16 on 2020-12-10 12:07

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique_for_date='posted', verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Краткое содержание')),
                ('content', models.TextField(verbose_name='Полное содержание')),
                ('posted', models.DateTimeField(db_index=True, default=datetime.datetime(2020, 12, 10, 15, 7, 12, 615531), verbose_name='Опубликована')),
                ('image', models.FileField(default='temp.jpg', upload_to='', verbose_name='Путь к картинке')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'статья блога',
                'verbose_name_plural': 'статьи блога',
                'db_table': 'Posts',
                'ordering': ['-posted'],
            },
        ),
        migrations.CreateModel(
            name='Zakaz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique_for_date='posted', verbose_name='ФИО')),
                ('number', models.CharField(max_length=100, unique_for_date='posted', verbose_name='Телефон')),
                ('pay', models.CharField(choices=[('1', 'Наличные'), ('2', 'Безналичный расчет')], max_length=100, verbose_name='Способ оплаты')),
                ('rabota', models.CharField(choices=[('1', 'Забрать груз'), ('2', 'Аренда манипулятора'), ('3', 'Аренда грузовой машины')], max_length=100, verbose_name='Вид работы')),
                ('description', models.TextField(verbose_name='Подробнее о заказе')),
                ('posted', models.DateTimeField(db_index=True, default=datetime.datetime(2020, 12, 10, 15, 7, 12, 616529), verbose_name='Дата')),
                ('image', models.FileField(default='temp.jpg', upload_to='', verbose_name='Фото места работы')),
                ('status', models.BooleanField(default=False, verbose_name='Статус заказа')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Имя пользователя')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказ клиента',
                'db_table': 'Zakaz',
                'ordering': ['-posted'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Комментарий')),
                ('date', models.DateTimeField(db_index=True, default=datetime.datetime(2020, 12, 10, 15, 7, 12, 616529), verbose_name='Дата')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Blog', verbose_name='Статья')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарий к статьям блога',
                'db_table': 'Comments',
                'ordering': ['-date'],
            },
        ),
    ]
