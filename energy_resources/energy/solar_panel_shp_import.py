from .layermapping import CustomLayerMapping
from .models import SolarPanel

mapping = {'owner_name': 'owner_name',
           'manufacturer': 'manuf',
           'note': 'note',
           'entity': 'entity',
           'canton': 'canton',
           'city': 'city',
           'zone': 'zone',
           'altitude': 'altitude',
           'panel_angle': 'panel_angl',
           'field_strength': 'field_stre'}


def import_shapefile_sp(filepath, user_req):
    global user
    user = user_req
    lm = CustomLayerMapping(SolarPanel, filepath, mapping, last_user=user_req)
    lm.save(verbose=True)
    user = None