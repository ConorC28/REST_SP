from rest_framework import serializers
from .models import Bucketlist

class BucketlistSerializer(serializers.ModelSerializer):
	"""Serializer to map the Model instance into Json format"""
	
	class Meta:
		"""Meta class to map serializers fields with the model fields"""
		model = Bucketlist
		fields = ('id', 'name', 'date_created','date_modified')
		read_only_fields = ('date_modified', 'date_crereated')