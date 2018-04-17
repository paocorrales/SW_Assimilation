import numpy as np

def distll_fun(alon,alat,blon,blat):
    #pi=3.14159
    re=6371.3e3

    lon1 = alon * np.pi/180
    lon2 = blon * np.pi/180
    lat1 = alat * np.pi/180
    lat2 = blat * np.pi/180

    cosd = np.sin(lat1)*np.sin(lat2) + np.cos(lat1)*np.cos(lat2)*np.cos(lon2-lon1)
    cosd = min(1.0, cosd)
    cosd = max(-1.0, cosd)
    
    dist = np.arccos(cosd) * re

    return dist

