from django.contrib import admin
from . import models
from django_markdown.admin import MarkdownModelAdmin
from django_markdown.widgets import AdminMarkdownWidget
from django.db.models import TextField
# Register your models here.

class EntryAdmin(MarkdownModelAdmin):
	list_display = ("title", "category", "created")
	prepopulated_fields = {"slug": ("title",)}
	formfield_overrides = {TextField: {'widget': AdminMarkdownWidget}}

class CommentAdmin(admin.ModelAdmin):
	list_display = ("name", "entry_post",)

class CategoryAdmin(admin.ModelAdmin):
	list_display = ("name",)

class ProgramTutorialAdmin(admin.ModelAdmin):
	list_display = ("tutorial_name", "created", "category",)
	prepopulated_fields = {"slug": ("tutorial_name",)}
	formfield_overrides = {TextField: {'widget': AdminMarkdownWidget}}

class ProgramTutorialDetailAdmin(admin.ModelAdmin):
	list_display = ("topic", "category", "tutorial_name",)
	formfield_overrides = {TextField: {'widget': AdminMarkdownWidget}}

class WebThemeFeatureAdmin(admin.ModelAdmin):
	list_display = ("feature",)

class WebThemeAdmin(admin.ModelAdmin):
	list_display = ("theme_name", "theme_category", "theme_author",)
	prepopulated_fields = {"slug": ("theme_name",)}
	
	
admin.site.register(models.Entry, EntryAdmin)
admin.site.register(models.Tag)
admin.site.register(models.Comment, CommentAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.ProgramTutorial, ProgramTutorialAdmin)
admin.site.register(models.ProgramTutorialDetail, ProgramTutorialDetailAdmin)
admin.site.register(models.WebThemeFeature, WebThemeFeatureAdmin)
admin.site.register(models.WebTheme, WebThemeAdmin)