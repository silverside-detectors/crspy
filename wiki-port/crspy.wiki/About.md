# **Cosmic Ray Sensor Python Tool (crspy)**

## **About**

#### **What is crspy?**

It stands for **c**osmic **r**ay neutron ­­**s**ensor **py**thon tool. Cosmic Ray Neutron Sensors (CRNS) are a technique of estimating field scale soil moisture by detecting Neutrons generated from Cosmic-Rays (see references such as - Zreda et al., 2012, Hawdon et al., 2014). 

A CRNS has a tube connected to it which will detect when a fast neutron, which originate from Cosmic-Rays, passes through it. Fast neutrons are slowed down when they encounter Hydrogen atoms more so than other elements. With this knowledge we can estimate field scale soil moisture with these instruments. For a more complete description please refer to the above referenced literature which outlines the technology in much greater detail.

There are several steps required to correct for external factors, the most important ones being pressure, incoming cosmic ray intensity, atmospheric water vapour and above ground biomass (**include refs here**). We also need to calibrate the sensor to each site and convert neutron counts into soil moisture estimates. 

To make things easier crspy is a python tool that calibrates, corrects and processes raw CRS data to give soil moisture estimates. 

#### **Why make crspy?**

There are numerous CRS networks around the world, such as COSMOS (USA), COSMOS-UK (UK), TERENO (Germany) and CosmOz (Australia). There are also individual sites around the world such as the ones our group at Bristol own. 

Since the first inception of CRNSs, improvements have been identified but, in some instances, not implemented to all networks. Additionally, each network has made decisions on best practice when it comes to correcting their own sites. This tool came to be from a desire to process CRNS sites from across the globe in a harmonized way. It is designed to be modular so that as the CRS community improve the efficacy of this technique it can easily be applied to available data. 

Networks such as COSMOS and CosmOz publicly share their raw data. This tool allows the processing of that data to give soil moisture estimates that have been estimated in a harmonized way. It has been provided as an open source tool to allow discussion and collaboration. 

#### **What does it do?**

It is possible for crspy to process raw neutron counts, correct for external variables, provide quality analysis, site calibration and calculate soil moisture estimates along with error bars and graphical outputs for analysis. 

This can easily be applied to any site around the world as long as the minimum required data is provided. One key aspect is the tool can collect additional data from global sources to fill in any potential gaps. 

