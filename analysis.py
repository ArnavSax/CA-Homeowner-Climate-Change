# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import seaborn as sb

# seaice = pd.read_csv("C:/Users/saxen/Desktop/ClimateData/seaice.csv")
# greenhouseGases = pd.read_csv("C:/Users/saxen/Desktop/ClimateData/greenhouse_gas_inventory_data_data.csv")
df = pd.read_csv("C:/Users/saxen/Desktop/ClimateData/BerkeleyData/GlobalTemperatures.csv")
# globalTempbyState = pd.read_csv("C:/Users/saxen/Desktop/ClimateData/BerkeleyData/GlobalLandTemperaturesByState.csv")
# globalTempbyMajorCity = pd.read_csv("C:/Users/saxen/Desktop/ClimateData/BerkeleyData/GlobalLandTemperaturesByMajorCity.csv")
# globalTempbyCountry = pd.read_csv("C:/Users/saxen/Desktop/ClimateData/BerkeleyData/GlobalLandTemperaturesByCountry.csv")
# globalTempCity = pd.read_csv("C:/Users/saxen/Desktop/ClimateData/BerkeleyData/GlobalLandTemperaturesByCity.csv")

#stuff = [seaice, greenhouseGases, globalTemp, globalTempbyState, globalTempbyMajorCity, globalTempbyCountry, globalTempCity]

# for i cin stuff:
#     print(i.describe())
#sb.barplot(greenhouseGases["year"], greenhouseGases["value"])
# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)
# pd.set_option('display.width', 1000)
# pd.set_option('display.colheader_justify', 'center')
# pd.set_option('display.precision', 3)
# solar = pd.read_csv("project-sunroof-state.csv")


sb.relplot(x=df["dt"], y=df["LandAverageTemperature"])




