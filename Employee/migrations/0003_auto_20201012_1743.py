# Generated by Django 3.0.3 on 2020-10-12 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0002_auto_20201012_1738'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employeedb',
            old_name='Nationality',
            new_name='nationality',
        ),
        migrations.RenameField(
            model_name='employeedb',
            old_name='Position',
            new_name='position',
        ),
        migrations.AddField(
            model_name='employeedb',
            name='grade',
            field=models.IntegerField(blank=True, default=8),
        ),
    ]
