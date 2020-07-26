from django.db import models

# Create your models here.

class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=100,default="")
    desc=models.CharField(max_length=500,default="")
    category=models.CharField(max_length=50,default="")
    subcategory=models.CharField(max_length=50,default="")
    price=models.IntegerField(default="")
    pub_date=models.DateField(default="")
    image=models.ImageField(upload_to="static/images",default="")
    detailimage=models.ImageField(upload_to="static/images",default="")

    def __str__(self):
        return self.product_name


