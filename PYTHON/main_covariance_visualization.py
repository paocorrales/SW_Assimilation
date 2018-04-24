# Juan Ruiz and Pierre Tandeo, 2015
#
# =============================================================================
#                        IMPORT LIBRARIES
# =============================================================================
import numpy as np
from read_ensemble import read_ensemble
from compute_covariance import compute_covariance
from compute_localization import compute_localization
from compute_analysis_update import compute_analysis_update
from plot_covariance import plot_covariance

#==============================================================================
#                   SET EXPERIMENT PARAMETERS
#==============================================================================
#Folder to save figures to
figfolder = '../FIG/Loc4000'
#Select the observed variable.
Variable = 0       # U=0 , V=1 , PHI= 2  Variable at local point
#Indicate the location of the observation (integer)
GridJ = 30         #Location of grid point for which spatial covariances will be computed.
GridI = 25
Time = 504         #Available times are 102, 504 and 900.
EnsSize = 99       #From 2 to 999
#Select the localization scale

LOCALIZATION_SCALE = 2000e3  #Localization scale in meters.
OBSMINUSGUES = 1           #Difference between the first guess and the \                          observation at the observation location (same \                          units as the assimilated observation)
OBSERVATION_ERROR = 1      #Observation error (same units as the assimilated \                          observation)


#==============================================================================
#             OTHER PARAMETERS (For your own experiments)
#==============================================================================
NATURENAME = 'NATURE_MM15_ICOND4'
EXPNAME = 'EXP_HUGEENS_15_METHOD3_ENS999_SKIP2_2_W6.0'
NLats = 38     #Number of latitudes
NLons = 48     #Number of longitudes
NVars = 3      #U,V and PHI (number of variables)
path_true = '../EXPERIMENTS/' + NATURENAME + '/'
path_data = '../EXPERIMENTS/' + EXPNAME + '/'
out_file = 'covariance_matrix.npz'

#==============================================================================
#                SET GRID AND GET CLIMATOLOGY
#==============================================================================
#Generate grid.
#lon = np.linspace(0.0, 360-360//NLons, NLons)
lon = np.linspace(0.0, 360, NLons)
lat = np.linspace(-90, 90, NLats)
[lon , lat] = np.meshgrid(lon,lat)

#Get longitude and latitude of the selected location.
LonI = lon[GridJ-1,GridI-1]
LatJ = lat[GridJ-1,GridI-1]

#Load XTMEAN and XTSTD from climatology.
CLIMATOLOGY = np.load(path_true + 'climatology.npz')
XTMEAN = CLIMATOLOGY['XTMEAN']
XTSTD = CLIMATOLOGY['XTSTD']

#==========================================================================
#                     READ ENSEMBLE
#==========================================================================
#XENS contains the data for all the model grid points, variables and
#ensemble members. XENS(lat,lon,variable,ensemble member)
#XB is a prefix, if XB is selected then the forecast (background) ensemble
#is read. If XA is selected the the analysis ensemble is read.
print('Reading ensemble data')
XENS = read_ensemble(path_data, 'XB', NLons, NLats, NVars, EnsSize, Time)

#==========================================================================
#                    COMPUTE COVARIANCE
#==========================================================================
#XMEAN contain the ensemble mean XMEANS(lon,lat,variable)
#XSPREAD contains the ensemble spread XSPREAD(lon,lat,variable)
#COVARIANCE contains the covariance between the grid point GridJ, GridI,
#and Variable with all the other grid points for U, V and PHI.
#ANOM is the  anomaly in the initial condition for U, V and PHI

print('Computing covariance')
[XMEAN, XSPREAD, ANOM, COVARIANCE] = compute_covariance(XTMEAN, XENS, GridJ, GridI, Variable)

#COVARIANCE(lat,lon,variable), COVARIANCE(i,j,k) is the covariance of
#variable k, at location i,j with variable Variable at location GridI,
#GridJ.

#==========================================================================
#                     COMPUTE LOCALIZATION FUNCTION
#==========================================================================
#Localization is the localization function. Localizaed covariance is
#obtained by performing the Schur product between LOCALIZATION and the
#covariance.
print('Computing localization')
LOCALIZATION = compute_localization(NLats, NLons, LonI, LatJ, lon, lat, LOCALIZATION_SCALE)

#==========================================================================
#                     COMPUTE SINGLE OBS INCREMENT
#==========================================================================
#Increment is the correction introduced by a single observation located at
#GridI, GridJ and for variable Variable assuming yo-h(x) = OBSMINUSGUES and
#that the observational error is OBSERVATION_ERROR.
#Increment stores the correction for all variables and locations
#INCREMENT(lon,lat,variable).
print('Computing analysis update')
INCREMENT = compute_analysis_update(COVARIANCE, LOCALIZATION, GridI, GridJ, Variable, OBSMINUSGUES, OBSERVATION_ERROR, NLats, NLons, NVars)

#INCREMENT(i,j,k) is the analysis increment for variable k at the location
#i,j due to the assimilation of an observation of variable Variable at
#GridI, GridJ.

#==========================================================================
#                        MAKE SOME PLOTS
#==========================================================================
#Plot the horizontal distribution of ensemble spread for U, V and PHI.
#Plot the horizontal distribution for the covariances between Variable and
#U, Variable and V and Variable and PHI (Variable can be U, V or PHI).
#Plot the horizontal distribution of covariances in the same plot using
#shaded and vectors.
#Plot the horizontal distribution of localized covariances. This figures
#can be compared with the non-localized covariances to understand the
#effect of localization.
#Plot the analysis INCREMENT produced by a single observation at the
#location LonI, LatJ and for the selected variable.
print('Making plots')
plot_covariance(figfolder, XMEAN, ANOM, XSPREAD, COVARIANCE, LOCALIZATION, INCREMENT, lon, lat, LonI, LatJ, Variable)
