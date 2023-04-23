from django.db import models

# Model for storing product information
class Product(models.Model):
	id = 			models.CharField(max_length = 12, null=False, blank=False, unique=True, primary_key=True)
	title = 		models.CharField(max_length=200)
	price = 		models.DecimalField(max_digits=6, decimal_places=2, null=False)
	category = 		models.CharField(max_length=100)
	description = 	models.TextField(max_length=500)
	image = 		models.TextField(max_length=300)
	
	def __str__(self):
		return self.id + " " + self.title
	
	class Meta:
		ordering = ["id"]