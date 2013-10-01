from django.http import HttpResponse, HttpResponseBadRequest
from django.contrib.gis.geos import Point
from djgeojson.serializers import Serializer as GeoJSONSerializer

from .models import Unit

def find_rocks(request):
    """
    Given a given lat/long pair, return the unit(s) surrounding it.
    """
    if request.is_ajax():
        lat = request.GET.get('lat', None)
        lon = request.GET.get('lon', None)
        
        if lat and lon:
            point = Point(float(lon), float(lat))
            units = Unit.objects.filter(geom__contains=point)
            geojson_data = GeoJSONSerializer().serialize(
                units, use_natural_keys=True) 

            return HttpResponse(geojson_data,
                mimetype='application/json')
    msg = "Bad request: not AJAX or no latlong pair present"
    return HttpResponseBadRequest(msg)