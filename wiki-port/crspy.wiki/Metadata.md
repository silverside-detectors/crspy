# **Metadata**

When processing raw data to get soil moisture estimates, there is a need for site specific descriptors of some variables. For example, bulk density of the soil (g/cm^3) is required to obtain volumetric soil moisture estimates. These static values are stored in the `metadata.csv` file. 

Some values will need to be inputted manually by the user. In the below table these are any with a "Yes" for "Required at start?" column. Other values will be written during the running of the tool - obtained from various global datasets. 



| NAME             | UNITS       | DESCRIPTION                                                  | Required at start? |
| ---------------- | ----------- | ------------------------------------------------------------ | ------------------ |
| COUNTRY          | -           | Country code for location of site                            | Yes                |
| SITENUM          | -           | Assigned number for site. COUNTRY and SITENUM are used to identify each site. Naming convention is described in info. This is then used to find the relevant values in the meta_data.csv table. | Yes                |
| INSTALL_DATE     | -           | Date of site installation                                    | No                 |
| LONGITUDE        | degrees     | Longitude of site                                            | Yes                |
| LATITUDE         | degrees     | Latitude of site                                             | Yes                |
| ELEV             | m           | Elevation above sea level of site                            | Yes                |
| TIMEZONE         | -           | Timezone of the site                                         | No                 |
| GV               | gv          | Cutoff Rigidity of site                                      | Yes                |
| LW               | %           | Lattice Water from site specific calibration data            | Yes                |
| SOC              | %           | Soil Organic Carbon from site specific calibration data      | Yes                |
| BD               | g/cm3       | Bulk Density from site specific calibration data             | Yes                |
| N0               | -           | Theoretic maximum neutron count for site (dry conditions), calculated in tool and written. | No                 |
| AGBWEIGHT        | kg/m2       | Live woody above ground biomass estimates from ECMWF biomass data | No                 |
| RAIN_DATA_SOURCE | -           | Declaration of the source of rain data. Currently this will be either "Local" or "ERA5_Land" | No                 |
| TEM_DATA_SOURCE  | -           | Declaration of the source of temperature data. Currently this will be either "Local" or "ERA5_Land" | No                 |
| BETA_COEFF       | -           | Store of the calculated beta coefficient (see pressure calculations) for each individual site | No                 |
| REFERENCE_PRESS  | mb          | Reference pressure calculated using elevation                | No                 |
| BD_ISRIC         | g/cm3       | Bulk Density estimates taken from the International Soil Reference and Information Centre (SoilGrids250m https://soilgrids.org/ ) | No                 |
| SOC_ISRIC        | g/dm3       | Soil Organic Carbon estimates from ISRIC                     | No                 |
| pH_H20_ISRIC     | pH          | pH of water estimates from ISRIC                             | No                 |
| CEC_ISRIC        | mmol(c )/kg | Cation exchange capacity at ph7 from ISRIC                   | No                 |
| CFVO_ISRIC       | cm3/dm3     | Coarse fragments from ISRIC                                  | No                 |
| NITROGEN_ISRIC   | cg/kg       | Nitrogen in soil from ISRIC                                  | No                 |
| SAND_ISRIC       | g/kg        | Sand in soil from ISRIC                                      | No                 |
| SILT_ISRIC       | g/kg        | Silt in soil from ISRIC                                      | No                 |
| CLAY_ISRIC       | g/kg        | Clay in soil from ISRIC                                      | No                 |
| *_ISRIC_UC       | varied      | The uncertainty bounds of each of the ISRIC variables, in absolute terms. | No                 |
| TEXTURE          | -           | Soil texture identified from Sand/Silt/Clay percentages using the USDA soil texture triangle | No                 |
| WRB_ISRIC        | -           | World Reference Base (2006) soil class from ISRIC. Provided as a table of probable classes - this is the most probable class. | No                 |
| LAND_COVER       | -           | Land Cover type taken from Copernicus data set.              | No                 |

#### **Additional Info**

http://www.crnslab.org/ is a great resource. It is especially useful in finding site specific cut-off rigidity if it is not already available in data.
