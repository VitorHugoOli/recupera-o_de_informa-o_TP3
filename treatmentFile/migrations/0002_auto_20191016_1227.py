# Generated by Django 2.2.6 on 2019-10-16 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treatmentFile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='texto',
            name='texto',
            field=models.CharField(max_length=10000000),
        ),
    ]
