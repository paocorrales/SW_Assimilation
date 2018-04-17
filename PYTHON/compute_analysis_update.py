import numpy as np

def compute_analysis_update(COVARIANCE,LOCALIZATION,GridI,GridJ,Variable,d,R,NLats,NLons,NVars):

# Compute the analysis increment computed by a single observation.
# d = OBSMINUSGUES
# R = OBSERVATION_ERROR
    INCREMENT = np.full((NLats, NLons, NVars), np.nan)
# Compute the forecast (background) error at the observation location.
# Note that since we are assimilating only one observation, HPfHt is a scalar
    HPfHt = COVARIANCE[GridI,GridJ,Variable] # (H Pf Ht)

# Compute Kalman Gain. In this case Kalman Gain is computed independently
# for each model variable. In this way we avoid computing the full Pf
# matrix and computing H explicitely.
    KPHI = COVARIANCE[:,:,2]*LOCALIZATION/(R + HPfHt)  # PfH t * inv( H Pf Ht + R)
    KU   = COVARIANCE[:,:,0]*LOCALIZATION/(R + HPfHt)  # PfH t * inv( H Pf Ht + R)
    KV   = COVARIANCE[:,:,1]*LOCALIZATION/(R + HPfHt)  # PfH t * inv( H Pf Ht + R)

# We use the Kalman gain previously computed to compute the analysis
# increments in different variables. Note that in this case yo and h(x) are
# scalars because we are assimilating only 1 observation.
    INCREMENT[:,:,2] = KPHI*d   # KPHI * ( yo - h(x) )  PHI increment 
    INCREMENT[:,:,0] = KU  *d   # KU * ( yo - h(x) )  U   increment
    INCREMENT[:,:,1] = KV  *d   # KV * ( yo - h(x) )  V   increment
    
    return INCREMENT

