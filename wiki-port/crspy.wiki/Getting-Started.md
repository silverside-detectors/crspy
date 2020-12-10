## **Getting Started**

### **Installation**

It is recommended to use git to copy and organise the package, this can be in the terminal if on mac or linux. If using windows, GitBash is a very useful tool (https://gitforwindows.org/). In either the terminal or GitBash run:

```
git clone https://github.com/danpower101/crspy
```

This will clone the repository giving you the package ready to install. It will also contain some files that will be needed in the initial set up as well as an example dataset to run.

Once downloaded it can be installed with conda. Open up anaconda prompt (or terminal/cmd if this is your preferred route). Navigate to the folder where crspy downloaded:

```
cd ~/path/to/folder/crspy
```

Once inside the folder it can be installed to the python environment using:

```
pip install .
```

This will now install crspy to the PATH so it can be imported like any python tool you may use already. 



### **Setting up the working environment**

When working with crspy it is recommended to set up a new working directory. In this example we set up a new working directory called "cosmos_analysis" using terminal:

```
mkdir ~/user/cosmos_analysis
```

#### **Name List**

In the cloned repository there will be a file named `name_list.py`. This file is used throughout the code as a way to change global values without having to go into the code. Most of these should be kept as default as they will impact the code and the outputs. The most important is `defaultdir` which should be a string to your working directory folder. For example here we change it to:

`defaultdir = "~/user/cosmos_analysis"`

When you process data within crspy it is important to import this dictionary along with any packages you need using:

```python
from name_list import nld
```

Then if you want to call the defaultdir you would use:

```
nld['defaultdir']
```

#### **Initialise the Working Directory**

Once the above step has been done we can initialise the working directory 

Run the following code from within the working directory in your Python IDE:

```python
from name_list import nld
import crspy

wd = nld['defaultdir']
crspy.initial(wd)
```
This will create a data folder, the structure of this folder is:

```
├───data
│   ├───calibration_data
│   ├───crns_data
│   │   ├───dupe_check
│   │   ├───final
│   │   ├───level1
│   │   ├───raw
│   │   ├───simple
│   │   ├───theta
│   │   └───tidy
│   ├───era5land
│   ├───global_biomass_tiff
│   ├───land_cover_data
│   ├───n0_calibration
│   └───qa
└───__pycache__
```

It will also write a base `meta_data.csv` file which should be filled in as described in the Meta Data section.

#### **nmdb_stations**

If you wish to have the option to use the intensity correction where the station with the nearest cut-off ridgidity is used as opposed to using Jungrfraujoch with an additional correction (RcCorr) then you need to move the file `nmdb_stations.csv` into the data folder of you working directory. This is a list of station codes and their respective GV based on the information on NMDB.eu. With this you can now turn on:

`intentype = "nearestGV"`

when processing the data (see [**Processing Data**](https://github.com/danpower101/crspy/wiki/Processing-the-data) ) . The default is to use the Jungfraujoch station with the additioanl correction.