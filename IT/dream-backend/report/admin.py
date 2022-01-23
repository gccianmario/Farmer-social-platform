from django.contrib import admin
from . import models


# This part deals with what can be seen from the admin administration portal
# add possibility in admin console to create new models
@admin.register(models.HarvestReport)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('firstName', 'lastName', 'date', 'id', 'status', 'slug', 'author')
    #prepopulated_fields = {'slug': ('title',), }


admin.site.register(models.CropCategory)
admin.site.register(models.Zone)
