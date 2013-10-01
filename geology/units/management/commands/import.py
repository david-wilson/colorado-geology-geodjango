import os
import units

from django.core.management.base import BaseCommand, CommandError
from django.contrib.gis.utils import LayerMapping

from units.models import Unit, unit_mapping

class Command(BaseCommand):
    help = 'Loads geologic unit data from app data directory'

    def handle(self, *args, **options):
        unit_shp = os.path.abspath(os.path.join(os.path.join(os.path.dirname(units.__file__), 'data/cogeol.kml')))

        lm = LayerMapping(Unit, unit_shp, unit_mapping, 
            transform=False, encoding='iso-8859-1') 
        lm.save(strict=True, verbose=True)
