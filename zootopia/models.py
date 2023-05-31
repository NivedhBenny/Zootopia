from django.db import models
from django.contrib.auth.models import User

class Pets(models.Model):
    PetType=models.CharField(max_length=10)
    Breed=models.CharField(max_length=10)
    PhotoPet=models.ImageField(upload_to="images")
    PetName=models.CharField(max_length=10,default=0000)
    SpecialCare=models.CharField(max_length=10)
    Price=models.CharField(max_length=10)
    Status=models.CharField(max_length=10)

class Products(models.Model):
    ProductType=models.CharField(max_length=10)
    PetType=models.CharField(max_length=10)
    PhotoProd=models.FileField()
    Size=models.CharField(max_length=10)
    Quantity=models.CharField(max_length=10)
    Price=models.CharField(max_length=10)
    Status=models.CharField(max_length=10)

class Register_User(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Email=models.EmailField()
    Name=models.CharField(max_length=50)
    Gender=models.CharField(max_length=20)
    Username=models.CharField(max_length=20)
    Password1=models.CharField(max_length=20)
    Password2=models.CharField(max_length=20)
    role=models.CharField(max_length=20)
    status=models.CharField(max_length=20)

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Pets=models.ForeignKey(Pets,on_delete=models.CASCADE,null=True, blank=True)
    Products = models.ForeignKey(Products, on_delete=models.CASCADE,null=True, blank=True)
    petname=models.CharField(max_length=10)
    photo=models.FileField()
    price=models.CharField(max_length=10)
    quantity=models.CharField(max_length=10,default="1")
    cart_status=models.CharField(max_length=10)

class Pay(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Pets=models.ForeignKey(Pets,on_delete=models.CASCADE)
    petsname=models.CharField(max_length=10)
    price=models.CharField(max_length=10)
    cart_status=models.CharField(max_length=10)

class Address(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=10)
    lastname=models.CharField(max_length=10)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=10)
    State=models.CharField(max_length=10)
    zip=models.CharField(max_length=10)

class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    petname=models.CharField(max_length=10)
    photo=models.FileField()
    price=models.CharField(max_length=10)
    quantity=models.CharField(max_length=10,default="1")
    total=models.CharField(max_length=10)
    order_status=models.CharField(max_length=10)
