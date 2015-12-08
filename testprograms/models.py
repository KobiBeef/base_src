from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

# Create your models here.

############################ INDEPENDENT MODELS ############################
class Category(models.Model):
	# will change this to models.SlugField(max_length=200, unique=True)
	# name = models.CharField(max_length=200)
	name = models.SlugField(max_length=200, unique=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Category"
		verbose_name_plural = "Categories"

class Tag(models.Model):
	slug = models.SlugField(max_length=200, unique=True)

	def __str__(self):
		return self.slug

############################ ENTRY PAGE MODELS ############################
class Entry(models.Model):
	title = models.CharField(max_length=200)
	slug = models.SlugField(max_length=200, unique=True)
	body = models.TextField()
	user = models.ForeignKey(User, related_name="testuser", null=True)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	category = models.ForeignKey(Category)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('testprogram_entry_detail', kwargs={"category": self.category, "slug": self.slug})

	class Meta:
		ordering = ['-created']
		verbose_name = "Entry"
		verbose_name_plural = "Entries"

class EntryComment(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField(max_length=50)
	created = models.DateTimeField(auto_now_add=True)
	body = models.TextField()
	post = models.ForeignKey(Entry, related_name='comments', null=True)

	def __str__(self):
		return self.name

	class Meta():
		verbose_name = "Entry Comment"
		verbose_name_plural = "Entry Comments"

############################ PROGRAMMING PAGE MODELS ############################
class ProgramLanguage(models.Model):
	language = models.ForeignKey(Category, null=True)
	
	def __str__(self):
		return self.language.name

	class Meta():
		verbose_name = "Programming Language"
		verbose_name_plural = "Programming Languages"

class ProgramTutorial(models.Model):
	program_language = models.ForeignKey(ProgramLanguage, null=True)
	tutorial_name = models.CharField(max_length=100)
	tutorial_url = models.URLField(max_length=100, blank=True)
	tutorial_desc = models.TextField()
	tutorial_created = models.DateTimeField(auto_now_add=True)
	tutorial_modified = models.DateTimeField(auto_now=True)
	tutorial_tags = models.ManyToManyField(Tag)
	slug = models.SlugField(max_length=100, unique=True)

	def __str__(self):
		return self.tutorial_name

	def get_absolute_url(self):
		return reverse('programning_detail', kwargs={"category": self.category, "slug": self.slug})

	class Meta():
		verbose_name = "Programming Tutorial"
		verbose_name_plural = "Programming Tutorials"

class ProgramTutorialContent(models.Model):
	program_tutorial = models.ForeignKey(ProgramTutorial, related_name="topics", null=True)
	tutorial_topic = models.CharField(max_length=100)
	tutorial_body = models.TextField()
	tutorial_resources = models.URLField(max_length=100, blank=True)

	def __str__(self):
		return self.tutorial_topic

	class Meta():
		verbose_name = "Programming Tutorial Content"
		verbose_name_plural = "Programming Tutorial Contents"

############################ INTERWEBS PAGE MODELS ############################
class WebThemeType(models.Model):
	web_theme_type = models.CharField(max_length=100)

	def __str__(self):
		return self.web_theme_type

	class Meta():
		verbose_name = "Web Theme Type"
		verbose_name_plural = "Web Theme Types"

class WebThemeCategory(models.Model):
	web_theme_category = models.ForeignKey(Category, null=True)

	def __str__(self):
		return self.web_theme_category.name

	class Meta():
		verbose_name = "Web Theme Category"
		verbose_name_plural = "Web Theme Categories"

class WebThemeFeature(models.Model):
	feature = models.CharField(max_length=400, unique=True)

	def __str__(self):
		return self.feature

	class Meta():
		verbose_name = "Web Theme Feature"
		verbose_name_plural = "Web Theme Features"

class WebTheme(models.Model):
	live_preview = models.CharField(max_length=500, null=True)
	theme_name = models.CharField(max_length=100)
	slug = models.SlugField(max_length=100, unique=True)
	theme_image = models.ImageField(upload_to='static/testprograms/images/', blank=True)
	theme_desc_short = models.TextField()
	theme_desc_long =  models.TextField()
	theme_author = models.ForeignKey(User, related_name="theme_author", null=True)
	theme_created = models.DateTimeField(auto_now_add=True)
	theme_modified = models.DateTimeField(auto_now=True)
	theme_type = models.ForeignKey(WebThemeType, null=True)
	theme_features = models.ManyToManyField(WebThemeFeature)
	theme_category = models.ForeignKey(WebThemeCategory, null=True)
	theme_tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.theme_name

	def get_absolute_url(self):
		return reverse('testprograms_webtheme_detail', kwargs={"category": self.category, "slug": self.slug})

	class Meta():
		verbose_name = "Web Theme "
		verbose_name_plural = "Web Themes"

############################ MULTIMEDIA PAGE MODELS ############################
class MultiMediaCategory(models.Model):
	media_category = models.ForeignKey(Category, null=True)

	def __str__(self):
		return self.media_category.name

	class Meta():
		verbose_name = "Multimedia Category"
		verbose_name_plural = "Multimedia Categories"

class MultiMediaType(models.Model):
	media_type = models.CharField(max_length=100, null=True)

	def __str__(self):
		return self.media_type

	class Meta():
		verbose_name = "Multimedia Type"
		verbose_name_plural = "Multimedia Types"

class MultiMediaApi(models.Model):
	# media_name = models.ForeignKey(MultiMediaContent, null=True)
	api_title = models.CharField(max_length=500, null=True)
	api_pic_count = models.IntegerField(null=True)
	api_view_count = models.IntegerField(null=True)

	def __str__(self):
		return self.api_title

	class Meta:
		verbose_name = "MultiMedia API"
		verbose_name_plural = "MultiMedia API's"

class MultiMediaContent(models.Model):
	# embed_field for flicker
	embed_condition = models.BooleanField(default=False)
	embed_location = models.CharField(max_length=500, null=True)
	embed_title = models.CharField(max_length=500, null=True)
	embed_img_src = models.CharField(max_length=500, null=True)
	embed_img_width = models.IntegerField(null=True)
	embed_img_height = models.IntegerField(null=True)
	embed_img_alt = models.CharField(max_length=500, null=True)

	# testing flickr api
	api = models.ForeignKey(MultiMediaApi, null=True)

	# flickr url grab link
	url = models.URLField(max_length=100, blank=True)

	media_name = models.CharField(max_length=100)
	slug = models.SlugField(max_length=200, unique=True)
	media_creator = models.ForeignKey(User, related_name='mediatestuser', null=True)
	media_created = models.DateTimeField(auto_now_add=True)
	# will be removing this due to FLICKR API or not
	media_path = models.ImageField(upload_to='static/testprograms/images/multimedia/', blank=True)
	media_desc = models.TextField()
	media_category = models.ForeignKey(MultiMediaCategory, null=True)
	media_type = models.ForeignKey(MultiMediaType, null=True)
	media_tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.media_name

	class Meta():
		verbose_name = "Multimedia Content"
		verbose_name_plural = "Multimedia Contents"

############################ HARDWARE PAGE MODELS ############################
class HardwareCategory(models.Model):
	category = models.ForeignKey(Category, null=True)

	def __str__(self):
		return self.category.name

	class Meta():
		verbose_name = "Hardware Category"
		verbose_name_plural = "Hardware Categories"

class HardwareFeature(models.Model):
	hardware_feature = models.CharField(max_length=400, unique=True)

	def __str__(self):
		return self.hardware_feature

	class Meta():
		verbose_name = "Hardware Feature"
		verbose_name_plural = "Hardware Features"

class HardwareDetail(models.Model):
	hardware_category = models.ForeignKey(HardwareCategory)
	hardware_name = models.CharField(max_length=200)
	hardware_brand = models.CharField(max_length=100)
	hardware_model = models.CharField(max_length=100)
	hardware_desc = models.TextField()
	hardware_features = models.ManyToManyField(HardwareFeature)

	def __str__(self):
		return self.hardware_name

	class Meta():
		verbose_name = "Hardware Detail"
		verbose_name_plural = "Hardware Details"

class HardwarePost(models.Model):
	hardware_post_title = models.CharField(max_length=100)
	# add a post image
	# hardware_post_image = models.ImageField()
	hardware_name = models.ForeignKey(HardwareDetail, null=True)
	hardware_post_creator = models.ForeignKey(User, related_name="testuserhardware", null=True)
	hardware_post_created = models.DateTimeField(auto_now_add=True)
	hardware_post_modified = models.DateTimeField(auto_now=True)
	hardware_post_body = models.TextField()
	hardware_post_tags = models.ManyToManyField(Tag)
	slug = models.SlugField(max_length=100, unique=True)

	def __str__(self):
		return self.hardware_post_title

	def get_absolute_url(self):
		return reverse('testprograms_hardwarepost_detail', kwargs={"category": self.hardware_name.hardware_category.category.name, "slug": self.slug})

	class Meta():
		ordering = ['-hardware_post_created']
		verbose_name = "Hardware Post"
		verbose_name_plural = "Hardware Posts"

class HardwareComment(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField(max_length=50)
	created = models.DateTimeField(auto_now_add=True)
	body = models.TextField()
	hardware_comment_post = models.ForeignKey(HardwarePost, related_name='comments', null=True)

	def __str__(self):
		return self.name

	class Meta():
		verbose_name = "Hardware Comment"
		verbose_name_plural = "Hardware Comments"