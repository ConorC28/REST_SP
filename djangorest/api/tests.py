from django.test import TestCase
from .models import Bucketlist
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse
# Create your tests here.

class ModelTestCase(TestCase):
	"""This class defines the test suite for the bucketlist model."""

	def setUp(self):
		"""Define the test client and other test variables."""
		self.bucketlist_name = "Write world class code"
		self.bucketlist = Bucketlist(name=self.bucketlist_name)
	
	def test_model_can_create_a_bucketlist(self):
		"""Test the bucketlist model can create bucketlist."""
		old_count = Bucketlist.objects.count()
		self.bucketlist.save()
		new_count = Bucketlist.objects.count()
		self.assertNotEqual(old_count, new_count)
		
class ViewTestCase(TestCase):
	def setUp(self):
		"""Define the test client and other test variables"""
		self.client = APIClient()
		self.bucketlist_data = {'name':'Go to Ibiza'}
		self.response = self.client.post(
			reverse('create'),
			self.bucketlist_data,
			format="json")

	def test_api_can_create_a_bucketlist(self):
		"""Test the api has bucketlist creation compatibility"""
		self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)		

	def test_api_can_get_a_bucketlist(self):
		"""Test the api can get a given bucketlist"""
		bucketlist = Bucketlist.object.get()
		response = self.client.get(
			reverse('details', kwargs={'pk':bucketlist.id}),
			format="json")
			
		self.assertREqual(res.statys_code, status.http_200_ok)
		self.assertContains(response, bucketlist)
	
	def test_api_can_update_bucketlist(self):
	"""Test the API can update given bucketlist"""
		change_bucketlist = {'name':'Something new'}
		response = self.client.put(
			reverse('details',kwargs={'pk': bucketlist.id}),
			change_bucketlist, format="json")
			
		self.assertREqual(res.statys_code, status.http_200_ok)
		
	def test_api_can_delete_bucketlist(self):
	"""Test the API can update given bucketlist"""
		bucketlist = Bucketlist.objects.get()
		response = self.client.delete(
			reverse('details',kwargs={'pk': bucketlist.id}),
			change_bucketlist, format="json",
			follow=True)
			
		self.assertREqual(res.statys_code, status.http_200_ok)