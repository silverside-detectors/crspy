# **Processing the data**

It is possible to process the data with the use of a single function. This functions takes in two arguments. One is the path to the raw time series data - which should be stored in the `data>crns_data>raw` folder. The other is a Boolean tag to state whether to run the n0 calibration process. It saves time and is not necessary to calibrate on each run. 



```python
from name_list import nld
import crspy

# Use the getlistoffiles function to get a list of file paths for time series data
fileslist = crspy.getlistoffiles(nld['defaultdir']+"/data/crns_data/raw/")

# Run the process with the following - outputs are the dataframe and metadata file - args are first file in list, and whether calibration is required.
df, meta = crspy.process_raw_data(fileslist[0], calibrate=True)

# Or alternatively to use the nearestGV process (such as that used by CosmOz) write:
df, meta = crspy.process_raw_data(fileslist[0], calibrate=True, intentype="nearestGV")
```

This is all that's needed. The final data frame will be output as well as the metadata (which would include an updated N0 for the site if calibrate is True). The program will output and save tables, figures and additional data during the running of the process.