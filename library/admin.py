from django.contrib import admin
from . import models
# Register your models here.

class PublisherAdmin(admin.ModelAdmin):
	list_display = ("name", "website")

class AuthorAdmin(admin.ModelAdmin):
	list_display = ("name", "email")

class BookAdmin(admin.ModelAdmin):
	list_display = ("title",)

class CategoryAdmin(admin.ModelAdmin):
	list_display = ("category",)

class ContactAdmin(admin.ModelAdmin):
	list_display = ("name",)

class CommentAdmin(admin.ModelAdmin):
	list_display = ("name", "contact", )


admin.site.register(models.Publisher, PublisherAdmin)
admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Book, BookAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Contact, ContactAdmin)
admin.site.register(models.TestComment, CommentAdmin)