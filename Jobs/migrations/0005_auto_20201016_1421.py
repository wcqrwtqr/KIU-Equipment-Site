# Generated by Django 3.0.3 on 2020-10-16 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jobs', '0004_jobmasterinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobmasterinfo',
            name='gasRate',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=10),
        ),
        migrations.AlterField(
            model_name='jobmasterinfo',
            name='oilRate',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
    ]