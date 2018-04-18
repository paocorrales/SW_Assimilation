from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
        


def plot_covariance(XMEAN,ANOM,XSPREAD,COVARIANCE,LOCALIZATION,INCREMENT,lon,lat,LonI,LatJ,Variable):
 
# Palette
    seq = plt.get_cmap('YlGn')
    div = plt.get_cmap('PRGn')
    
    if Variable == 0:
        VAR='U'
    elif Variable == 1:
        VAR='V'
    elif Variable == 2:
        VAR='PHI'


#==============================================================================
#                      INITIAL 
#==============================================================================

    
    fig, ax = plt.subplots(figsize=(16, 12))
    map = Basemap(projection='mill',lon_0=180)
    map.drawcoastlines()
    map.drawparallels(np.arange(-80,90,20),labels=[1,0,0,0], fontsize=10)
    map.drawmeridians(np.arange(map.lonmin,map.lonmax+30,40),labels=[0,0,0,1], fontsize=10)
    x, y = map(lon, lat)
    Lon, Lat = map(LonI, LatJ)
    scale = np.amax(np.abs(ANOM[:, :, 2]))/5
    levels = np.array([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])*scale
    cf = ax.contourf(x, y, ANOM[:, :, 2], cmap = div)
    ax.contour(cf, colors='k', linewidths=0.5)
    ax.plot(Lon, Lat, marker='.', markersize=25, color="red")
    ax.quiver(x, y, XMEAN[:, :, 0], XMEAN[:, :, 1], width = 0.001) 
    ax.set_ylabel('Lat', labelpad = 30)
    ax.set(title='PHI (anomaly, shaded), U;V (mean, vectors)')
    map.colorbar(cf, location='right')
    plt.savefig('../FIG/' + 'Initial.png')
    plt.show()

#==============================================================================
#                         U VARIANCE
#==============================================================================
    
    fig, ax = plt.subplots(figsize=(16, 12))
    map = Basemap(projection='mill',lon_0=180)
    map.drawcoastlines()
    map.drawparallels(np.arange(-80,90,20),labels=[1,0,0,0], fontsize=10)
    map.drawmeridians(np.arange(map.lonmin,map.lonmax+30,40),labels=[0,0,0,1], fontsize=10)
    x, y = map(lon, lat)
    cf = ax.contourf(x, y, XSPREAD[:, :, 0], cmap = seq)
    map.colorbar(cf, location='right')
    ax.contour(cf, colors='k', linewidths=0.5)
    ax.set_xlabel('Lon', labelpad = 20)
    ax.set_ylabel('Lat', labelpad = 30)
    ax.set(title='U Variance (m/s)')
    plt.savefig('../FIG/U_Variance.png')
    
#==============================================================================
#                        V VARIANCE
#==============================================================================
    
    fig, ax = plt.subplots(figsize=(16, 12))
    map = Basemap(projection='mill',lon_0=180)
    map.drawcoastlines()
    map.drawparallels(np.arange(-80,90,20),labels=[1,0,0,0], fontsize=10)
    map.drawmeridians(np.arange(map.lonmin,map.lonmax+30,40),labels=[0,0,0,1], fontsize=10)
    x, y = map(lon, lat)
    cf = ax.contourf(x, y, XSPREAD[:, :, 1], cmap = seq)
    ax.contour(cf, colors='k', linewidths=0.5)
    ax.set_xlabel('Lon', labelpad = 20)
    ax.set_ylabel('Lat', labelpad = 30)
    ax.set(title='V Variance (m/s)')
    map.colorbar(cf, location='right')
    plt.savefig('../FIG/V_Variance.png')
    
#==============================================================================
#                        PHI VARIANCE
#==============================================================================
    
    fig, ax = plt.subplots(figsize=(16, 12))
    map = Basemap(projection='mill',lon_0=180)
    map.drawcoastlines()
    map.drawparallels(np.arange(-80,90,20),labels=[1,0,0,0], fontsize=10)
    map.drawmeridians(np.arange(map.lonmin,map.lonmax+30,40),labels=[0,0,0,1], fontsize=10)
    x, y = map(lon, lat)
    cf = ax.contourf(x, y, XSPREAD[:, :, 2], cmap = seq)
    ax.contour(cf, colors='k', linewidths=0.5)
    ax.set_xlabel('Lon', labelpad = 20)
    ax.set_ylabel('Lat', labelpad = 30)
    ax.set(title='PHI Variance (m)')
    map.colorbar(cf, location='right')
    plt.savefig('../FIG/PHI_Variance.png')
    
    
#==============================================================================
#                          VAR - U COVARIANCE
#==============================================================================
    
    fig, ax = plt.subplots(figsize=(16, 12))
    map = Basemap(projection='mill',lon_0=180)
    map.drawcoastlines()
    map.drawparallels(np.arange(-80,90,20),labels=[1,0,0,0], fontsize=10)
    map.drawmeridians(np.arange(map.lonmin,map.lonmax+30,40),labels=[0,0,0,1], fontsize=10)
    x, y = map(lon, lat)
    Lon, Lat = map(LonI, LatJ)
    scale = np.amax(np.abs(COVARIANCE[:, :, 0]))/5
    levels = np.array([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])*scale
    cf = ax.contourf(x, y, COVARIANCE[:, :, 0], cmap = div, levels = levels)
    ax.contour(cf, colors='k', linewidths=0.5)
    ax.plot(Lon, Lat, marker='.', markersize=25, color="red")
    ax.set_xlabel('Lon', labelpad = 20)
    ax.set_ylabel('Lat', labelpad = 30)
    ax.set(title='Covariance '+ VAR + '-U')
    map.colorbar(cf, location='right')
    plt.savefig('../FIG/' + VAR + '-U_Variance.png')
    
    
#==============================================================================
#                           VAR - V COVARIANCE
#==============================================================================
    
    fig, ax = plt.subplots(figsize=(16, 12))
    map = Basemap(projection='mill',lon_0=180)
    map.drawcoastlines()
    map.drawparallels(np.arange(-80,90,20),labels=[1,0,0,0], fontsize=10)
    map.drawmeridians(np.arange(map.lonmin,map.lonmax+30,40),labels=[0,0,0,1], fontsize=10)
    x, y = map(lon, lat)
    Lon, Lat = map(LonI, LatJ)
    scale = np.amax(np.abs(COVARIANCE[:, :, 1]))/5
    levels = np.array([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])*scale
    cf = ax.contourf(x, y, COVARIANCE[:, :, 1], cmap = div, levels = levels)
    ax.contour(cf, colors='k', linewidths=0.5)
    ax.plot(Lon, Lat, marker='.', markersize=25, color="red")
    ax.set_xlabel('Lon', labelpad = 20)
    ax.set_ylabel('Lat', labelpad = 30)
    ax.set(title='Covariance '+ VAR + '-V')
    map.colorbar(cf, location='right')
    plt.savefig('../FIG/' + VAR + '-V_Variance.png')
    
    
#==============================================================================
#                         VAR - PHI COVARIANCE
#==============================================================================
    
    fig, ax = plt.subplots(figsize=(16, 12))
    map = Basemap(projection='mill',lon_0=180)
    map.drawcoastlines()
    map.drawparallels(np.arange(-80,90,20),labels=[1,0,0,0], fontsize=10)
    map.drawmeridians(np.arange(map.lonmin,map.lonmax+30,40),labels=[0,0,0,1], fontsize=10)
    x, y = map(lon, lat)
    Lon, Lat = map(LonI, LatJ)
    scale = np.amax(np.abs(COVARIANCE[:, :, 2]))/5
    levels = np.array([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])*scale
    cf = ax.contourf(x, y, COVARIANCE[:, :, 2], cmap = div, levels = levels)
    ax.contour(cf, colors='k', linewidths=0.5)
    ax.plot(Lon, Lat, marker='.', markersize=25, color="red")
    ax.set_xlabel('Lon', labelpad = 20)
    ax.set_ylabel('Lat', labelpad = 30)
    ax.set(title='Covariance '+ VAR + '-PHI')
    map.colorbar(cf, location='right')
    plt.savefig('../FIG/' + VAR + '-PHI_Variance.png')
    
#==============================================================================
#                 VAR - PHI , VAR - U , VAR - V COVARANICE
#==============================================================================
    
    fig, ax = plt.subplots(figsize=(16, 12))
    map = Basemap(projection='mill',lon_0=180)
    map.drawcoastlines()
    map.drawparallels(np.arange(-80,90,20),labels=[1,0,0,0], fontsize=10)
    map.drawmeridians(np.arange(map.lonmin,map.lonmax+30,40),labels=[0,0,0,1], fontsize=10)
    x, y = map(lon, lat)
    Lon, Lat = map(LonI, LatJ)
    scale = np.amax(np.abs(COVARIANCE[:, :, 2]))/5
    levels = np.array([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])*scale
    cf = ax.contourf(x, y, COVARIANCE[:, :, 2], cmap = div, levels = levels)
    ax.contour(cf, colors='k', linewidths=0.5)
    ax.plot(Lon, Lat, marker='.', markersize=25, color="red")
    ax.quiver(x, y, COVARIANCE[:, :, 0], COVARIANCE[:, :, 1], 
                  units = 'height', scale = 0.6, width = 0.002)
    ax.set_ylabel('Lat', labelpad = 30)
    ax.set(title='Covariance '+ VAR + '-PHI (shaded), ' + VAR + '-U ; ' + VAR + '-V (vectors)')
    map.colorbar(cf, location='right')
    plt.savefig('../FIG/' + VAR + '-PHI_Covariance_Vectors.png')
    plt.show()
    
    
#==============================================================================
#                        VAR - U LOCALIZED COVARIANCE
#==============================================================================
    
    fig, ax = plt.subplots(figsize=(16, 12))
    map = Basemap(projection='mill',lon_0=180)
    map.drawcoastlines()
    map.drawparallels(np.arange(-80,90,20),labels=[1,0,0,0], fontsize=10)
    map.drawmeridians(np.arange(map.lonmin,map.lonmax+30,40),labels=[0,0,0,1], fontsize=10)
    x, y = map(lon, lat)
    Lon, Lat = map(LonI, LatJ)
    scale = np.amax(np.abs(COVARIANCE[:, :, 0]))/5
    levels = np.array([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])*scale
    cf = ax.contourf(x, y, COVARIANCE[:, :, 0]*LOCALIZATION, cmap = div, levels = levels)
    ax.contour(cf, colors='k', linewidths=0.5)
    ax.plot(Lon, Lat, marker='.', markersize=25, color="red")
    ax.set_ylabel('Lat', labelpad = 30)
    ax.set(title='Localized covariance '+ VAR + '-U')
    map.colorbar(cf, location='right')
    plt.savefig('../FIG/' + VAR + '-U_Localized_Covariance.png')
    plt.show()
    
    
#==============================================================================
#                       VAR - V LOCALIZED COVARIANCE
#==============================================================================
    
    fig, ax = plt.subplots(figsize=(16, 12))
    map = Basemap(projection='mill',lon_0=180)
    map.drawcoastlines()
    map.drawparallels(np.arange(-80,90,20),labels=[1,0,0,0], fontsize=10)
    map.drawmeridians(np.arange(map.lonmin,map.lonmax+30,40),labels=[0,0,0,1], fontsize=10)
    x, y = map(lon, lat)
    Lon, Lat = map(LonI, LatJ)
    scale = np.amax(np.abs(COVARIANCE[:, :, 1]))/5
    levels = np.array([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])*scale
    cf = ax.contourf(x, y, COVARIANCE[:, :, 1]*LOCALIZATION, cmap = div, levels = levels)
    ax.contour(cf, colors='k', linewidths=0.5)
    ax.plot(Lon, Lat, marker='.', markersize=25, color="red")
    ax.set_ylabel('Lat', labelpad = 30)
    ax.set(title='Localized covariance '+ VAR + '-V')
    map.colorbar(cf, location='right')
    plt.savefig('../FIG/' + VAR + '-V_Localized_Covariance.png')
    plt.show()
    
    
#==============================================================================
#                     VAR - PHI LOCALIZED COVARIANCE
#==============================================================================
    
    fig, ax = plt.subplots(figsize=(16, 12))
    map = Basemap(projection='mill',lon_0=180)
    map.drawcoastlines()
    map.drawparallels(np.arange(-80,90,20),labels=[1,0,0,0], fontsize=10)
    map.drawmeridians(np.arange(map.lonmin,map.lonmax+30,40),labels=[0,0,0,1], fontsize=10)
    x, y = map(lon, lat)
    Lon, Lat = map(LonI, LatJ)
    scale = np.amax(np.abs(COVARIANCE[:, :, 2]))/5
    levels = np.array([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])*scale
    cf = ax.contourf(x, y, COVARIANCE[:, :, 2]*LOCALIZATION, cmap = div, levels = levels)
    ax.contour(cf, colors='k', linewidths=0.5)
    ax.plot(Lon, Lat, marker='.', markersize=25, color="red")
    ax.set_ylabel('Lat', labelpad = 30)
    ax.set(title='Localized covariance '+ VAR + '-PHI')
    map.colorbar(cf, location='right')
    plt.savefig('../FIG/' + VAR + '-PHI_Localized_Covariance.png')
    plt.show()
    
    
#==============================================================================
#               VAR - PHI , VAR - U , VAR - V LOCALIZED COVARANICE
#==============================================================================
    
    fig, ax = plt.subplots(figsize=(16, 12))
    map = Basemap(projection='mill',lon_0=180)
    map.drawcoastlines()
    map.drawparallels(np.arange(-80,90,20),labels=[1,0,0,0], fontsize=10)
    map.drawmeridians(np.arange(map.lonmin,map.lonmax+30,40),labels=[0,0,0,1], fontsize=10)
    x, y = map(lon, lat)
    Lon, Lat = map(LonI, LatJ)
    scale = np.amax(np.abs(COVARIANCE[:, :, 2]))/5
    levels = np.array([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])*scale
    cf = ax.contourf(x, y, COVARIANCE[:, :, 2]*LOCALIZATION, cmap = div, levels = levels)
    ax.contour(cf, colors='k', linewidths=0.5)
    ax.plot(Lon, Lat, marker='.', markersize=25, color="red")
    ax.quiver(x, y, COVARIANCE[:, :, 0]*LOCALIZATION, COVARIANCE[:, :, 1]*LOCALIZATION, 
                  units = 'height', scale = 0.6, width = 0.002)
    ax.set_ylabel('Lat', labelpad = 30)
    ax.set(title='Localized covariance '+ VAR + '-PHI (shaded), ' + VAR + '-U ; ' + VAR + '-V (vectors)')
    map.colorbar(cf, location='right')
    plt.savefig('../FIG/' + VAR + '-PHI_Localized_Covariance_Vectors.png')
    plt.show()
    
    
#==============================================================================
#                 SINGLE OBSERVATION ANALYSIS INCREMENT 
#==============================================================================
    
    fig, ax = plt.subplots(figsize=(16, 12))
    map = Basemap(projection='mill',lon_0=180)
    map.drawcoastlines()
    map.drawparallels(np.arange(-80,90,20),labels=[1,0,0,0], fontsize=10)
    map.drawmeridians(np.arange(map.lonmin,map.lonmax+30,40),labels=[0,0,0,1], fontsize=10)
    x, y = map(lon, lat)
    Lon, Lat = map(LonI, LatJ)
    scale = np.amax(np.abs(INCREMENT[:, :, 2]))/5
    levels = np.array([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])*scale
    cf = ax.contourf(x, y, INCREMENT[:, :, 2], cmap = div, levels = levels)
    ax.contour(cf, colors='k', linewidths=0.5)
    ax.plot(Lon, Lat, marker='.', markersize=25, color="red")
    ax.quiver(x, y, INCREMENT[:, :, 0], INCREMENT[:, :, 1], 
                  units = 'height', scale = 0.6, width = 0.002)
    ax.set_ylabel('Lat', labelpad = 30)
    ax.set(title='Analysis Increment in PHI (shaded), U;V (vectors)')
    map.colorbar(cf, location='right')
    plt.savefig('../FIG/' + 'Analysis_Increment_PHI_Vectors.png')
    plt.show()
    

#==============================================================================
#                      SINGLE LOCALIZATION
#==============================================================================
    
    fig, ax = plt.subplots(figsize=(16, 12))
    map = Basemap(projection='mill',lon_0=180)
    map.drawcoastlines()
    map.drawparallels(np.arange(-80,90,20),labels=[1,0,0,0], fontsize=10)
    map.drawmeridians(np.arange(map.lonmin,map.lonmax+30,40),labels=[0,0,0,1], fontsize=10)
    x, y = map(lon, lat)
    Lon, Lat = map(LonI, LatJ)
    scale = np.amax(np.abs(LOCALIZATION))/5
    levels = np.array([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])*scale
    cf = ax.contourf(x, y, LOCALIZATION, cmap = div, levels = levels)
    ax.contour(cf, colors='k', linewidths=0.5)
    ax.plot(Lon, Lat, marker='.', markersize=25, color="red")
    ax.set_ylabel('Lat', labelpad = 30)
    ax.set(title='Localization function')
    map.colorbar(cf, location='right')
    plt.savefig('../FIG/' + 'Localization_function.png')
    plt.show()



