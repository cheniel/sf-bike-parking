from django.db import models

class BikeParking(models.Model):
	address=models.CharField(max_length=200)
	locationName=models.CharField(max_length=200)
	streetName=models.CharField(max_length=200)
	racks=models.IntegerField()
	spaces=models.IntegerField()
	placement=models.CharField(max_length=10)
	monthInstalled=models.IntegerField()
	yearInstalled=models.IntegerField()
	longitude=models.DecimalField(decimal_places=6,max_digits=12)
	latitude=models.DecimalField(decimal_places=6,max_digits=12)



