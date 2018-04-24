import os
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.basemap import Basemap

def set_env_map(fs, lon, lat, LonI, LatJ, marker=False):

    fig, ax = plt.subplots(figsize=(14, 10))
    m = Basemap(projection='mill', lon_0=180)
    m.drawcoastlines()
    m.drawparallels(np.arange(-80, 90, 20), labels=[1, 0, 0, 0], fontsize=fs)
    m.drawmeridians(np.arange(m.lonmin, m.lonmax+30, 40), labels=[0, 0, 0, 1], fontsize=fs)
    x, y = m(lon, lat)
    Lon, Lat = m(LonI, LatJ)
    #ax.set_xlabel('Lon', labelpad=20, fontsize=fs)
    #ax.set_ylabel('Lat', labelpad=30, fontsize=fs)
    if marker:
        ax.plot(Lon, Lat, marker='.', markersize=25, color="red")
    return fig, ax, m, x, y

def plot_covariance(outdir, XMEAN, ANOM, XSPREAD, COVARIANCE, LOCALIZATION, INCREMENT, lon, lat, LonI, LatJ, Variable):

    #Create output directory
    if not os.path.exists(outdir):
        os.makedirs(outdir)

    # Palette
    seq = plt.get_cmap('YlGn')
    div = plt.get_cmap('PRGn')

    if Variable == 0:
        VAR = 'U'
        wscale = 0.05
        wkey = 0.03
    elif Variable == 1:
        VAR ='V'
        wscale = 0.05
        wkey = 0.03
    elif Variable == 2:
        VAR ='PHI'
        wscale = 0.5
        wkey = 0.3

    #Graphic parameters
    fstitle = 22
    fs = 20


#==============================================================================
#                        INITIAL
#==============================================================================

    fig, ax, m, x, y = set_env_map(fs, lon, lat, LonI, LatJ, marker=True)
    cf = ax.contourf(x, y, ANOM[:, :, 2], cmap=div, levels=np.linspace(-300, 300, 13))
    #cf = ax.contourf(lon, lat, ANOM[:, :, 2], projection='mill', cmap=div, levels=np.linspace(-300, 300, 13))
    ax.contour(cf, colors='k', linewidths=0.5)
    cbar = m.colorbar(cf, location='right')
    cbar.ax.tick_params(labelsize=fs)
    #ax.quiver(x, y, XMEAN[:, :, 0], XMEAN[:, :, 1], width=0.001)
    q = ax.quiver(x[::2,::2], y[::2,::2], XMEAN[::2, ::2, 0], XMEAN[::2, ::2, 1], scale=60, units='inches', scale_units='inches')
    ax.quiverkey(q, 0.90, 0.1, 30, r'30 $\frac{m}{s}$', labelpos='E', coordinates='figure')
    ax.set_title('PHI (anomaly, shaded), U;V (mean, vectors)', fontsize=fstitle)
    plt.savefig(outdir + '/Initial.png', bbox_inches='tight')
    plt.close()

#==============================================================================
#                         U SPREAD
#==============================================================================
    print('    Spread')
    fig, ax, m, x, y = set_env_map(fs, lon, lat, LonI, LatJ)
    cf = ax.contourf(x, y, XSPREAD[:, :, 0], cmap=seq)
    ax.contour(cf, colors='k', linewidths=0.5)
    cbar = m.colorbar(cf, location='right')
    cbar.ax.tick_params(labelsize=fs)
    ax.set_title('U Spread (m/s)', fontsize=fstitle)
    plt.savefig(outdir + '/U_Spread.png', bbox_inches='tight')
    plt.close()

#==============================================================================
#                        V SPREAD
#==============================================================================

    fig, ax, m, x, y = set_env_map(fs, lon, lat, LonI, LatJ)
    cf = ax.contourf(x, y, XSPREAD[:, :, 1], cmap=seq)
    ax.contour(cf, colors='k', linewidths=0.5)
    cbar = m.colorbar(cf, location='right')
    cbar.ax.tick_params(labelsize=fs)
    ax.set_title('V Spread (m/s)', fontsize=fstitle)
    plt.savefig(outdir + '/V_Spread.png', bbox_inches='tight')
    plt.close()

#==============================================================================
#                        PHI SPREAD
#==============================================================================

    fig, ax, m, x, y = set_env_map(fs, lon, lat, LonI, LatJ)
    cf = ax.contourf(x, y, XSPREAD[:, :, 2], cmap=seq)
    ax.contour(cf, colors='k', linewidths=0.5)
    cbar = m.colorbar(cf, location='right')
    cbar.ax.tick_params(labelsize=fs)
    ax.set_title('PHI Spread (m/s)', fontsize=fstitle)
    plt.savefig(outdir + '/PHI_Spread.png', bbox_inches='tight')
    plt.close()

#==============================================================================
#                          VAR - U COVARIANCE
#==============================================================================
    print('    Covariance')
    fig, ax, m, x, y = set_env_map(fs, lon, lat, LonI, LatJ, marker=True)
    scale = np.amax(np.abs(COVARIANCE[:, :, 0]))/5
    levels = np.array([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])*scale
    cf = ax.contourf(x, y, COVARIANCE[:, :, 0], cmap=div, levels = levels)
    ax.contour(cf, colors='k', linewidths=0.5)
    cbar = m.colorbar(cf, location='right')
    cbar.ax.tick_params(labelsize=fs)
    ax.set_title('Covariance '+ VAR + '-U', fontsize=fstitle)
    plt.savefig(outdir + '/' + VAR + '-U_Covariance.png', bbox_inches='tight')

#==============================================================================
#                           VAR - V COVARIANCE
#==============================================================================

    fig, ax, m, x, y = set_env_map(fs, lon, lat, LonI, LatJ, marker=True)
    scale = np.amax(np.abs(COVARIANCE[:, :, 1]))/5
    levels = np.array([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])*scale
    cf = ax.contourf(x, y, COVARIANCE[:, :, 1], cmap=div, levels = levels)
    ax.contour(cf, colors='k', linewidths=0.5)
    cbar = m.colorbar(cf, location='right')
    cbar.ax.tick_params(labelsize=fs)
    ax.set_title('Covariance '+ VAR + '-V', fontsize=fstitle)
    plt.savefig(outdir + '/' + VAR + '-V_Covariance.png', bbox_inches='tight')

#==============================================================================
#                         VAR - PHI COVARIANCE
#==============================================================================
    fig, ax, m, x, y = set_env_map(fs, lon, lat, LonI, LatJ, marker=True)
    scale = np.amax(np.abs(COVARIANCE[:, :, 2]))/5
    levels = np.array([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])*scale
    cf = ax.contourf(x, y, COVARIANCE[:, :, 2], cmap=div, levels = levels)
    ax.contour(cf, colors='k', linewidths=0.5)
    cbar = m.colorbar(cf, location='right')
    cbar.ax.tick_params(labelsize=fs)
    ax.set_title('Covariance '+ VAR + '-PHI', fontsize=fstitle)
    plt.savefig(outdir + '/' + VAR + '-PHI_Covariance.png', bbox_inches='tight')

#==============================================================================
#                 VAR - PHI , VAR - U , VAR - V COVARANICE
#==============================================================================
    fig, ax, m, x, y = set_env_map(fs, lon, lat, LonI, LatJ, marker=True)
    scale = np.amax(np.abs(COVARIANCE[:, :, 2]))/5
    levels = np.array([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])*scale
    cf = ax.contourf(x, y, COVARIANCE[:, :, 2], cmap=div, levels=levels)
    ax.contour(cf, colors='k', linewidths=0.5)
    cbar = m.colorbar(cf, location='right')
    cbar.ax.tick_params(labelsize=fs)
    #ax.quiver(x, y, COVARIANCE[:, :, 0], COVARIANCE[:, :, 1], units='height', scale=0.6, width=0.002)
    q = ax.quiver(x, y, COVARIANCE[:, :, 0], COVARIANCE[:, :, 1], scale=wscale, units='inches', scale_units='inches')
    ax.quiverkey(q, 0.90, 0.1, wkey, wkey, labelpos='E', coordinates='figure')
    ax.set_title('Covariance '+ VAR + '-PHI (shaded), ' + VAR + '-U ; ' + VAR + '-V (vectors)', fontsize=fstitle)
    plt.savefig(outdir + '/' + VAR + '-PHI_Covariance_Vectors.png', bbox_inches='tight')
    plt.close()

#==============================================================================
#                        VAR - U LOCALIZED COVARIANCE
#==============================================================================
    print('    Localized covariance')
    fig, ax, m, x, y = set_env_map(fs, lon, lat, LonI, LatJ, marker=True)
    scale = np.amax(np.abs(COVARIANCE[:, :, 0]))/5
    levels = np.array([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])*scale
    cf = ax.contourf(x, y, COVARIANCE[:, :, 0]*LOCALIZATION, cmap=div, levels=levels)
    ax.contour(cf, colors='k', linewidths=0.5)
    cbar = m.colorbar(cf, location='right')
    cbar.ax.tick_params(labelsize=fs)
    ax.set_title('Localized covariance '+ VAR + '-U', fontsize=fstitle)
    plt.savefig(outdir + '/' + VAR + '-U_Localized_Covariance.png', bbox_inches='tight')
    plt.close()

#==============================================================================
#                       VAR - V LOCALIZED COVARIANCE
#==============================================================================
    fig, ax, m, x, y = set_env_map(fs, lon, lat, LonI, LatJ, marker=True)
    scale = np.amax(np.abs(COVARIANCE[:, :, 1]))/5
    levels = np.array([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])*scale
    cf = ax.contourf(x, y, COVARIANCE[:, :, 1]*LOCALIZATION, cmap=div, levels=levels)
    ax.contour(cf, colors='k', linewidths=0.5)
    cbar = m.colorbar(cf, location='right')
    cbar.ax.tick_params(labelsize=fs)
    ax.set_title('Localized covariance '+ VAR + '-V', fontsize=fstitle)
    plt.savefig(outdir + '/' + VAR + '-V_Localized_Covariance.png', bbox_inches='tight')
    plt.close()

#==============================================================================
#                     VAR - PHI LOCALIZED COVARIANCE
#==============================================================================

    fig, ax, m, x, y = set_env_map(fs, lon, lat, LonI, LatJ, marker=True)
    scale = np.amax(np.abs(COVARIANCE[:, :, 2]))/5
    levels = np.array([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])*scale
    cf = ax.contourf(x, y, COVARIANCE[:, :, 2]*LOCALIZATION, cmap=div, levels=levels)
    ax.contour(cf, colors='k', linewidths=0.5)
    cbar = m.colorbar(cf, location='right')
    cbar.ax.tick_params(labelsize=fs)
    ax.set_title('Localized covariance '+ VAR + '-PHI', fontsize=fstitle)
    plt.savefig(outdir + '/' + VAR + '-PHI_Localized_Covariance.png', bbox_inches='tight')
    plt.close()

#==============================================================================
#               VAR - PHI , VAR - U , VAR - V LOCALIZED COVARANICE
#==============================================================================

    fig, ax, m, x, y = set_env_map(fs, lon, lat, LonI, LatJ, marker=True)
    scale = np.amax(np.abs(COVARIANCE[:, :, 2]))/5
    levels = np.array([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])*scale
    cf = ax.contourf(x, y, COVARIANCE[:, :, 2]*LOCALIZATION, cmap=div, levels=levels)
    ax.contour(cf, colors='k', linewidths=0.5)
    cbar = m.colorbar(cf, location='right')
    cbar.ax.tick_params(labelsize=fs)
    #ax.quiver(x, y, COVARIANCE[:, :, 0]*LOCALIZATION, COVARIANCE[:, :, 1]*LOCALIZATION, units='height', scale=0.6, width=0.002)
    q = ax.quiver(x, y, COVARIANCE[:, :, 0]*LOCALIZATION, COVARIANCE[:, :, 1]*LOCALIZATION, scale=wscale, units='inches', scale_units='inches')
    ax.quiverkey(q, 0.90, 0.1, wkey, wkey, labelpos='E', coordinates='figure')
    ax.set_title('Localized covariance '+ VAR + '-PHI (shaded), ' + VAR + '-U ; ' + VAR + '-V (vectors)', fontsize=fstitle)
    plt.savefig(outdir + '/' + VAR + '-PHI_Localized_Covariance_Vectors.png', bbox_inches='tight')
    plt.close()

#==============================================================================
#                 SINGLE OBSERVATION ANALYSIS INCREMENT
#==============================================================================
    print('    Analysis increment')
    fig, ax, m, x, y = set_env_map(fs, lon, lat, LonI, LatJ, marker=True)
    scale = np.amax(np.abs(INCREMENT[:, :, 2]))/5
    levels = np.array([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])*scale
    cf = ax.contourf(x, y, INCREMENT[:, :, 2], cmap=div, levels=levels)
    ax.contour(cf, colors='k', linewidths=0.5)
    cbar = m.colorbar(cf, location='right')
    cbar.ax.tick_params(labelsize=fs)
    #ax.quiver(x, y, INCREMENT[:, :, 0], INCREMENT[:, :, 1], units='height', scale=0.6, width=0.002)
    q = ax.quiver(x, y, INCREMENT[:, :, 0], INCREMENT[:, :, 1], scale=wscale, units='inches', scale_units='inches')
    ax.quiverkey(q, 0.90, 0.1, wkey, str(wkey), labelpos='E', coordinates='figure')
    ax.set_title('Analysis Increment in PHI (shaded), U;V (vectors)', fontsize=fstitle)
    plt.savefig(outdir + '/' + 'Analysis_Increment_PHI_Vectors.png', bbox_inches='tight')
    plt.close()

#==============================================================================
#                      SINGLE LOCALIZATION
#==============================================================================
    print('    Localization function')
    fig, ax, m, x, y = set_env_map(fs, lon, lat, LonI, LatJ, marker=True)
    scale = np.amax(np.abs(LOCALIZATION))/5
    levels = np.array([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])*scale
    cf = ax.contourf(x, y, LOCALIZATION, cmap=div, levels=levels)
    ax.contour(cf, colors='k', linewidths=0.5)
    cbar = m.colorbar(cf, location='right')
    cbar.ax.tick_params(labelsize=fs)
    ax.set_title('Localization function', fontsize=fstitle)
    plt.savefig(outdir + '/' + 'Localization_function.png', bbox_inches='tight')
    plt.close()
