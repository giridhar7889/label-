# Generated by Django 3.1.1 on 2021-02-09 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20210206_1334'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('items_json', models.CharField(max_length=500)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('address1', models.CharField(max_length=500)),
                ('address2', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zip', models.IntegerField(max_length=50)),
                ('Phone_number', models.IntegerField(max_length=50)),
            ],
        ),
    ]