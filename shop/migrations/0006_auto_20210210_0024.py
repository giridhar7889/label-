# Generated by Django 3.1.1 on 2021-02-09 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20210210_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='Phone_number',
            field=models.CharField(max_length=50),
        ),
    ]
