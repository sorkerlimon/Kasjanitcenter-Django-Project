# Generated by Django 4.2.6 on 2023-10-10 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseapplication', '0003_alter_courseregistration_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseregistration',
            name='address',
            field=models.CharField(max_length=100),
        ),
    ]
