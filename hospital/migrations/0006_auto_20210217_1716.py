# Generated by Django 3.1.6 on 2021-02-17 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0005_auto_20210217_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='app_date',
            field=models.DateField(),
        ),
    ]
