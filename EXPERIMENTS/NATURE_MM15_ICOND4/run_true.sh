#=============== BASIC CONFIGURATION ======================

GPATH=`pwd`/../
MODPATH="${GPATH}/TRUE/"
EXPPATH="${GPATH}/EXPERIMENTS/"
SCRPATH="${GPATH}/scripts/"
CONFIGPATH="${GPATH}/CONFIG/"

ulimit -s unlimited
#================ EXPERT CONFIGURATION =====================

#RUN TYPE
ICOND=4   # Define different idealized model settings (view init.f for details)

#TOPOGRAPHY PARAMETERS
FTOPO=.TRUE.     #Activate topography forcing. 
MOUNTA=1500.0    #Mountain height
MOUNTW=1.5e5     #Mountain width
RADIUS=0.523     #Mountain radius (for ICOND = 5 only)

#MODEL CONSTANTS
DT=150.0        #TIME STEP IN SECONDS
RADFORCE=.TRUE. #Activate radiative forcing.
TAUF=86400.0    #Radiative forcing time scale.
FORCED=.FALSE.  #Momentum forcing.

#MODEL RESOLUTION CONSTANTS (LOWRES, MEDRES , HIRES)
MM=15       # 15 , 42 ,  63
NN=15       # 15 , 42 ,  63
KK=30       # 30 , 42 ,  63
NLAT=38     # 38 , 64 ,  96
NLON=48     # 48 ,128 , 192

RADFORCE=.TRUE. 

#EXPERIMENT SETTINGS
TOTALEXPTIME=12000.0 #Total experiment time in hours.
WINDOWL=6.0         #Assimilation frequency.

#OBSERVATION ERRORS
UERROR=1.0
VERROR=1.0
PERROR=10.0
DERROR=1.0e-8
ZERROR=1.0e-6

#================ END CONFIGURATION =====================

EXPNAME=NATURE_MM${MM}_ICOND${ICOND}

#Build the code.
cd $MODPATH
make clean

cp $CONFIGPATH/* .


#================ APPLY CONFIGURATION =====================

sed -i 's/@DT@/'${DT}'/g'  ./input.f
sed -i 's/@FORCED@/'${FORCED}'/g'  ./input.f
sed -i 's/@FTOPO@/'${FTOPO}'/g'  ./input.f
sed -i 's/@ICOND@/'${ICOND}'/g'  ./input.f

sed -i 's/@FTOPO@/'${FTOPO}'/g'  ./init.f
sed -i 's/@MOUNTA@/'${MOUNTA}'/g'  ./init.f
sed -i 's/@MOUNTW@/'${MOUNTW}'/g'  ./init.f
sed -i 's/@RADIUS@/'${RADIUS}'/g'  ./init.f

sed -i 's/@MM@/'${MM}'/g'                      ./params.i
sed -i 's/@NN@/'${NN}'/g'                      ./params.i
sed -i 's/@KK@/'${KK}'/g'                      ./params.i
sed -i 's/@NLAT@/'${NLAT}'/g'                  ./params.i
sed -i 's/@NLON@/'${NLON}'/g'                  ./params.i
sed -i 's/@RADFORCE@/'${RADFORCE}'/g'          ./params.i
sed -i 's/@TAUF@/'${TAUF}'/g'                  ./params.i
sed -i 's/@TOTALEXPTIME@/'${TOTALEXPTIME}'/g'  ./params.i
sed -i 's/@WINDOWL@/'${WINDOWL}'/g'            ./params.i

sed -i 's/@UERROR@/'${UERROR}'/g'  ./params.i
sed -i 's/@VERROR@/'${VERROR}'/g'  ./params.i
sed -i 's/@PERROR@/'${PERROR}'/g'  ./params.i
sed -i 's/@DERROR@/'${DERROR}'/g'  ./params.i
sed -i 's/@ZERROR@/'${ZERROR}'/g'  ./params.i

#================ END CONFIGURATION =====================

#Select the parameters according to the resolution
cp ./params.$RESOLUTION ./params.i
make 

#Set the experiment
cd $EXPPATH
rm -fr $EXPNAME

mkdir ./${EXPNAME}

cd $EXPNAME

#COPY THE SCRIPT THAT GENERATES THE DATA
cp $SCRPATH/run_true.sh ./

#LINK MODEL AND OBSERVATIONS
cp  $MODPATH/true ./

#CREATE DIRECTORY TREE
mkdir ./OBS/
mkdir ./STATE/

./true

#COPY RESULTS
mv XT* ./STATE/
mv XO* ./OBS/

