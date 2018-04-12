function plot_covariance(XBS,COVARIANCE,LOCALIZATION,INCREMENT,lon,lat,LonI,LatJ,Variable)

ms=14; %Marker size
fs=[0 0 30 30];

coast=load('coast');
coast.long(coast.long < 0)=coast.long(coast.long < 0)+360;
for ii=1:length(coast.long)-1
    if( abs(coast.long(ii) - coast.long(ii+1)) > 180)
        coast.long(ii)=NaN;
        coast.long(ii+1)=NaN;
    end
end


if(Variable==1)
    VAR='U';
elseif( Variable==2)
    VAR='V';
elseif( Variable==3)
    VAR='PHI';
end

%==========================================================================
%                     U VARIANCE
%==========================================================================

hFig=figure('Menubar','none'); %,'Visible','Off');
set(hFig, 'Units', 'centimeters', 'Position', fs)

scale=max(max(abs(XBS(:,:,1))))/5;
levels=[0 1 2 3 4 5]*scale;
colors=[2 32 34 36 38];
contourf(lon,lat,XBS(:,:,1),levels);
hold on
plot_jrcol(levels,colors);

plot(coast.long,coast.lat,'k','LineWidth',2)
title(['U Variance (m/s)'],'FontSize',15);
colorbar('YTick',levels);
xlabel('Lon','FontSize',15);ylabel('Lat','FontSize',15)
set(gca,'FontSize',15)

%==========================================================================
%                     V VARIANCE
%==========================================================================


hFig=figure('Menubar','none'); %,'Visible','Off');
set(hFig, 'Units', 'centimeters', 'Position', fs)

scale=max(max(abs(XBS(:,:,2))))/5;
levels=[0 1 2 3 4 5]*scale;
colors=[2 32 34 36 38];
contourf(lon,lat,XBS(:,:,2),levels);
hold on
plot_jrcol(levels,colors);

plot(coast.long,coast.lat,'k','LineWidth',2)
title(['V Variance (m/s)'],'FontSize',15);
colorbar('YTick',levels);
xlabel('Lon','FontSize',15);ylabel('Lat','FontSize',15)
set(gca,'FontSize',15)
axis('square')

%==========================================================================
%                     PHI VARIANCE
%==========================================================================

hFig=figure('Menubar','none'); %,'Visible','Off');
set(hFig, 'Units', 'centimeters', 'Position', fs)

scale=max(max(abs(XBS(:,:,3))))/5;
levels=[0 1 2 3 4 5]*scale;
colors=[2 32 34 36 38];
contourf(lon,lat,XBS(:,:,3),levels);
hold on
plot_jrcol(levels,colors);

plot(coast.long,coast.lat,'k','LineWidth',2)
title(['PHI Variance (m)'],'FontSize',15);
colorbar('YTick',levels);
xlabel('Lon','FontSize',15);ylabel('Lat','FontSize',15)
set(gca,'FontSize',15)
axis('square')


%==========================================================================
%                     VAR - U COVARIANCE
%==========================================================================

hFig=figure('Menubar','none'); %,'Visible','Off');
set(hFig, 'Units', 'centimeters', 'Position', fs)

scale=max(max(abs(COVARIANCE(:,:,1))))/5;
levels=[-5 -4 -3 -2 -1 1 2 3 4 5]*scale;
colors=[48 46 44 42 2 32 34 36 38];
contourf(lon,lat,COVARIANCE(:,:,1),levels);
hold on
plot_jrcol(levels,colors);
plot(LonI,LatJ,'ok','MarkerSize',ms,'MarkerFaceColor','k')
plot(coast.long,coast.lat,'k','LineWidth',2)
title(['Covariance ' VAR '-U '],'FontSize',15);
colorbar('YTick',levels);
xlabel('Lon','FontSize',15);ylabel('Lat','FontSize',15)
set(gca,'FontSize',15)
axis('square')


%==========================================================================
%                     VAR - V COVARIANCE
%==========================================================================

hFig=figure('Menubar','none'); %,'Visible','Off');
set(hFig, 'Units', 'centimeters', 'Position',fs)

scale=max(max(abs(COVARIANCE(:,:,2))))/5;
levels=[-5 -4 -3 -2 -1 1 2 3 4 5]*scale;
colors=[48 46 44 42 2 32 34 36 38];
contourf(lon,lat,COVARIANCE(:,:,2),levels);
plot_jrcol(levels,colors);
hold on
plot(LonI,LatJ,'ok','MarkerSize',ms,'MarkerFaceColor','k')
plot(coast.long,coast.lat,'k','LineWidth',2)
%quiver(lon,lat,XBM(:,:,1,end)-XTMEAN(:,:,1),-XBM(:,:,2,end)+XTMEAN(:,:,2))
title(['Covariance ' VAR '-V '],'FontSize',15);
colorbar('YTick',levels);
xlabel('Lon','FontSize',15);ylabel('Lat','FontSize',15)
set(gca,'FontSize',15)
axis('square')


%==========================================================================
%                     VAR - PHI COVARIANCE
%==========================================================================

hFig=figure('Menubar','none'); %,'Visible','Off');
set(hFig, 'Units', 'centimeters', 'Position',fs)

scale=max(max(abs(COVARIANCE(:,:,3))))/5;
levels=[-5 -4 -3 -2 -1 1 2 3 4 5]*scale;
colors=[48 46 44 42 2 32 34 36 38];
contourf(lon,lat,COVARIANCE(:,:,3),levels);
plot_jrcol(levels,colors);
hold on
plot(LonI,LatJ,'ok','MarkerSize',ms,'MarkerFaceColor','k')
plot(coast.long,coast.lat,'k','LineWidth',2)
%quiver(lon,lat,XBM(:,:,1,end)-XTMEAN(:,:,1),-XBM(:,:,2,end)+XTMEAN(:,:,2))
title(['Covariance ' VAR '-PHI'],'FontSize',15);
colorbar('YTick',levels);
xlabel('Lon','FontSize',15);ylabel('Lat','FontSize',15)
set(gca,'FontSize',15)
axis('square')

%==========================================================================
%                     VAR - PHI , VAR - U , VAR - V COVARANICE
%==========================================================================

hFig=figure('Menubar','none'); %,'Visible','Off');
set(hFig, 'Units', 'centimeters', 'Position',fs)

scale=max(max(abs(COVARIANCE(:,:,3))))/5;
levels=[-5 -4 -3 -2 -1 1 2 3 4 5]*scale;
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


%==========================================================================
%                     VAR - U LOCALIZED COVARIANCE
%==========================================================================

hFig=figure('Menubar','none'); %,'Visible','Off');
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

%==========================================================================
%                    VAR - V LOCALIZED COVARIANCE
%==========================================================================

hFig=figure('Menubar','none'); %,'Visible','Off');
set(hFig, 'Units', 'centimeters', 'Position',fs)

scale=max(max(abs(COVARIANCE(:,:,2))))/5;
levels=[-5 -4 -3 -2 -1 1 2 3 4 5]*scale;
colors=[48 46 44 42 2 32 34 36 38];
contourf(lon,lat,COVARIANCE(:,:,2).*LOCALIZATION,levels);
plot_jrcol(levels,colors);
hold on
plot(LonI,LatJ,'ok','MarkerSize',ms,'MarkerFaceColor','k')
plot(coast.long,coast.lat,'k','LineWidth',2)
%quiver(lon,lat,XBM(:,:,1,end)-XTMEAN(:,:,1),-XBM(:,:,2,end)+XTMEAN(:,:,2))
title(['Localized covariance ' VAR '-V'],'FontSize',15);
colorbar('YTick',levels);
xlabel('Lon','FontSize',15);ylabel('Lat','FontSize',15)
set(gca,'FontSize',15)
axis('square')

%==========================================================================
%                     VAR - PHI LOCALIZED COVARIANCE
%==========================================================================

hFig=figure('Menubar','none'); %,'Visible','Off');
set(hFig, 'Units', 'centimeters', 'Position',fs)

scale=max(max(abs(COVARIANCE(:,:,3))))/5;
levels=[-5 -4 -3 -2 -1 1 2 3 4 5]*scale;
colors=[48 46 44 42 2 32 34 36 38];
contourf(lon,lat,COVARIANCE(:,:,3).*LOCALIZATION,levels);
plot_jrcol(levels,colors);
hold on
plot(LonI,LatJ,'ok','MarkerSize',ms,'MarkerFaceColor','k')
plot(coast.long,coast.lat,'k','LineWidth',2)
%quiver(lon,lat,XBM(:,:,1,end)-XTMEAN(:,:,1),-XBM(:,:,2,end)+XTMEAN(:,:,2))
title(['Localized covariance ' VAR '-PHI'],'FontSize',15);
colorbar('YTick',levels);
xlabel('Lon','FontSize',15);ylabel('Lat','FontSize',15)
set(gca,'FontSize',15)
axis('square')

%==========================================================================
%           VAR - PHI , VAR - U , VAR - V LOCALIZED COVARANICE
%==========================================================================

hFig=figure('Menubar','none'); %,'Visible','Off');
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


%==========================================================================
%   SINGLE OBSERVATION ANALYSIS INCREMENT 
%==========================================================================

hFig=figure('Menubar','none'); %,'Visible','Off');
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



%==========================================================================
%   SINGLE LOCALIZATION
%==========================================================================

hFig=figure('Menubar','none'); %,'Visible','Off');
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

