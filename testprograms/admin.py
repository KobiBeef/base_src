from django.contrib import admin
from . import models
from django_markdown.admin import MarkdownModelAdmin
from django_markdown.widgets import AdminMarkdownWidget
from django.db.models import TextField
# Register your models here.
# FOR DEVELOPMENT PURPOSE I POST ALL MODELS, will remove unecessary models when deployed
##################### INDEPENDENT ADMIN MODELS #####################
class CategoryAdmin(admin.ModelAdmin):
	list_display = ("name",)

class TagAdmin(admin.ModelAdmin):
	list_display = ("slug",)

##################### ENTRY ADMIN MODELS #####################
class EntryAdmin(MarkdownModelAdmin):
	list_display = ("title", "created",)
	prepopulated_fields = {"slug": ("title",)}
	formfield_overrides = {TextField: {'widget': AdminMarkdownWidget}}

class EntryCommentAdmin(admin.ModelAdmin):
	list_display = ("name", "created", )

##################### PROGRAMMING ADMIN MODELS #####################
class ProgramLanguageAdmin(admin.ModelAdmin):
	list_display = ("language",)

class ProgramTutorialAdmin(admin.ModelAdmin):
	list_display = ("tutorial_name", "tutorial_url", "program_language", )
	prepopulated_fields = {"slug": ("tutorial_name",)}
	formfield_overrides = {TextField: {'widget': AdminMarkdownWidget}}

class ProgramTutorialContentAdmin(admin.ModelAdmin):
	list_display = ("program_tutorial", "tutorial_topic", )
	formfield_overrides = {TextField: {'widget': AdminMarkdownWidget}}

##################### INTERWEBS ADMIN MODELS #####################
class WebThemeTypeAdmin(admin.ModelAdmin):
	list_display = ("web_theme_type",)

class WebThemeCategoryAdmin(admin.ModelAdmin):
	list_display = ("web_theme_category",)

class WebThemeFeatureAdmin(admin.ModelAdmin):
	list_display = ("feature",)

class WebThemeAdmin(admin.ModelAdmin):
	list_display = ("theme_name", "theme_type", "theme_category",)
	prepopulated_fields = {"slug": ("theme_name",)}
	formfield_overrides = {TextField: {'widget': AdminMarkdownWidget}}

##################### MULTIMEDIA ADMIN MODELS #####################
class MultiMediaCategoryAdmin(admin.ModelAdmin):
	list_display = ("media_category", )

class MultiMediaTypeAdmin(admin.ModelAdmin):
	list_display = ("media_type", )

class MultiMediaContentAdmin(admin.ModelAdmin):
	list_display = ("media_name", "media_creator", "media_type", "media_category" )
	prepopulated_fields = {"slug": ("media_name",)}
	formfield_overrides = {TextField: {'widget': AdminMarkdownWidget}}

class MultiMediaApiAdmin(admin.ModelAdmin):
	list_display = ("api_title", "api_pic_count", "api_view_count")

##################### HARDWARE ADMIN MODELS #####################
class HardwareCategoryAdmin(admin.ModelAdmin):
	list_display = ("category", )

class HardwareFeatureAdmin(admin.ModelAdmin):
	list_display = ("hardware_feature",)

class HardwareDetailAdmin(admin.ModelAdmin):
	list_display = ("hardware_name", "hardware_category", "hardware_brand",)
	formfield_overrides = {TextField: {'widget': AdminMarkdownWidget}}

class HardwarePostAdmin(admin.ModelAdmin):
	list_display = ("hardware_post_title", "hardware_name", "hardware_post_created", )
	prepopulated_fields = {"slug": ("hardware_post_title",)}
	formfield_overrides = {TextField: {'widget': AdminMarkdownWidget}}

class HardwareCommentAdmin(admin.ModelAdmin):
	list_display = ("name", "created", )

######### INDEPENDENT MODELS REGISTER #########
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Tag, TagAdmin)

######### ENTRY ADMIN MODELS REGISTER #########
admin.site.register(models.Entry, EntryAdmin)
admin.site.register(models.EntryComment, EntryCommentAdmin)

######### PROGRAMMING ADMIN MODELS REGISTER #########
admin.site.register(models.ProgramLanguage, ProgramLanguageAdmin)
admin.site.register(models.ProgramTutorial, ProgramTutorialAdmin)
admin.site.register(models.ProgramTutorialContent, ProgramTutorialContentAdmin)

######### INTERWEBS ADMIN MODELS REGISTER #########
admin.site.register(models.WebThemeType, WebThemeTypeAdmin)
admin.site.register(models.WebThemeCategory, WebThemeCategoryAdmin)
admin.site.register(models.WebThemeFeature, WebThemeFeatureAdmin)
admin.site.register(models.WebTheme, WebThemeAdmin)

######## MULTIMEDIA ADMIN MODELS REGISTER #########
admin.site.register(models.MultiMediaCategory, MultiMediaCategoryAdmin)
admin.site.register(models.MultiMediaType, MultiMediaTypeAdmin)
admin.site.register(models.MultiMediaContent, MultiMediaContentAdmin)
admin.site.register(models.MultiMediaApi, MultiMediaApiAdmin)

######### HARDWARE ADMIN MODELS REGISTER #########
admin.site.register(models.HardwareCategory, HardwareCategoryAdmin)
admin.site.register(models.HardwareFeature, HardwareFeatureAdmin)
admin.site.register(models.HardwareDetail, HardwareDetailAdmin)
admin.site.register(models.HardwarePost, HardwarePostAdmin)
admin.site.register(models.HardwareComment, HardwareCommentAdmin)