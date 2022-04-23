from django.db import models

# Create your models here.
class School(models.Model):
	name = models.CharField(max_length=200)
	location = models.CharField(max_length=200)
	founded =  models.CharField(max_length=50)
	_price = models.DecimalField(
				max_digits=15, 
				decimal_places=2, 
				default=99.99
			)

	@property
	def get_price_discount(self):
		return (30/100) * float(self._price)
	