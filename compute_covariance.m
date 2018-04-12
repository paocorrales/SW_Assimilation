function [XMEAN,XSPREAD,COVARIANCE]=compute_covariance(XENS,GridJ,GridI,Variable);

XSPREAD=std(XENS,[],4);
XMEAN=mean(XENS,4);

[NLats NLons]=size(XENS);

COVARIANCE=NaN(NLats,NLons,3);

for ii=1:NLons
    for jj=1:NLats
        tmp=cov(squeeze(XENS(jj,ii,1,:)),squeeze(XENS(GridJ,GridI,Variable,:)));
        COVARIANCE(jj,ii,1)=tmp(2,1);
        tmp=cov(squeeze(XENS(jj,ii,2,:)),squeeze(XENS(GridJ,GridI,Variable,:)));
        COVARIANCE(jj,ii,2)=tmp(2,1);
        tmp=cov(squeeze(XENS(jj,ii,3,:)),squeeze(XENS(GridJ,GridI,Variable,:)));
        COVARIANCE(jj,ii,3)=tmp(2,1); 
    end
end

end