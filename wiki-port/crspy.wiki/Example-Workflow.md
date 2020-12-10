# **Walkthrough**

Firstly ensure that you have python and git installed. Here I am using a windows machine so I use [GitBash](https://gitforwindows.org/). If you are not on windows using the terminal along with git in the same way will work. Firstly I want to make a folder to download the crspy tool to. The folder will be:

`~\Users\Dan\Documents\CRS`

Open up GitBash and move to that folder. For this I would need to type and run:

`cd Documents/CRS/`

Next clone the repo by running the following command:

`git clone https://github.com/danpower101/crspy`

This will now download the crspy tool along with the example data. 

### **Installing crspy**

The next step is to install crspy as a package that can be imported to python. Install the package using pip. For example, here I would open up Anaconda Prompt (which acts like CMD.exe for the conda distribution of python). In Anaconda Prompt I would navigate to the folder containing crspy.

`cd Documents\CRS\crspy\` 

Once in this folder install using the following command:

`pip install .`

It should now use install crspy as an importable package to your

*NOTE: there are differences in using " \ "  or " / "depending on your operating system and software. GitBash uses linux style commands and so file paths use " / " whereas Anaconda Prompt will use Windows style so it will use " \ " for file paths. If you get errors switching between software this could be the cause.*

****

### **Set up the working directory**

Next we want to make a directory that will be used to store all the data we will process, analyse and use. Here I created a folder called:

`~\Users\Dan\Documents\CRS\analysis`

In this folder copy and paste the example file `name_list.py` which can be found in the downloaded crspy folder. The name_list is used to define constant variables for use in crspy. Most of these can be left as default, however we want to change the `defaultdir` variable. This can be done in any text editor. In this example I would change the line:

`defaultdir = "C:/user/example_working_directory"`

 to 

`defaultdir = "C:/Users/Dan/Documents/CRS/analysis/"`

Next I want to prepare the environment with the folder structure. Open up a python IDE (such as Spyder) and make sure to change the working directory to the same as the `defaultdir` value. Once done the following code should be run:

```python
from name_list import nld # this reads in the dictionary of constants
import crspy # import the crspy package

crspy.initial(nld['defaultdir']) #Run the initialisation function
```

This will create the required folder structure along with a skeleton outline of the metadata table. 

### **Adding data to the folders**

The next step is preparing the folders with the required data. Examples are provided in the downloaded crspy repository in `crspy/data`. The example come from one of the sites within the COSMOS network which is publicly available for download [here](http://cosmos.hwr.arizona.edu/)

For the purposes of this workflow there is an example `meta_data.csv` pre-filled out with the meta_data for the example data. This can be found in the `crspy/data`folder in the downloaded crspy repository. 

The process to download ERA5-Land is time consuming. The documentation explains this process in greater detail [here](https://github.com/danpower101/crspy/wiki/ERA5-Land-Data), for this workflow, a pre-prepared netcdf example is given. This should be copied into the `data/era5land` folder.

Once you have copied the ERA5-Land data into the `data/era5land` folder you will need to change a variable in the `name_list.py` file. Here you will change the `era5_filenam` variable to match the name of the ERA5-Land netcdf. Here this would be:

`era5_filename = "example_era5land"`

Calibration data is provided and should be copied from the cloned repository to the `data/calibration_data/` folder.

Raw data is provided and should be copied from the cloned repository to the `data/crns_data/raw` folder. 

### **Setting up CDS-API for Python**

It is also **important** to set up your computer to use the cds-api from within Python - this is described [here](https://github.com/danpower101/crspy/wiki/ERA5-Land-Data#setting-up-your-environment)

### **Downloading additional data**

Additional data is needed to fill out the meta_data table and for analysis. These are explained in greater detail in the wiki. Some are easily accessed via an API however some require us to download and store a copy in our working directory. We need to download ERA5-Land data (skipped here) as well as the land cover data and the above ground biomass data. To download these, in Python run:

```python
crspy.dl_land_cover() # about 2GB
crspy.dl_agb() # about 25GB
```

If the cds-api has been correctly set up this will download a global map for each of these data types that can then be used to extract data from latitude and longitude. 

Take a quick coffee break whilst they download...

### **Fill in the metadata table**

At this point we are ready to fill in the meta_data table. This is done with a single function that takes as it's input our `metadata.csv` and outputs a filled `metadata.csv`. It also saves the table to the data directory. Some of the data is taken from the pre-downloaded data and some is directly accessed from APIs. 

```python
import pandas as pd # pandas is needed to read in the csv

# Read in the metadata.csv file using pandas
meta = pd.read_csv(nld['defaultdir']+"/data/metadata.csv")

# Run the function
meta = crspy.fill_metadata(meta)
```

Due to the size of the downloaded files you may wish to delete the netcdf files in `data/global_biomass_netcdf` and `data/land_cover_data`. The values have been extracted for the sites and placed into the `meta_data.csv` so will not be required until new sites are added.

### **Process raw data**

Now that the working directory has been prepared and data has been downloaded and written to the appropriate tables, raw data can be processed through to the final product. A simple function call can run all the steps for data. Here there is also a helper function that is used to list all the raw data you may have, this can then be written as a loop for processing many sites. 

```python
# Use the getlistoffiles function to get a list of file paths for time series data
fileslist = crspy.getlistoffiles(nld['defaultdir']+"/data/crns_data/raw/")

# Run the process with the following - outputs are the dataframe and metadata file - args are first file in list, and whether calibration is required. If we don't have a N0 in meta_data.csv but do have calibration data this can be set to True
df, meta = crspy.process_raw_data(fileslist[0], calibrate=True)
```

Once done the outputs should be in their appropriate folder. 