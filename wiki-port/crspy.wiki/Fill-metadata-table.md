# **Fill metadata table**

Once the additional data has been collected and the `meta_data.csv` table has been filled out with the required data we can fill the metadata into the table. This can be done with this script:

```python
from name_list import nld
import crspy
import pandas as pd

# Read in the meta_data.csv file using pandas
meta = pd.read_csv(nld['defaultdir']+"/data/meta_data.csv")

# Run the function
meta = crspy.fill_meta_data(meta)
```

This will now go through the metadata table row by row and append the data from the numerous sources, using the latitude and longitude of the site as the input variables in finding information.

**Data written to table**

The data collected and written are:

* https://soilgrids.org/ data - all data written along with uncertainties
* soil textures - obtained from above data
* land cover data
* above ground biomass estimates
* beta coefficient - a variable that changes based on latitude, cut-off rigidity and elevation, used in pressure corrections
* reference pressure - also used in pressure corrections

