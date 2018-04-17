import numpy as np 

def compute_covariance(XENS,GridJ,GridI,Variable):

# Compute the ensemble spread (standard deviation) and mean.
    XSPREAD = np.std(XENS, 3)
    XMEAN = np.mean(XENS, 3)

    [NLats , NLons , NVars , EnsSize] = XENS.shape

    COVARIANCE = np.full((NLats,NLons,NVars), np.nan)

# Compute the spatial covariance between the variable 'Variable' at the
# location GridI, GridJ and all other grid points and variables.
    for k in range(NVars):
        for ii in range(NLons):
            for jj in range(NLats):
          
                tmp = np.cov(XENS[jj,ii,k,:], XENS[GridJ-1,GridI-1,Variable,:])
                COVARIANCE[jj,ii,k] = tmp[1, 0]
    
    return XMEAN, XSPREAD, COVARIANCE

# COVARIANCE(lat,lon,variable), COVARIANCE(i,j,k) is the covariance of
# variable k, at location i,j with variable Variable at location GridI, GridJ.