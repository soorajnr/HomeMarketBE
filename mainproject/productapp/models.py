from django.db import models
from userapp.models import User
from location_field.models.plain import PlainLocationField
# Create your models here.
class Category_class(models.Model):
    category=models.CharField(max_length=250)
    
    def __str__(self):
       return self.category

class Product(models.Model):
    id=models.AutoField(primary_key=True,unique=True)
    name=models.CharField(max_length=250)
    seller=models.ForeignKey(User,on_delete=models.CASCADE)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    description=models.CharField(max_length=300)
    category=models.ForeignKey(Category_class,on_delete=models.CASCADE)
    photo=models.ImageField(upload_to='images',blank=True)
    location = PlainLocationField(based_fields=['city'], zoom=7)
    quantity=models.FloatField(blank=True)
    date_added=models.DateField(auto_now_add=True)
    price_cat=models.CharField(max_length=100,blank=True)

    def __str__(self):
        return '{}'.format(self.name)

    
    
