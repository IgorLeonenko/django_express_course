from django.db import models

# Create your models here.
class Item(models.Model):
    item_name  = models.CharField(max_length=200)
    item_desc  = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500, default="https://t3.ftcdn.net/jpg/02/48/42/64/360_F_248426448_NVKLywWqArG2ADUxDq6QprtIzsF82dMF.jpg")

    def __str__(self):
        return self.item_name