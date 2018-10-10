import os
from django.contrib.gis.utils import LayerMapping
from .models import WorldBorder

world_mapping = {
    'fips': 'FIPS',
    'iso2': 'ISO2',
    'iso3': 'ISO3',
    'un': 'UN',
    'name': 'NAME',
    'area': 'AREA',
    'pop2005': 'POP2005',
    'region': 'REGION',
    'subregion': 'SUBREGION',
    'lon': 'LON',
    'lat': 'LAT',
    'mpoly': 'MULTIPOLYGON'
}

world_shp = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        'data', 'TM_WORLD_BORDERS-0.3.shp'
    ),
)


def run(verbose=True):
    """
    The transform keyword is set to False 
    because the data in the shapefile does not need to be converted -- it's already in WGS84 (SRID=4326)
    """
    lm = LayerMapping(WorldBorder, world_shp, world_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)
