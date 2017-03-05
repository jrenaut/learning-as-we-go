from django.contrib import admin
from lawgo.models import *

@admin.register(Bio)
class BioAdmin(admin.ModelAdmin):
    list_display = ('user', 'display')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
