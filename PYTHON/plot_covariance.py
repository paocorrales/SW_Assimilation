from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize

# set the colormap and centre the colorbar
class MidpointNormalize(Normalize):
    def __init__(self, vmin=None, vmax=None, midpoint=None, clip=False):
        self.midpoint = midpoint
        Normalize.__init__(self, vmin, vmax, clip)

    def __call__(self, value, clip=None):
        # I'm ignoring masked values and all kinds of edge cases to make a
        # simple example...
        x, y = [self.vmin, self.midpoint, self.vmax], [0, 0.5, 1]
        return np.ma.masked_array(np.interp(value, x, y))

norm = MidpointNormalize(midpoint=0)  

# Palette
seq = plt.get_cmap('YlGn')
div = plt.get_cmap('PRGn')
  
#def shiftedColorMap(cmap, min_val, max_val):
#    '''Function to offset the "center" of a colormap. Useful for data with a negative min and positive max and you want the middle of the colormap's dynamic range to be at zero. Adapted from https://stackoverflow.com/questions/7404116/defining-the-midpoint-of-a-colormap-in-matplotlib
#
#    Input
#    -----
#      cmap : The matplotlib colormap to be altered.
#      start : Offset from lowest point in the colormap's range.
#          Defaults to 0.0 (no lower ofset). Should be between
#          0.0 and `midpoint`.
#      midpoint : The new center of the colormap. Defaults to
#          0.5 (no shift). Should be between 0.0 and 1.0. In
#          general, this should be  1 - vmax/(vmax + abs(vmin))
#          For example if your data range from -15.0 to +5.0 and
#          you want the center of the colormap at 0.0, `midpoint`
#          should be set to  1 - 5/(5 + 15)) or 0.75
#      stop : Offset from highets point in the colormap's range.
#          Defaults to 1.0 (no upper ofset). Should be between
#          `midpoint` and 1.0.'''
#    epsilon = 0.001
#    start, stop = 0.0, 1.0
#    min_val, max_val = min(0.0, min_val), max(0.0, max_val) # Edit #2
#    midpoint = 1.0 - max_val/(max_val + abs(min_val))
#    cdict = {'red': [], 'green': [], 'blue': [], 'alpha': []}
#    # regular index to compute the colors
#    reg_index = np.linspace(start, stop, 257)
#    # shifted index to match the data
#    shift_index = np.hstack([np.linspace(0.0, midpoint, 128, endpoint=False), np.linspace(midpoint, 1.0, 129, endpoint=True)])
#    for ri, si in zip(reg_index, shift_index):
#        if abs(si - midpoint) < epsilon:
#            r, g, b, a = cmap(0.5) # 0.5 = original midpoint.
#        else:
#            r, g, b, a = cmap(ri)
#        cdict['red'].append((si, r, r))
#        cdict['green'].append((si, g, g))
#        cdict['blue'].append((si, b, b))
#        cdict['alpha'].append((si, a, a))
#    newcmap = matplotlib.colors.LinearSegmentedColormap(cdict)
#    plt.register_cmap(cmap=newcmap)
#    return newcmap
        
def plot_covariance(XSPREAD,COVARIANCE,LOCALIZATION,INCREMENT,lon,lat,LonI,LatJ,Variable):
 
    if (Variable==1):
        VAR='U'
    elif (Variable==2):
        VAR='V'
    elif( Variable==3):
        VAR='PHI'


#==========================================================================
#                     U VARIANCE
#==========================================================================

fig, ax = plt.subplots(figsize=(16, 12))
map = Basemap(projection='mill',lon_0=180)
map.drawcoastlines()
map.drawparallels(np.arange(-80,90,20),labels=[1,0,0,0], fontsize=10)
map.drawmeridians(np.arange(map.lonmin,map.lonmax+30,40),labels=[0,0,0,1], fontsize=10)
map.colorbar(cf, location='right')
x, y = map(lon, lat)
cf = ax.contourf(x, y, XSPREAD[:, :, 0], cmap = seq)
ax.contour(cf, colors='k', linewidths=0.5)
ax.set_xlabel('Lon', labelpad = 20)
ax.set_ylabel('Lat', labelpad = 30)
ax.set(title='U Variance (m/s)')[-0.012, -0.006, 0.006, 0.012]
plt.savefig('../FIG/U_Variance.png')

#==========================================================================
#                     V VARIANCE
#==========================================================================

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

#==========================================================================
#                     PHI VARIANCE
#==========================================================================

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


#==========================================================================
#                     VAR - U COVARIANCE
#==========================================================================

fig, ax = plt.subplots(figsize=(16, 12))
map = Basemap(projection='mill',lon_0=180)
map.drawcoastlines()
map.drawparallels(np.arange(-80,90,20),labels=[1,0,0,0], fontsize=10)
map.drawmeridians(np.arange(map.lonmin,map.lonmax+30,40),labels=[0,0,0,1], fontsize=10)
x, y = map(lon, lat)
Lon, Lat = map(LonI, LatJ)
#scale = shiftedColorMap(PRGn, min_val = np.min(COVARIANCE[:, :, 0]), max_val = np.max(np.min(COVARIANCE[:, :, 0])))
cf = ax.contourf(x, y, COVARIANCE[:, :, 0], norm = norm, cmap = div)
ax.contour(cf, colors='k', linewidths=0.5)
ax.plot(Lon, Lat, marker='.', markersize=25, color="red")
ax.set_xlabel('Lon', labelpad = 20)
ax.set_ylabel('Lat', labelpad = 30)
ax.set(title='Covariance '+ VAR + '-U')
map.colorbar(cf, location='right')
plt.savefig('../FIG/' + VAR + '-U_Variance.png')


#==========================================================================
#                     VAR - V COVARIANCE
#==========================================================================

fig, ax = plt.subplots(figsize=(16, 12))
map = Basemap(projection='mill',lon_0=180)
map.drawcoastlines()
map.drawparallels(np.arange(-80,90,20),labels=[1,0,0,0], fontsize=10)
map.drawmeridians(np.arange(map.lonmin,map.lonmax+30,40),labels=[0,0,0,1], fontsize=10)
x, y = map(lon, lat)
Lon, Lat = map(LonI, LatJ)
cf = ax.contourf(x, y, COVARIANCE[:, :, 1], norm = norm, cmap = div)
ax.contour(cf, colors='k', linewidths=0.5)
ax.plot(Lon, Lat, marker='.', markersize=25, color="red")
ax.set_xlabel('Lon', labelpad = 20)
ax.set_ylabel('Lat', labelpad = 30)
ax.set(title='Covariance '+ VAR + '-V')
map.colorbar(cf, location='right')
plt.savefig('../FIG/' + VAR + '-V_Variance.png')


#==========================================================================
#                     VAR - PHI COVARIANCE
#==========================================================================

fig, ax = plt.subplots(figsize=(16, 12))
map = Basemap(projection='mill',lon_0=180)
map.drawcoastlines()
map.drawparallels(np.arange(-80,90,20),labels=[1,0,0,0], fontsize=10)
map.drawmeridians(np.arange(map.lonmin,map.lonmax+30,40),labels=[0,0,0,1], fontsize=10)
x, y = map(lon, lat)
Lon, Lat = map(LonI, LatJ)
cf = ax.contourf(x, y, COVARIANCE[:, :, 2], cmap = div)
ax.contour(cf, colors='k', linewidths=0.5)
ax.plot(Lon, Lat, marker='.', markersize=25, color="red")
ax.set_xlabel('Lon', labelpad = 20)
ax.set_ylabel('Lat', labelpad = 30)
ax.set(title='Covariance '+ VAR + '-PHI')
map.colorbar(cf, location='right')
plt.savefig('../FIG/' + VAR + '-PHI_Variance.png')

#==========================================================================
#                     VAR - PHI , VAR - U , VAR - V COVARANICE
#==========================================================================

fig, ax = plt.subplots(figsize=(16, 12))
map = Basemap(projection='mill',lon_0=180)
map.drawcoastlines()
map.drawparallels(np.arange(-80,90,20),labels=[1,0,0,0], fontsize=10)
map.drawmeridians(np.arange(map.lonmin,map.lonmax+30,40),labels=[0,0,0,1], fontsize=10)
x, y = map(lon, lat)
Lon, Lat = map(LonI, LatJ)
cf = ax.contourf(x, y, COVARIANCE[:, :, 2], cmap = div)
ax.contour(cf, colors='k', linewidths=0.5)
ax.plot(Lon, Lat, marker='.', markersize=25, color="red")
Q = ax.quiver(x, y, COVARIANCE[:, :, 0], COVARIANCE[:, :, 1], units = 'height', width=0.001)
ax.set_xlabel('Lon', labelpad = 20)
ax.set_ylabel('Lat', labelpad = 30)
ax.set(title='Covariance '+ VAR + '-PHI (shaded), ' + VAR + '-U ; ' + VAR + '-V (vectors)')
map.colorbar(cf, location='right')
plt.savefig('../FIG/' + VAR + '-PHI_Variance.png')


#scale=max(max(abs(COVARIANCE(:,:,3))))/5;
#levels=[-5 -4 -3 -2 -1 1 2 3 4 5]*scale;
colors=[48 46 44 42 2 32 34 36 38];
contourf(lon,lat,COVARIANCE(:,:,3),levels);
plot_jrcol(levels,colors);
hold on
plot(LonI,LatJ,'ok','MarkerSize',ms,'MarkerFaceColor','k')
quiver(lon,lat,COVARIANCE(:,:,1),COVARIANCE(:,:,2))
plot(coast.long,coast.lat,'k','LineWidth',2)
title(['Covariance ' VAR '-PHI (shaded), ' VAR '-U ; ' VAR '-V (vectors)'],'FontSize',15)
plot(coast.long,coast.lat,'k','LineWidth',2)
colorbar('YTick',levels);
xlabel('Lon','FontSize',15);ylabel('Lat','FontSize',15)
set(gca,'FontSize',15)
axis('square')


#==========================================================================
#                     VAR - U LOCALIZED COVARIANCE
#==========================================================================

hFig=figure('Menubar','none'); #,'Visible','Off');
set(hFig, 'Units', 'centimeters', 'Position',fs)

scale=max(max(abs(COVARIANCE(:,:,1))))/5;
levels=[-5 -4 -3 -2 -1 1 2 3 4 5]*scale;
colors=[48 46 44 42 2 32 34 36 38];
contourf(lon,lat,COVARIANCE(:,:,1).*LOCALIZATION,levels);
hold on
plot_jrcol(levels,colors);
plot(LonI,LatJ,'ok','MarkerSize',ms,'MarkerFaceColor','k')
plot(coast.long,coast.lat,'k','LineWidth',2)
title(['Localized covariance ' VAR '-U'],'FontSize',15);
colorbar('YTick',levels);
xlabel('Lon','FontSize',15);ylabel('Lat','FontSize',15)
set(gca,'FontSize',15)
axis('square')

#==========================================================================
#                    VAR - V LOCALIZED COVARIANCE
#==========================================================================

hFig=figure('Menubar','none'); #,'Visible','Off');
set(hFig, 'Units', 'centimeters', 'Position',fs)

scale=max(max(abs(COVARIANCE(:,:,2))))/5;
levels=[-5 -4 -3 -2 -1 1 2 3 4 5]*scale;
colors=[48 46 44 42 2 32 34 36 38];
contourf(lon,lat,COVARIANCE(:,:,2).*LOCALIZATION,levels);
plot_jrcol(levels,colors);
hold on
plot(LonI,LatJ,'ok','MarkerSize',ms,'MarkerFaceColor','k')
plot(coast.long,coast.lat,'k','LineWidth',2)
#quiver(lon,lat,XBM(:,:,1,end)-XTMEAN(:,:,1),-XBM(:,:,2,end)+XTMEAN(:,:,2))
title(['Localized covariance ' VAR '-V'],'FontSize',15);
colorbar('YTick',levels);
xlabel('Lon','FontSize',15);ylabel('Lat','FontSize',15)
set(gca,'FontSize',15)
axis('square')

#==========================================================================
#                     VAR - PHI LOCALIZED COVARIANCE
#==========================================================================

hFig=figure('Menubar','none'); #,'Visible','Off');
set(hFig, 'Units', 'centimeters', 'Position',fs)

scale=max(max(abs(COVARIANCE(:,:,3))))/5;
levels=[-5 -4 -3 -2 -1 1 2 3 4 5]*scale;
colors=[48 46 44 42 2 32 34 36 38];
contourf(lon,lat,COVARIANCE(:,:,3).*LOCALIZATION,levels);
plot_jrcol(levels,colors);
hold on
plot(LonI,LatJ,'ok','MarkerSize',ms,'MarkerFaceColor','k')
plot(coast.long,coast.lat,'k','LineWidth',2)
#quiver(lon,lat,XBM(:,:,1,end)-XTMEAN(:,:,1),-XBM(:,:,2,end)+XTMEAN(:,:,2))
title(['Localized covariance ' VAR '-PHI'],'FontSize',15);
colorbar('YTick',levels);
xlabel('Lon','FontSize',15);ylabel('Lat','FontSize',15)
set(gca,'FontSize',15)
axis('square')

#==========================================================================
#           VAR - PHI , VAR - U , VAR - V LOCALIZED COVARANICE
#==========================================================================

hFig=figure('Menubar','none'); #,'Visible','Off');
set(hFig, 'Units', 'centimeters', 'Position',fs)

scale=max(max(abs(COVARIANCE(:,:,3))))/5;
levels=[-5 -4 -3 -2 -1 1 2 3 4 5]*scale;
colors=[48 46 44 42 2 32 34 36 38];
contourf(lon,lat,COVARIANCE(:,:,3).*LOCALIZATION,levels);
plot_jrcol(levels,colors);
hold on
plot(LonI,LatJ,'ok','MarkerSize',ms,'MarkerFaceColor','k')
quiver(lon,lat,COVARIANCE(:,:,1).*LOCALIZATION,COVARIANCE(:,:,2).*LOCALIZATION)
plot(coast.long,coast.lat,'k','LineWidth',2)
title(['Localized covariance ' VAR '-PHI (shaded), ' VAR '-U ; ' VAR '-V (vectors)'],'FontSize',15)
plot(coast.long,coast.lat,'k','LineWidth',2)
colorbar('YTick',levels);
xlabel('Lon','FontSize',15);ylabel('Lat','FontSize',15)
set(gca,'FontSize',15)
axis('square')


#==========================================================================
#   SINGLE OBSERVATION ANALYSIS INCREMENT 
#==========================================================================

hFig=figure('Menubar','none'); #,'Visible','Off');
set(hFig, 'Units', 'centimeters', 'Position',fs)

scale=max(max(abs(INCREMENT(:,:,3))))/5;
levels=[-5 -4 -3 -2 -1 1 2 3 4 5]*scale;
colors=[48 46 44 42 2 32 34 36 38];
contourf(lon,lat,INCREMENT(:,:,3),levels);
plot_jrcol(levels,colors);
hold on
plot(LonI,LatJ,'ok','MarkerSize',ms,'MarkerFaceColor','k')
quiver(lon,lat,INCREMENT(:,:,1),INCREMENT(:,:,2))
plot(coast.long,coast.lat,'k','LineWidth',2)
title('Analysis Increment in PHI (shaded), U;V (vector)','FontSize',15)
plot(coast.long,coast.lat,'k','LineWidth',2)
colorbar('YTick',levels);
xlabel('Lon','FontSize',15);ylabel('Lat','FontSize',15)
set(gca,'FontSize',15)
axis('square')



#==========================================================================
#   SINGLE LOCALIZATION
#==========================================================================

hFig=figure('Menubar','none'); #,'Visible','Off');
set(hFig, 'Units', 'centimeters', 'Position',fs)

scale=max(max(abs(LOCALIZATION)))/5;
levels=[0 1 2 3 4 5]*scale;
colors=[2 42 44 46 48];
contourf(lon,lat,LOCALIZATION,levels);
plot_jrcol(levels,colors);
hold on
plot(LonI,LatJ,'ok','MarkerSize',ms,'MarkerFaceColor','k')
plot(coast.long,coast.lat,'k','LineWidth',2)
title('Localization function','FontSize',15)
plot(coast.long,coast.lat,'k','LineWidth',2)
colorbar('YTick',levels);
xlabel('Lon','FontSize',15);ylabel('Lat','FontSize',15)
set(gca,'FontSize',15)
axis('square')

