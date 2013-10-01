from django.contrib.gis import admin
from .models import Unit

admin.site.register(Unit, admin.GeoModelAdmin)
