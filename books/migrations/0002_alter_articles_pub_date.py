# Generated by Django 4.1.2 on 2023-05-21 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='pub_date',
            field=models.DateField(verbose_name='Дата публикации книги'),
        ),
    ]
