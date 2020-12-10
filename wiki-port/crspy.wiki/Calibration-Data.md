# **Calibration Data**

This tool has been written primarily around the COSMOS-USA data. This means that the calibration data available at COSMOS website can be downloaded and used with this tool. 

For example, go to http://cosmos.hwr.arizona.edu/Probes/StationDat/046/calib.php if you click the scissors on the table, and select tab delimited table and copy this into excel, this would work fine within the tool. It will change the column names by default.

The naming also has to follow a convention as the timeseries data does, here we save as a `.csv` file. This is `Calib_"COUNTRY"_Site_"SITENUM"`. So if we had a `COUNTRY: UK` and `SITENUM: 101` the calibration data would be saved as `Calib_UK_Site_101.csv` 

### **None standard calibration data**

If you have data that does not follow the "standard" format it would need to be organised in a certain way to be used in crspy. This just means you need to ensure certain columns are available and it will work as normal. The require columns are:

| NAME      | UNITS                    | DESCRIPTION                                                  |
| --------- | ------------------------ | ------------------------------------------------------------ |
| DATE      | Date. Format "dd/mm/yyy" | Date that the data was collected from the site               |
| PROFILE   | int                      | Integer to differentiate profiles. A profile being a single core. The core could then have multiple "layers". |
| LOC_rad   | meters                   | Distance from the sensor for each sample in meters.          |
| DEPTH_AVG | cm                       | The depth of the soil sample for each layer. Taken as the mid point of the layer. |
| SWV       | (%)                      | The volumetric soil moisture of the sample. Given as a percent; i.e. 50% not 0.5 |

If you have more than a single day of calibration data, place all data in the same table. The n0_calibration function will identify that there are numerous days and complete calibration on each day. 