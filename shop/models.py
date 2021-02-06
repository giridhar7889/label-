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




