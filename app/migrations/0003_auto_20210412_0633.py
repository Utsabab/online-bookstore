# Generated by Django 3.1.7 on 2021-04-12 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210412_0632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='label',
            field=models.CharField(choices=[('G', 'good'), ('N', 'new'), ('A', 'acceptable')], max_length=1),
        ),
    ]
