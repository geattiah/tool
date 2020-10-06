import sys
import os
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np
from osgeo import gdal
import fnmatch
import fiona
from fiona.crs import from_epsg
import rasterio as rio
from rasterio.plot import plotting_extent,show
from rasterio.mask import mask

rain = pd.read_csv("D:\\carpe_prog_data\\weather\\rain.csv") 
temp = pd.read_csv("D:\\carpe_prog_data\\weather\\temp.csv") 

rain_out = dict(zip(temp.Zeitstempel, temp.Wert))
print(rain_out)


print(temp)

dat = 2017_02_02
date = str(dat)
#date_input = str(date[0:4])+str(date[5:7])+ str(date[8:])
print(date)
results = rain_out[int(date)]
print(results)

