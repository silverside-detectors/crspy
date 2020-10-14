"""
Created on Wed Aug 28 15:20:35 2019

@author: Daniel Power
Email: daniel.power@bristol.ac.uk

This module takes in the combined data from combine_data.py and processes the 
neutron correction. It creates a column with the relevant coefficients. This 
allows detailed look at how each coefficient impacts theta.

Citations: 
    Hawdon, A., D. McJannet, and J. Wallace (2014), 
    Calibration and correction procedures for cosmic-ray neutron soil moisture 
    probes located across Australia, 
    Water Resour. Res., 50, 5029–5043, doi:10.1002/ 2013WR015138.

    Rosolem, R. and Shuttleworth, W. J. and Zreda, M. and Franz, T. E. and 
    Zeng, X. and Kurc, S. A. (2013),
    The effect of atmospheric water vapor on neutron count in the cosmic-ray soil 
    moisture observing system,
    Journal of Hydrometeorology, 14, 1659--1671
    
    Baatz, R., H. R. Bogena, H.-J. Hendricks Franssen, J. A. Huisman, C. Montzka, 
    and H. Vereecken (2015), 
    An empirical vegetation correction for soil water content quantification using 
    cosmic ray probes, Water Resour. Res., 51, 2030–2046, doi:10.1002/ 2014WR016443.
    
"""
from name_list import nld
import os
import math
import pandas as pd # Pandas for dataframe
import numpy as np

# crspy funcs
from crspy.neutron_correction_funcs import (
        pv,
        humfact,
        pressfact_B,
        finten,
        RcCorr,
        agb,              
        )

os.chdir(nld['defaultdir']) #set wd

def neutcoeffs(df, country, sitenum):
    """
    Provides the correction factors for the time series data. 
    
    Steps include:
        - Calculate fawv - first calculate pv from VP and TEMP then fawv
        - Calculate fbar - use metadata to collect betacoeff and refpres
        - Calculate solar intensity - use ref date (01/05/2011) for Jung Count and Jungcount
          additionally corrected with RcCorr
        - Calculate fagb 
    """
    
    print ("~~~~~~~~~~~~~ Calculate Neutron Correction Factors ~~~~~~~~~~~~~")
    # Read in meta fresh
    meta = pd.read_csv(nld['defaultdir']+"/data/metadata.csv")
    meta['SITENUM'] = meta.SITENUM.map("{:03}".format) # Ensure its three digits
    
    df = df.replace(nld['noval'], np.nan)
    
    ###############################################################################
    #                    Atmospheric Water Vapour                                 #
    ###############################################################################
    """
    Rosolem et al., (2013)
    
    Uses ERA5_Land data for vapour pressure and temperature to find absolute humidity.
    This can then be converte to neutrons which is again converted to a coefficient
    for tidy data. Ref pressure of PV0 is always set to 0.
    """
    # Define Constant
    
    df['pv'] = df.apply(lambda row: pv(row['VP'], row['TEMP']), axis=1) # VP is in Pascals and TEMP is in Cel
    df['pv'] = df['pv']*1000 # convert Kg m-3 to g m-3
    df["fawv"] = df.apply(lambda row: humfact(row['pv'], nld['pv0']), axis=1)

    
    ###############################################################################
    #                            Pressure                                         #
    ###############################################################################
    
    """
    
    """
    refpres = meta.loc[(meta.SITENUM == sitenum) & (meta.COUNTRY == country), "REFERENCE_PRESS"].item()
    beta = meta.loc[(meta.SITENUM == sitenum) & (meta.COUNTRY == country), "BETA_COEFF"].item()
    df['fbar'] = df.apply(lambda row: pressfact_B(row['PRESS'], beta, refpres), axis = 1)
    
    

    ###############################################################################
    #                       Solar Intensity                                       #
    ###############################################################################
    """
    The fsol comes from HydroInnova - update required to correct the coefficient for
    the differencee in cutoff ridgitiy (GV) between Junfraujoch and the CRNS site.
    
    See Hawdon et al (2014) for full explanation - equation taken from that paper.
    """
    Rc = meta.loc[(meta.SITENUM == sitenum) & (meta.COUNTRY == country), "GV"].item()
    RcCorrval = RcCorr(Rc)
    df['finten_noGV'] = df.apply(lambda row: finten(nld['jung_ref'], row['JUNG_COUNT']), axis=1)
    
    df['finten'] = (df['finten_noGV'] - 1) * RcCorrval + 1
    
    ###############################################################################
    #                       Above Ground Biomass                                  #
    ###############################################################################
    """
    The agbval comes from metadata and is above ground biomas (Kg m^2). Currently
    using a single value but hope in the future to find seasonal data.   
    """
    #The below bwe will eventually be read in from metadata file or a bwe file
    agbval = meta.loc[(meta.COUNTRY == country) & (meta.SITENUM == sitenum), 'AGBWEIGHT'].item() # Taken from supplemental data of Franz et al., 2012
    if math.isnan(agbval): # Introduce catch incase info isn't available
        df['fagb'] = 1
    else:
        df['fagb'] = df.apply(lambda row: agb(agbval), axis = 1)
        
    ###############################################################################
    #                        Corrected Neutrons                                   #
    ###############################################################################
    """
    Need to create the MODCORR which is corrected neutrons. 
    """
    df['MOD_CORR'] = df['MOD'] * df['fbar'] * df['finten'] * df['fawv'] * df['fagb']  
    df['MOD_CORR'] = df['MOD_CORR'].apply(np.floor)
    
    # Error is the ((standard deviation) / MOD)*MODCORR
    df['MOD_ERR'] = (np.sqrt(df['MOD'])/df['MOD']) * df['MOD_CORR']
    df['MOD_ERR'] = df['MOD_ERR'].apply(np.floor)
    
    # Remove calcs done on missing data
    DTstore = df['DT']
    df = df.reset_index(drop=True)
    df.loc[df['finten'].isnull(), :] = np.nan
    df = df.set_index(DTstore)
    df['DT'] = df.index
    df = df.replace(np.nan,nld['noval'])
    df = df.round(3) # decimal place limit
    
    # Save Lvl1 data
    df.to_csv(nld['defaultdir'] + "/data/crns_data/level1/"+country+"_SITE_" + sitenum+"_LVL1.txt",
          header=True, index=False, sep="\t",  mode='w')
    meta.to_csv(nld['defaultdir'] + "/data/metadata.csv", header=True, index=False, mode='w')
    print ("Done")
    return df, meta