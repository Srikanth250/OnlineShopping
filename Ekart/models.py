from django.db import models

# Create your models here.
class Mobile(models.Model):
	product_image = models.CharField(max_length=250)
	product_name = models.CharField(max_length=100)
	product_small_description = models.TextField()
	product_big_description = models.TextField()
	product_price = models.IntegerField()
	company_name = models.CharField(max_length=100)
	
	def __str__(self):
		return self.product_name
		
class Laptop(models.Model):
	product_image = models.CharField(max_length=250)
	product_name = models.CharField(max_length=100)
	product_small_description = models.TextField()
	product_big_description = models.TextField()
	product_price = models.IntegerField()
	company_name = models.CharField(max_length=100)
	
	def __str__(self):
		return self.product_name
		
class Camera(models.Model):
	product_image = models.CharField(max_length=250)
	product_name = models.CharField(max_length=100)
	product_small_description = models.TextField()
	product_big_description = models.TextField()
	product_price = models.IntegerField()
	company_name = models.CharField(max_length=100)
	
	def __str__(self):
		return self.product_name
