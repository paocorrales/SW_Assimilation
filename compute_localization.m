
function [LOCALIZATION]=compute_localization(NLats,NLons,LonI,LatJ,lon,lat,LOCALIZATION_SCALE)


LOCALIZATION=zeros(NLats,NLons);

for jj=1:NLats
    for ii=1:NLons
        dist_m=distll_fun(LonI,LatJ,lon(jj,ii),lat(jj,ii));
        LOCALIZATION(jj,ii)=exp( -0.5*( (dist_m*dist_m) / (LOCALIZATION_SCALE*LOCALIZATION_SCALE) ) );
        
    end
end