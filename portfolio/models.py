from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

# DATABASE RESTRUCTURERING FOR EASE ON CREATING PAGES and for EXPANSION and DATA RESUSE

# Create your models here.

# INDEPENDENT MODLES
class Tag(models.Model):
	slug = models.SlugField(max_length=200, unique=True)

	def __str__(self):
		return self.slug

class Category(models.Model):
	name = models.CharField(max_length=30)
	
	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Category"
		verbose_name_plural = "Categories"

########################### ENTRY(PAGE) temporary home or landing page ###########################
# MAIN MODELS:

# class EntryCategory(models.Model):
	# entry_category = models.ForeignKey(Category, null=True)

class Entry(models.Model):
	title = models.CharField(max_length=200)
	slug = models.SlugField(max_length=200, unique=True)
	#######################
	# decommisioning this #
	#######################
	category = models.ForeignKey(Category, null=True)
	# replaced by this #
	# entry_category = models.ForeignKey(EntryCategory, null=True)

	user = models.ForeignKey(User)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	body = models.TextField()
	tags = models.ManyToManyField(Tag)
	publish = models.BooleanField(default=False)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('entry_detail', kwargs={"category": self.category, "slug": self.slug})

	# YOU CAN DO DOUBLE get_absolute_url()
	# def get_absolute_url(self):
	# 	return reverse('program_detail', kwargs={"category": self.category, "slug": self.slug})

	class Meta:
		verbose_name = "Entry"
		verbose_name_plural = "Entries"
		ordering = ["-created"]

class Comment(models.Model):
	name = models.CharField(max_length=50)
	body = models.TextField()
	created = models.DateTimeField(auto_now_add=True, null=True)
	entry_post = models.ForeignKey(Entry, blank=True, null=True)

	def __str__(self):
		return self.name

########################### PROGRAMMING PAGE ###########################
# MAIN MODEL/S:
# class ProgramLanguage(models.Model):
	# language = models.ForeignKey(Category, null=True)

class ProgramTutorial(models.Model):
	# program_language = models.ForeignKey(ProgramLanguage, null=True)
	tutorial_name = models.CharField(max_length=90)
	# tutorial_url = models.URLField(max_length=100, blank=True)
	slug = models.SlugField(max_length=200, unique=True)
	description = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	category = models.ForeignKey(Category, null=True)
	user = models.ForeignKey(User, null=True)
	tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.tutorial_name

	def get_absolute_url(self):
		return reverse('program_tutorial_detail', kwargs={"category": self.category, "slug": self.slug})

	class Meta:
		verbose_name = "Program Tutorial"
		verbose_name_plural = "Program Tutorials"

class ProgramTutorialDetail(models.Model):
	topic = models.CharField(max_length=90)
	body = models.TextField()
	tutorial_name = models.ForeignKey(ProgramTutorial, null=True)
	category = models.ForeignKey(Category, null=True)

	def __str__(self):
		return self.topic

	class Meta:
		verbose_name = "Program Tutorial Detail"
		verbose_name_plural = "Program Tutorial Details"

# creating model for InterWebs
class WebThemeFeature(models.Model):
	feature = models.CharField(max_length=200, unique=True)

	def __str__(self):
		return self.feature

	class Meta:
		verbose_name = "Web Theme Feature"
		verbose_name_plural = "Web Theme Features"

class WebTheme(models.Model):
	theme_name = models.CharField(max_length=50)
	slug = models.SlugField(max_length=200, unique=True)
	
	##############################
	# this field requires PILLOW #
	##############################
	theme_image = models.ImageField(upload_to='static/portfolio/images/', blank=True)

	# will setup /MEDIA_ROOT/ in settings
	# theme_file = models.ImageField(upload_to='templates/portfolio/bootstrap_live_preview/', blank=True)

	theme_desc_short = models.TextField()
	theme_desc_long = models.TextField()
	theme_author = models.CharField(max_length=50)
	theme_license = models.CharField(max_length=50)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	theme_features = models.ManyToManyField(WebThemeFeature)
	theme_category = models.ForeignKey(Category, null=True)
	# theme_category would be
		# - Admin and Dashboard
		# - Full Websites
	theme_tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.theme_name

	def get_absolute_url(self):
		return reverse('webtheme_detail', kwargs={"theme_slug": self.theme_slug})

	class Meta:
		verbose_name = "Web Theme"
		verbose_name_plural = "Web Themes"