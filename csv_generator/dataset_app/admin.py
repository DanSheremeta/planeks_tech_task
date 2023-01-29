from django.contrib import admin
from . import models


admin.site.register(models.Schema)
admin.site.register(models.Column)
