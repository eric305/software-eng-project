from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Book)
admin.site.register(models.Author)
admin.site.register(models.Review)
admin.site.register(models.TechValleyTimes)
admin.site.register(models.Comment)