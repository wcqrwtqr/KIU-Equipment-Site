# Generated by Django 3.0.3 on 2020-10-17 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0003_auto_20201012_1743'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employeedb',
            options={'ordering': ['first_name']},
        ),
    ]