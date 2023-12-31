# Generated by Django 4.2.6 on 2023-10-10 04:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CourseRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('father_name', models.CharField(max_length=100)),
                ('mother_name', models.CharField(max_length=100)),
                ('national_id', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('mobile_number', models.CharField(max_length=15)),
                ('bkash_transaction_id', models.CharField(max_length=20)),
                ('registration_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('courses', models.ManyToManyField(to='courseapplication.course')),
            ],
        ),
    ]
