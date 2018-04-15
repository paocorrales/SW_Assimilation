# Juan Ruiz and Pierre Tandeo, 2015
#
# =============================================================================
#                        IMPORT LIBRARiES
# =============================================================================
import numpy as np

#==========================================================================
#                   SET EXPERIMENT PARAMETERS
#==========================================================================
#Select the observed variable.
Variable = 1       # U=1 , V=2 , PHY= 3  Variable at local point
#Indicate the location of the observation (integer)
GridJ = 30         #Location of grid point for which spatial covariances will be computed.
GridI = 25 
Time = 504         #Available times are 102, 504 and 900. 
EnsSize = 99       #From 2 to 999
#Select the localization scale
LOCALIZATION_SCALE = 1400e3  #Localization scale in meters.
OBSMINUSGUES = 1           #Difference between the first guess and the observation at 
                           #the observation location (same units as the
                           #assimilated observation)
OBSERVATION_ERROR = 1      #Observation error (same units as the assimilated observation)

#==========================================================================
#             OTHER PARAMETERS (For your own experiments)
#==========================================================================
NATURENAME = 'NATURE_MM15_ICOND4' 
EXPNAME = 'EXP_HUGEENS_15_METHOD3_ENS999_SKIP2_2_W6.0' 
NLats = 38     #Number of latitudes 
NLons = 48     #Number of longitudes
NVars = 3      #U,V and PHI (number of variables)
path_true = '../EXPERIMENTS/' + NATURENAME + '/' 
path_data = '../EXPERIMENTS/' + EXPNAME + '/' 
out_file = 'covariance_matrix.npz'

#==========================================================================
#                SET GRID AND GET CLIMATOLOGY
#==========================================================================
#Generate grid.
lon = np.linspace(0.0, 360-360//NLons, NLons) 
lat = np.linspace(-90, 90, NLats) 
[lon , lat] = np.meshgrid(lon,lat)

#Get longitude and latitude of the selected location.
LonI = lon[GridJ,GridI]
LatJ = lat[GridJ,GridI]

#Load XTMEAN and XTSTD from climatology.
#load([path_true '/climatology.mat'])  !!!!!

#==========================================================================
#                     READ ENSEMBLE
#==========================================================================
#XENS contains the data for all the model grid points, variables and
#ensemble members. XENS(lon,lat,variable,ensemble member)
#XB is a prefix, if XB is selected then the forecast (background) ensemble
#is read. If XA is selected the the analysis ensemble is read.

XENS = read_ensemble(path_data, 'XB', NLons, NLats, NVars, EnsSize, Time) 
  
#==========================================================================
#                    COMPUTE COVARIANCE
#==========================================================================
#XMEAN contain the ensemble mean XMEANS(lon,lat,variable)
#XSPREAD contains the ensemble spread XSPREAD(lon,lat,variable)
#COVARIANCE contains the covariance between the grid point GridJ, GridI,
#and Variable with all the other grid points for U, V and PHI.

[XMEAN,XSPREAD,COVARIANCE]=compute_covariance(XENS,GridJ,GridI,Variable) 

#COVARIANCE(lat,lon,variable), COVARIANCE(i,j,k) is the covariance of
#variable k, at location i,j with variable Variable at location GridI,
#GridJ.

#==========================================================================
#                     COMPUTE LOCALIZATION FUNCTION
#==========================================================================
#Localization is the localization function. Localizaed covariance is
#obtained by performing the Schur product between LOCALIZATION and the
#covariance.
[LOCALIZATION]=compute_localization(NLats,NLons,LonI,LatJ,lon,lat,LOCALIZATION_SCALE) 

#==========================================================================
#                     COMPUTE SINGLE OBS INCREMENT
#==========================================================================
#Increment is the correction introduced by a single observation located at
#GridI, GridJ and for variable Variable assuming yo-h(x) = OBSMINUSGUES and
#that the observational error is OBSERVATION_ERROR.
#Increment stores the correction for all variables and locations
#INCREMENT(lon,lat,variable).
[INCREMENT]=compute_analysis_update(COVARIANCE,LOCALIZATION,GridI,GridJ,Variable,OBSMINUSGUES,OBSERVATION_ERROR) 

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
plot_covariance(XSPREAD,COVARIANCE,LOCALIZATION,INCREMENT,lon,lat,LonI,LatJ,Variable) 




