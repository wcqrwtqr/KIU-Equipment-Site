# Generated by Django 3.0.3 on 2020-10-12 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jobs', '0002_auto_20201012_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobsdb',
            name='endDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='jobsdb',
            name='startDate',
            field=models.DateField(null=True),
        ),
    ]
