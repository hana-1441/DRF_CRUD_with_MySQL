# Generated by Django 4.2.7 on 2023-12-02 07:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApiData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.TextField(blank=True, max_length=100, null=True)),
                ('creation_date', models.DateField(default=2, null=True)),
                ('last_updated', models.DateTimeField(default=datetime.datetime(2023, 12, 2, 13, 2, 52, 360793), null=True)),
            ],
            options={
                'db_table': 'Api_data',
            },
        ),
    ]
