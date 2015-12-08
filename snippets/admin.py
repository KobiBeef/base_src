from django.contrib import admin
from . import models

# Register your models here.
class SnippetAdmin(admin.ModelAdmin):
	list_display = ('title', 'created')

admin.site.register(models.Snippet, SnippetAdmin)