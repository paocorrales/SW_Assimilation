import numpy as np
from distll_fun import distll_fun

def compute_localization(NLats,NLons,LonI,LatJ,lon,lat,LOCALIZATION_SCALE):
    LOCALIZATION=np.zeros((NLats,NLons))
    
    for jj in range(NLats):
        for ii in range(NLons):
            dist_m = distll_fun(LonI,LatJ,lon(jj,ii),lat(jj,ii))
            LOCALIZATION[jj,ii] = np.exp(-0.5*((dist_m*dist_m)/(LOCALIZATION_SCALE*LOCALIZATION_SCALE)))
    
    return LOCALIZATION