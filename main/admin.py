from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Location)
admin.site.register(Image)
admin.site.register(Comments)
admin.site.register(Profile)