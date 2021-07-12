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
from PIL import Image

stackfile = "D:\\new\\a\\stack\\stack.tif"
with rio.open(stackfile) as input_raster:
    lai = input_raster.read(1)
    ndmi = input_raster.read(2)
    ndvi = input_raster.read(3)
    rain = input_raster.read(4)
    temp = input_raster.read(5)
    slope = input_raster.read(6)
    soil = input_raster.read(7)  

# tool = np.where(lai > 2 , 'high', 
#          (np.where(ndmi < 6, 'low', 'medium')))

    lai_c = np.where((lai>2) & (ndvi>0.5) ,1,(2)
    print(lai_c)



#print(choices)
#x = np.where(lai >1 & ndmi > 2) 


