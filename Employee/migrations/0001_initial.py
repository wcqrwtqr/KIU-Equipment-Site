# Generated by Django 3.0.3 on 2020-10-12 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeDB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OSID', models.IntegerField(unique=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('Nationality', models.CharField(blank=True, default='Iraq', max_length=255)),
                ('Position', models.CharField(blank=True, max_length=255)),
                ('isExpat', models.BooleanField(default=False)),
                ('rotation', models.CharField(blank=True, default='5x5', max_length=10)),
            ],
        ),
    ]
