# **High level process description**

When running the function `crspy.process_raw_data()` there are a number of steps that occur. These have been wrapped into one function. Below is a high level description of what is occurring. When a time series is given as input to the function these are the steps that occur:

**Prepare Data**

The first step is preparing the data:

* Reads in the meta_data.csv file
* Extracts the country and sitenum from the file name
* Reads in the time series
* Formats the table (i.e. creates a DateTime column, cleans up whitespace etc.)
* Master Time - to allow easy integration of external data sources the time is adjusted so that each reading occurs on the hour (i.e. at 20:00 instead of 20:05). This is done by flooring the data to the hour. This occasionally causes duplicates for a single hour. For example, if a reading is from 20:05 and the next one is from 20:58. In these cases the first reading is kept and the second reading is flagged and removed. These can be checked by looking at the output given in `data>crns_data>dupe_check` where a column will state True/False depending on whether an hour has a duplicate.
* Reads in and collects all the ERA5-Land data for the site and prepares a dictionary with them
* Checks if local data is available, if it is unavailable it uses ERA5-Land data. This gets written to the `meta_data.csv` table. For example, if Local temperature data is used the `TEM_DATA_SOURCE` column will have `Local` written to it. This ensures full line of site on what data has been used where.
* The tool uses `PRESS1` (pressure) and `PRESS2` to give a single `PRESS` column (where `PRESS2` is used first and if not available uses `PRESS1` as a back up)
* Calculates vapour pressure (`VP`) and writes this as a column in the time series data. The process will differ depending on whether local RH data is available or not.
* Collects Jungfraujoch neutron counts from NMDB.eu and writes them as a column in the timeseries data.
* Final formatting of table and removing empty columns, saves table to folder `/data/crns_data/tidy`



**Correct neutrons**

Once prepared we correct neutron counts for external factors:

* Correct for Atmospheric Water Vapour
  
* Correct for Pressure
* Correct for Above Ground Biomass
* Correct for Solar Intensity
* Creates a corrected MOD based on above factors
* Creates an error column based on Poisson statistics

Click [here](tbc) for an in depth view of these correction steps.



**N0 Calibration**

If turned on it can also use the calibration data prepared and placed in the `data>calibration_data` folder to get an estimate of N0 (the theoretical neutron count in dry conditions). This method follows the most recent advancements in site calibration presented by [Schrön et al., (2017)](https://doi.org/10.5194/hess-21-5009-2017). The paper outlines the process in great detail and should be read for a full understanding. Below is a brief summary of some of the steps towards calibration of CRNS sites.

* Reads in site constants such as bulk density and lattice water
* Identifies how many unique calibration days there are and separates them into tables
* Gets average pressure, temperature and vapour pressure values for each unique day
* For each day it will iterate a loop to find the area averaged soil moisture based on the weighting procedures identified in Shcrön et al., (2017).
* To begin it will provide a field average soil moisture estimate based on equal weighting of each soil sample.
* Next a rescaled radial distance is calculated based on pressure, distance from the sensor and the initial field average soil moisture estimate.
* Next for each soil profile it will calculate a vertical weighted average of soil moisture using equations identified in Shcrön et al., (2017). This has dependencies on pressure, bulk density and it's radial distance from the sensor.
* Once each profile has a weighted average, the field average is calculated by weighting each profile based on it's radial distance from the sensor - with different weighting procedures on profiles less than 5m from sensor, 5-50m from sensor and over 50m from sensor. These have dependencies on humidity and temperature. 
* Finally with a field average estimate now available, this is compared with the initial equal average soil moisture estimate. If they diverge beyond the the accuracy assigned at the beginning it will loop through again using the new field average estimate until they converge. 
* Once we have the field average estimate of soil moisture for each calibration day we are able to identify N0. 
* We get the average `MOD` value for each calibration day and time from the time series data. 
* We iterate the soil moisture calculation with the obtained `MOD` value and insert N0 values from 0 - 10,000. These will give soil moisture estimates for each N0 value. 
* We can compare the soil moisture estimates from the 10,000 calculations with the calculated field average estimates from the above process. We then identify the N0 value that gives the least error.
* We do this for each site. To obtain the N0 we sum the error across all calibration days for each N0 and the N0 with the lowest total error is used.
* Finally the weighting tables and a user report are output to the folder `data>n0_calibration` for the user to see.

**Quality Analysis**

Once we have an N0 value it is possible to undertake quality analysis and remove data believed to be erroneous. Here we follow the same procedures as most networks. Data removed includes:

* N values that are greater than 20% in difference to previous N value - FLAG 1
* N values less than 30% of N0 - FLAG 2
* N values above N0 - FLAG 3
* Battery voltage below 10v - FLAG 4

N values are removed and the flag value is written to the `FLAG` column in the final table.

At this point a series of time series figures are created and saved to the `data>qa>*site` folder. These are provided as useful visual cues that can provide insight to possible issues in the data. For example, it's possible to see patterns of `PRESS` over time, or identify gaps or when values change. 

**Calculate soil moisture**

The final step is to calculate soil moisture. This uses the standard equation to calculate soil moisture based on the corrected neutron counts. We also calculate soil moisture error. 

This is defined by Poisson statistics where neutrons are considered to have an error equal to the square root of the measured neutrons. We take this neutron error value we call `Nerr`. `Nerr` is added to neutron counts and this new neutron value is used to estimate soil moisture. `Nerr` is also subtracted from neutron counts and this new neutron value is used to estimate soil moisture. We can now see the error bars of soil moisture rather than the error bars of raw neutrons.

Measurement depth is also calculated using methods described in Shcrön et al., (2017). This is the depth at which 86% of neutrons measured are thought to have originated from. 

These values are all written and a final table is output that includes all relevant variables for each site. This is written to `data>crns_data>final` 