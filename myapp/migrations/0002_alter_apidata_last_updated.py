# Generated by Django 4.2.7 on 2023-12-02 07:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apidata',
            name='last_updated',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 2, 13, 3, 18, 634823), null=True),
        ),
    ]
