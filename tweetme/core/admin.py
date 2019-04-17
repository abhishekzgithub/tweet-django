from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Comment)
admin.site.register(models.Like)
admin.site.register(models.Tweet)
admin.site.register(models.Follow)
admin.site.register(models.HashTag)
admin.site.register(models.UserFollower)