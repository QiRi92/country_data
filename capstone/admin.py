from django.contrib import admin

# Register your models here.
from App.models import Directory

class DirectoryAdmin(admin.ModelAdmin):
    list_display = ['country', 'topics', 'last_update' ,'next_release']
    search_fields = ['country']
    list_per_page = 8

admin.site.register(Directory, DirectoryAdmin)

