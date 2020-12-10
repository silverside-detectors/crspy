# **Above Ground Biomass Data**

Above ground biomass is a signal that should be removed from raw neutron data before estimating soil moisture. Obtaining dynamic data should be the ultimate goal as, especially in places where biomass changes with seasons, this should be corrected to remove this noise in the data. In practical terms this data is very hard to get hold of, especially a global resource. 

Crspy will correct the raw neutrons data using biomass estimates obtained from another cdsapi product. This above ground biomass product uses the year 2017 as it's base and gives estimates that we convert to kg/m^2.

Full details on the product can be found [here](http://cci.esa.int/sites/default/files/Biomass_D1.2_%20Product_Specification_Document_v2.pdf)

To collect the data another simple function is run:

```python
import crspy

crspy.dl_agb()
```

Once it has finished downloading the netcdf will be in `defaultdir/data/global_biomass_netcdf/`