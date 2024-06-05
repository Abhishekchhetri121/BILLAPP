from django.db import models

import random, string
# Create your models here.

def generate_random_id():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))



class CategoryList(models.Model):
   
    code = name = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Company(models.Model):
   id = models.CharField(primary_key=True, default=generate_random_id, editable=False, max_length=10)
   name = models.CharField(max_length=100, unique=True)
   email = models.CharField(max_length=50, unique=True)
   phone = models.CharField(max_length=15, unique=True)
   pan_no = models.CharField(max_length=20, unique=True)
   address = models.CharField(max_length=20)
   image = models.ImageField(default="Image Not Found",null=True)
   established = models.DateField()
   Type= models.CharField(max_length=100,unique=False,default="")
  

   def __str__(self):
      
      return self.name +"-"+self.Type
   

   
class Category(models.Model):
    id = models.CharField(primary_key=True, default=generate_random_id, editable=False, max_length=10)
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE,default="")
    image = models.ImageField(null=True)
     
    def __str__(self):
        return self.name

class Product(models.Model):
    Product_id = models.CharField(primary_key=True, default=generate_random_id, editable=False, max_length=10)
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=10,default=0)
    image = models.ImageField(default="",null=True)
    created_date = models.DateField(auto_now=True)
    updated_date = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)


    def __str__(self):
        return self.name
    