import numpy as np
# Read an ensemble of forecast for a particular time.

def read_ensemble(path_data,prefix,NLons,NLats,NVars,EnsSize,Time):

    # Initialize the ensemble array XBENS(lat,lon,variable,ensemble member)
    XENS = np.full((NLats, NLons, NVars, EnsSize), np.nan)   #Analysis ensemble mean
    tstr = str(10000 + Time) 
    tstr = tstr[1::]
  
    if prefix == 'XA':
        folder = 'ANALYSIS' 
    elif prefix == 'XB':
        folder = 'GUES' 
  
    for iens in range(EnsSize):
        ensstr = str(1000+iens+1) 
        ensstr = ensstr[1::]

        file = path_data + folder + '/ENS/' + prefix + '_T' + tstr + '_M' + ensstr 
        
        for ivar in range(NVars):
            nfile = open(file,'rb') 
            f = np.fromfile(nfile, 'float32')[NLons*NLats*ivar:(1 + ivar)*NLons*NLats].reshape([NLats, NLons])
            XENS[:,:,ivar,iens] = np.flip(f, 0)
    return XENS

  