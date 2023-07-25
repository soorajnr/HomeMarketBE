from django.db import models

# Create your models here.
class User(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=250)
    mobile=models.CharField(max_length=10,unique=True)

    
    def __str__(self):
        return self.name