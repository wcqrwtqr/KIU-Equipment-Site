# Generated by Django 3.1.2 on 2020-10-31 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jobs', '0007_auto_20201019_1948'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobsdb',
            name='files',
            field=models.FileField(null=True, upload_to='jobsFiles/'),
        ),
    ]
