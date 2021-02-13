from django.db import models

# Create your models here.
class product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    category=models.CharField(max_length=50,default="")
    subcategory=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=3000)
    publish_date=models.DateField()
    image=models.ImageField(upload_to="shop/images",default="")

    def __str__(self):
        return self.product_name
class Contact(models.Model):
    message_id=models.AutoField(primary_key=True)

    name=models.CharField(max_length=70,default="")
    email=models.CharField(max_length=50,default="")
    phone=models.CharField(max_length=15,default="")
    desc=models.CharField(max_length=500,default="")

    def __str__(self):
        return self.name

class Orders(models.Model):
    order_id=models.AutoField(primary_key=True)
    items_json=models.CharField(max_length=500)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    address1=models.CharField(max_length=500)
    address2=models.CharField(max_length=500)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    zip=models.CharField(max_length=50)
    Phone_number=models.CharField(max_length=50)

    def __str__(self):
        return self.name


class OrderUpdate(models.Model):
    update_id=models.AutoField(primary_key=True)
    order_id=models.IntegerField(default="")
    update_desc=models.CharField(max_length=5000)
    timestamp=models.DateField(auto_now_add=True)


    def __str__(self):
        return self.update_desc[0:7]+"....."



