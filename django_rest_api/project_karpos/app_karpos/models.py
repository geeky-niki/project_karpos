from django.db import models

# Create your models here.
#creating my first model

class daily_transection (models.Model):
  cust_id = models.IntegerField()
  cust_name =models.CharField(max_length=100)
  product_bought = models.CharField(max_length=100)
  product_price = models.DecimalField(max_digits=5, decimal_places=2)
  quantity = models.IntegerField()
  is_regular = models.BooleanField(default=False)

