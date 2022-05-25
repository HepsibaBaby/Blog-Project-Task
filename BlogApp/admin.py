from django.contrib import admin

# Register your models here.
from BlogApp import models

admin.site.register(models.Login)
admin.site.register(models.Profile)
