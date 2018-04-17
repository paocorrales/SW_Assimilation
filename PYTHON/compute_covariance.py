import numpy as np 

def compute_covariance(XENS,GridJ,GridI,Variable):

# Compute the ensemble spread (standard deviation) and mean.
    XSPREAD = np.std(XENS, 3)
    XMEAN = np.mean(XENS, 3)

    [NLats , NLons , NVars , EnsSize] = XENS.shape

    COVARIANCE = np.full((NLats,NLons,3), np.nan)

# Compute the spatial covariance between the variable 'Variable' at the
# location GridI, GridJ and all other grid points and variables.
    for ii in range(NLons):
        for jj in range(NLats):
            for k in range(NVars):
                tmp = np.cov(XENS[jj,ii,k,:], XENS[GridJ,GridI,Variable,:])
                COVARIANCE[jj,ii,k] = tmp[1, 0]
    
    return XSPREAD, XMEAN, COVARIANCE

# COVARIANCE(lat,lon,variable), COVARIANCE(i,j,k) is the covariance of
# variable k, at location i,j with variable Variable at location GridI, GridJ.