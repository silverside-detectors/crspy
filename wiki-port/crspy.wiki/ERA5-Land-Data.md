# **ERA5-Land Data**

Not all sites have all the necessary in-situ measurements of external variables available, in order to correct for all the currently known factors. The solution to this was to identify a global product that spans the spatial and temporal extent of the CRNS networks around the world. ERA5-Land data does just that. There are some steps required to get the data from the server into a format for use in crspy. The tools have been provided in crspy to do this.

### **Data description**

A full documentation on the ERA5-Land dataset can be found [here](https://confluence.ecmwf.int/display/CKB/ERA5-Land%3A+data+documentation)

It is a reanalysis dataset that spans the globe at 9km spatial resolution and 1 hour temporal resolution. It is provided by the European Centre for Medium-Range Weather Forecasts (ECMWF) and described as:

> Reanalysis combines model data with observations from across the world  into a globally complete and consistent dataset using the laws of  physics.

### **Data we collect**

There is a lot of possible data to download and a user can adapt any scripts to allow this. As default crspy will download:

* 2m Surface Temperature
* Surface Pressure
* Total Precipitation
* Volumetric Soil Moisture (4 layers)
* 2m Dewpoint Temperature
* Snow Water Equivelant



## **The data collection process**

### **Setting up your environment**

To access the data you will need an account -  [register here](https://cds.climate.copernicus.eu/user/register)

Once registered and logged in, you will be able to access the your API key [here](https://cds.climate.copernicus.eu/api-how-to)

To set up your computer you need to save a text file with the following:

```
url: https://cds.climate.copernicus.eu/api/v2
key: enter your key here
```

Save this file as `.cdsapirc`

These should be saved in the Home folder.

In a Windows environment this will be saved as `C:\Users\username_folder\.cdsapirc`

In a Linux environment in `$Home/.cdsapirc`

In a MacOS environment in `~/.cdsapirc`

Once this is done you will be able to use the `cdsapi` python tool to download data - as these credentials are used to confirm you are registered. 

### **Downloading the data**

The cdsapi can be slow to provide data. It has a limit on data points rather than overall size. Due to this we need to download data month by month. Crspy has a function to do this all automatically. Be aware however that for 10 years of data it can take ~36 hours to download all of it (see tips for ways to reduce this below). 

It is better to download a large spatial area and extract the data for that than to download individual grid points as they will take the same amount of time to process. 

The function `crspy.era5landdl(area, years, months, variables, savename)` is used.

area should be an array with max degrees in `[north, west, south, east]` 
years should be an array of years.
months should be an array of months (as integers).
variables is an array of the variables (names can be found on ERA5-Land website)
savename is a string to append to each file to save them (useful if downloading two separate areas)

```python
import crspy

area = [72,-156.7, 29.7, -68]
years = [2015,2016,2017]
months = [1,2,3,4,5,6,7,8,9,10,11,12]
variables = [
    '2m_temperature',
	'surface_pressure',
	'total_precipitation',
	'volumetric_soil_water_layer_1',
	'volumetric_soil_water_layer_2',
	'volumetric_soil_water_layer_3',
	'volumetric_soil_water_layer_4',
	'2m_dewpoint_temperature',
	'snow_depth_water_equivalent'
			]
savename = "First_batch"

crspy.era5landdl(area, years, months, variables, savename)
```

Running the above code will start a loop that downloads the data month by month as a netcdf. This data will be stored in `defaultdir/data/era5land/store/`



### **Sorting the data**

Once downloaded you will have a folder full of netcdf files. To make these manageable we will extract the grid points we need for each site and save them into another netcdf. This means we can save storage space. 

Firstly ensure that the `meta_data.csv` file has been filled out with the required data. This will be used to identify grid points (specifically using latitude and longitude along with site number and country)

We will now use the function `crspy.era5landnetdf(years, months, tol, loadname, savename, ogfile)`

`years` is the array of years you have downloaded in total
`months` is the array of months downloaded
`tol` is a float number to define the tolerance in degrees by which data will be taken from (to stop accidently setting data from grids far away)
`loadname` is the string given to the downloaded files in the previous function
`savename` is the name of the file to save the final netcdf as
`ogfile` can be left blank, if you have already processed a batch and saved the file it will read this and append data to it

```python
import crspy

years = [2015,2016,2017]
months = [1,2,3,4,5,6,7,8,9,10,11,12]
tol = 0.1 # recommended tolerance as this is a 9km grid point
loadname = "First_batch" # match above savename
savename = "era5land_all_sites"
#if we already processed a batch we could use:
	#ogfile = nld['defaultdir']+"/data/era5land/era5land_all_sites.nc"

crspy.era5landnetcdf(years, months, tol, loadname, savename)
```

We will now have a netcdf file for era5-land variables for the 3 years we wanted. These can be appended to sites now if required and used for analysis. For example, if you have a `USA_SITE_001` this will be the name of the slice for its data in the netcdf. 

### **Top Tip**

When downloading ERA5-Land data the bottleneck is on the cdsapi servers. They allow you to run **5** concurrent requests on the server however. If you open 5 kernels in your Python IDE, split the data into 5 batches and run them at the same time. For example, downloading 10 years of data as above - it will download in around 6-7 hours as opposed to 36 hours!