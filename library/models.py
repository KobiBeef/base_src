from django.core.urlresolvers import reverse
from django.db import models
from django import forms

# Create your models here.
# class from django tutorial
class Category(models.Model):
	category = models.CharField(max_length=20)

	def __str__(self):
		return self.category

class Publisher(models.Model):
	name = models.CharField(max_length=30)
	address = models.CharField(max_length=50)
	city = models.CharField(max_length=60)
	state_province = models.CharField(max_length=30)
	country = models.CharField(max_length=50)
	website = models.URLField()

	class Meta:
		ordering = ["-name"]

	def __str__(self):
		return self.name

class Author(models.Model):
	salutation = models.CharField(max_length=10)
	name = models.CharField(max_length=200)
	email = models.EmailField()

	def __str__(self):
		return self.name

class Book(models.Model):
	title = models.CharField(max_length=100)
	authors = models.ManyToManyField('Author')
	publisher = models.ForeignKey(Publisher)
	publication_date = models.DateField()
	category = models.ForeignKey(Category)

	def __str__(self):
		return self.title

# THIS WILL BE THE MODEL FOR THE COMMENTS ############################################
class Contact(models.Model):
	name = models.CharField(max_length=100)
	message = models.TextField()

	def get_absolute_url(self):
		return reverse('contact_detail', kwargs={'pk': self.pk})

	def __str__(self):
		return self.name

class TestComment(models.Model):
	name = models.CharField(max_length=20, blank=True)
	message = models.TextField()
	contact = models.ForeignKey(Contact, blank=True, null=True)

	def __str__(self):
		return self.name
######################################################################################