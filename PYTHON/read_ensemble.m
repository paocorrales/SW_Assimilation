function XENS=read_ensemble(path_data,prefix,NLons,NLats,NVars,EnsSize,Time)


XENS=NaN(NLats,NLons,NVars,EnsSize);  %Analysis ensemble mean

  tstr=num2str(10000+Time);
  tstr=tstr(2:end);
  
  if( strcmp(prefix,'XA') )
      folder='ANALYSIS';
  end
  if( strcmp(prefix,'XB') )
      folder='GUES';
  end
  
  
  for iens=1:EnsSize
    ensstr=num2str(1000+iens);
    ensstr=ensstr(2:end);
    
    file=[path_data '/' folder '/ENS/' prefix '_T' tstr '_M' ensstr];
    nfile=fopen(file,'r','l');
    for ivar=1:NVars
    XENS(:,:,ivar,iens)=flipdim(fread(nfile,[NLons NLats],'single')',1);  
    end
    fclose(nfile);
  end