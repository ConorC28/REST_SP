from django.db import models

# Create your models here.
class Gameslist(models.Model):
	"""This represents the Games model"""
	"""Owner = models.ForeignKey('auth.User',)"""
	Title = models.CharField(max_length=225, blank=False, unique=True)
	Console = models.CharField(max_length=50, blank=False, unique=True)
	ReleaseDate = models.CharField(max_length=10, blank=False, unique=True)
	Description = models.CharField(max_length=5000, blank=False, unique=True)
	FondMemories = models.CharField(max_length=10000, blank=False, unique=True)
	date_created = models.DateTimeField(auto_now_add=True)
	date_modified = models.DateTimeField(auto_now=True)
	
	def __str__(self):
		"""Return a human readable version"""
		return "{}".format(self.name)
	
class Bucketlist(models.Model):
	"""This class represents the bucket  model"""
	name = models.CharField(max_length=255, blank=False, unique=True)
	date_created = models.DateTimeField(auto_now_add=True)
	date_modified = models.DateTimeField(auto_now=True)
	
	def __str__(self):
		"""Return a humen readable representation of the model instance"""
		return "{}".format(self.name)