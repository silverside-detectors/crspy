# **Raw Site Timeseries Data**

This tool has been written primarily around publicly available raw neutron data. As it is likely peoples tables will be structured differently it uses column titles to identify which columns are which. Below is a table showing what each column should be labelled as in order for crspy to function correctly. Some data may be missing depending on what you have available. Much of this has been developed around the USA COSMOS network data (http://cosmos.hwr.arizona.edu/).

### **Naming each file to put in data/crns_data/raw**

Each file should be a tab delimited file. Each file should have a unique name that follows the structure `"COUNTRY"_SITE_"SITENUM"`. This will mean that the metadata table can be used as a look up, when you put a file into the main function it extracts country and sitenum from the table name and uses this to look up in `meta_data.csv`

So for example if your meta_data.csv had a site as `COUNTRY: UK` and `SITENUM: 101` the timeseries would be saved as `UK_SITE_101.txt`

Each time series should be placed in `defaultdir/data/crns_data/raw`

### **Column Titles**

The below table shows what each column title should be:

| NAME   | UNITS    | DESCRIPTION                                                  |
| ------ | -------- | ------------------------------------------------------------ |
| TIME   | datetime | Datetime of the observation. Format: "yyyy-mm-dd hh:mm:ss"   |
| MOD    | count    | Moderated neutron count for time interval                    |
| UNMOD  | count    | Unmoderated neutron count for time interval                  |
| PRESS1 | mb       | Pressure sensor number 1. Usually the older analogue version that is somewhat less accurate |
| PRESS2 | mb       | Pressure sensor number 2. This will be used primarily and if unavailable PRESS1 will be used in place. |
| I_TEM  | Celsius  | Internal Temperature of the sensor box in degrees Celsius    |
| I_RH   | (%)      | Relative humidity inside the sensor box, given as a percent  |
| BATT   | Voltage  | Voltage of the battery                                       |
| E_TEM  | Celsius  | External Temperature at the site. This would be an external reading. If not available then ERA5-Land data is used |
| E_RH   | (%)      | External Relative Humidity at the site. If not available then dewpoint temperature is used to find absolute humidity |
| RAIN   | mm       | Rainfall at the site. If local is available this is used - if not available it is obtained from ERA5-Land data |

E_TEM, E_RH and RAIN are desirable but not always available. The tool will adjust if these are not present to use ERA5-Land data. You may have additional observations but these are a minimum.