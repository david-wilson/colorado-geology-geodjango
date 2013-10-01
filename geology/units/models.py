from django.contrib.gis.db import models

unit_srid = 4326

class Unit(models.Model):
    name = models.CharField(max_length=1024)
    description = models.CharField(max_length=1024)
    geom = models.GeometryField(srid=unit_srid)
    objects = models.GeoManager()

    def __unicode_(self):
        return "Unit %s" % (name)

# Auto-generated `LayerMapping` dictionary for Unit model
unit_mapping = {
    'name' : 'Name',
    'description' : 'Description',
    'geom' : 'UNKNOWN',
}
