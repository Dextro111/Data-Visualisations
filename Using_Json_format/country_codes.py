from pygal_maps_world.maps import COUNTRIES

def get_country_code(country_name):
    """Return the Pygal 2-digit country code for given country"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    #   if Country not found return None
    return None

#print(get_country_code("Nigeria"))
#print(get_country_code("Ghana"))
#print(get_country_code("Portugal"))