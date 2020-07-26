from django.db import models
from django.contrib.auth.models import User


class Userprofile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    number=models.IntegerField(default="")
    profimage=models.ImageField(upload_to="static/profimage",default="")

    def __str__(self):
        return self.user.username

class Womens(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=100,default="")
    desc=models.CharField(max_length=500,default="")
    category=models.CharField(max_length=50,default="")
    subcategory=models.CharField(max_length=50,default="")
    price=models.IntegerField(default="")
    pub_date=models.DateField(default="")
    image=models.ImageField(upload_to="static/images",default="")
    detailimage=models.ImageField(upload_to="static/images",default="")
    detailimage2=models.ImageField(upload_to="static/images",default="")
    detailimage3=models.ImageField(upload_to="static/images",default="")
    detailimage4=models.ImageField(upload_to="static/images",default="")


    def __str__(self):
        return self.product_name


class Mens(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=100,default="")
    desc=models.CharField(max_length=500,default="")
    category=models.CharField(max_length=50,default="")
    subcategory=models.CharField(max_length=50,default="")
    price=models.IntegerField(default="")
    pub_date=models.DateField(default="")
    image=models.ImageField(upload_to="static/images",default="")
    detailimage=models.ImageField(upload_to="static/images",default="")
    detailimage2=models.ImageField(upload_to="static/images",default="")
    detailimage3=models.ImageField(upload_to="static/images",default="")
    detailimage4=models.ImageField(upload_to="static/images",default="")


    def __str__(self):
        return self.product_name


class Accessories(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=100,default="")
    desc=models.CharField(max_length=500,default="")
    category=models.CharField(max_length=50,default="")
    subcategory=models.CharField(max_length=50,default="")
    price=models.IntegerField(default="")
    pub_date=models.DateField(default="")
    image=models.ImageField(upload_to="static/images",default="")
    detailimage=models.ImageField(upload_to="static/images",default="")
    detailimage2=models.ImageField(upload_to="static/images",default="")
    detailimage3=models.ImageField(upload_to="static/images",default="")
    detailimage4=models.ImageField(upload_to="static/images",default="")


    def __str__(self):
        return self.product_name



