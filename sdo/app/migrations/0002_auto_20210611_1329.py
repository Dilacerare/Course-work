# Generated by Django 3.2.4 on 2021-06-11 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cycles',
            name='begin',
            field=models.DateField(verbose_name='Начало'),
        ),
        migrations.AlterField(
            model_name='cycles',
            name='end',
            field=models.DateField(verbose_name='Окончание'),
        ),
        migrations.AlterField(
            model_name='users',
            name='BDay',
            field=models.DateField(verbose_name='День рождения'),
        ),
    ]
