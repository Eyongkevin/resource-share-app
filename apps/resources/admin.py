from django.contrib import admin
from apps.resources import models

# Register your models here.

admin.site.register(models.Tag)
admin.site.register(models.Category)
admin.site.register(models.Resources)
admin.site.register(models.Review)
