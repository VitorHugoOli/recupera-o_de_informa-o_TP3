# Generated by Django 2.2.6 on 2019-10-16 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treatmentFile', '0002_auto_20191016_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='texto',
            name='texto',
            field=models.CharField(max_length=1000000),
        ),
    ]
