from django.contrib import admin
from docmanager.models import *

# Register your models here.
class DocumentAdmin(admin.ModelAdmin):
    list_display_links = None
    list_display = ['ISBN', 'title', 'author']
    list_editable = ['ISBN', 'title', 'author']
    list_filter = ['doc_type', 'author']

class AuthorAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Author._meta.fields]

admin.site.register(Document, DocumentAdmin)
admin.site.register(Author, AuthorAdmin)