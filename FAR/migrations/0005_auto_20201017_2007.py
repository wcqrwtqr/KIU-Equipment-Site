# Generated by Django 3.0.3 on 2020-10-17 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FAR', '0004_auto_20201010_1917'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='far_db',
            options={'ordering': ['equ_type']},
        ),
    ]
