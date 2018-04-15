function XENS = read_ensemble(path_data,prefix,NLons,NLats,NVars,EnsSize,Time)
 def read_ensamble(path_data,prefix,NLons,NLats,NVars,EnsSize,Time):
     
     XENS = np.full((NLats,NLons,NVars,EnsSize), np.nan)   #Analysis ensemble mean

     tstr = str(10000 + Time) 
     tstr = tstr[1::]
  
     if prefix == 'XA':
         folder = 'ANALYSIS' 
     elif prefix == 'XB':
         folder = 'GUES' 
  
    for iens in len(EnsSize):
        ensstr = str(1000+iens) 
        ensstr = ensstr[1::]
        
        file = path_data + folder + '/ENS/' + prefix + '_T' + tstr + '_M' + ensstr 
        nfile = fopen(file,'r','l') 
    
    for ivar in len(NVars)
    XENS(:,:,ivar,iens)=flipdim(fread(nfile,[NLons NLats],'single')',1)   
    
    fclose(nfile) 
  