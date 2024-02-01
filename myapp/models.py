from django.db import models
from datetime import datetime

# Create your models here.

class ApiData(models.Model):
    id=models.AutoField(primary_key=True)
    text=models.TextField(max_length=100,null=True,blank=True)
    creation_date=models.DateField(default=datetime.now().day,null=True)
    last_updated=models.DateTimeField(default=datetime.now(),null=True)

    class Meta:
        db_table='Api_data'