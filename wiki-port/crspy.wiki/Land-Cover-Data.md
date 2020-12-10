#  **Land Cover Data**

We collect land cover data from the cdsapi as well. Landcover data is presented as a global product at 100m grid resolution. It is a yearly product, that is one value is given for each grid for a year. In the crspy design we take the 2018 dataset. This will be written to site metadata for analysis.

Full details on the product can be found [here](https://www.esa-landcover-cci.org/).

To download the land cover netcdf you simply run:

```python
import crspy

crspy.dl_land_cover()
```

This will download the 2018 data and save it in `defaultdir/data/land_cover_data/`