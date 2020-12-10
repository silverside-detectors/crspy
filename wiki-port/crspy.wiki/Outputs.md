# **Outputs**

During the processing of sites, outputs are saved in the folders created at the beginning of the working directory set up. These are outlined below with each title representing which folder they will be found in.



#### **`data/crns_data/final`**

This folder will contain the final table which will include all variables. It is an iteration of the raw data that is initially fed into the program, attached to it are all the calculated factors, soil moisture estimates and additional variables sourced from ERA5-Land data. 



#### **`data/crns_data/tidy`**

This folder contains a copy of the raw data after the initial "tidy" processes are undertaken - such as master time and formatting. It is saved here as occasionally it is not possible to process a site entirely to the end but we can still get valuable information from it. 



#### **`data/crns_data/level1`**

This folder contains a copy of the raw data after the tidy process and after each factor has been calculated. This is a requirement for use in the N0 calibration. 



#### **`data/crns_data/dupe_check`**

This folder contains a copy of the raw data with a column attached which checks to see if an observation time has been duplicated by the master time creation. It is kept as it is important to check if duplication of observations is enough of an issue to lead to additional processing to be taken. A lot of duplications could indicate a sensor not measuring neutron counts correctly. 



#### **`data/n0_calibration`**

This folder will contain separate folders for each site that has been calibrated. When N0 calibration is undertaken there are a lot of iterations and steps and many of these are written here for full line of site. 

**Relative error plot**

A plot of the relative error found when using N0 (from 0 to 10,000) to estimate soil moisture is given. 

**Report**

A text report will be written like below (example taken from one of our sites). This is written out to clearly see what values have been used and a user should check this to ensure no mistakes have been made.

```
The optimised N0 is calculated as: 
N0   |  Total Relative Error  
       RelErr    N0
3297  0.36505  3297

The site calibrated was site number 101 in  UK and the name is Pounds 2B
The bulk density was 1.361
The user defined accuracy was 0.01
The soil organic carbon was 0.0325 g/m^3
The lattice water content was 0.031

 
Unique calibration dates where on: 
[datetime.date(2016, 11, 4) datetime.date(2015, 11, 4)
 datetime.date(2016, 2, 10) datetime.date(2015, 7, 3)]

Average neutron counts for each calib day where {0: 1837.7142857142858, 1: 1772.7142857142858, 2: 1766.2857142857142, 3: 1952.142857142857}
 
Please see the additional tables which hold calculations for each calibration date
```

This report will show the optimised N0 as well as the total relative error, that is the sum or errors for the optimised N0 based on all calibration days (explanation of this process can be found [here](https://github.com/danpower101/crspy/wiki/High-level-process-description)). The site name and number as well as the values used in calibration are written here. Unique calibration days are displayed along with the average neutron count for each calibration day. 

**Additional tables**

These tables write out the weighting values that are calculated during the calibration process. They also show the error for each calibration day individual as well as when taken together.



#### **`data/qa`**

This folder will contain a separate folder for each site. It contains figures that are useful for identifying possible issues with the data through visual checks as opposed to statistical. This includes time series representations of important variables that may allude to issues in the data (for example `BATT` reducing during winter months). It also contains heat maps that can be used to check if variables are covariant, where some you would expect to be but others should not be.