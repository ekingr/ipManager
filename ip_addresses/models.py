from django.db import models

# Create your models here.

class NetworkAddress(models.Model):
	address = models.IPAddressField()
	network_size = models.PositiveIntegerField()
	description = models.CharField(max_length=400)
	parent = models.ForeignKey('self')
	
