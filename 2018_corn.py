import os
import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import mapping
import rasterio as rio
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
import matplotlib.colors as mcolors

import csv
import pandas as pd
import matplotlib.pyplot as plt

file_name = []
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
lists = []
lists2 = []
lists3 = []
lists4 = []

folder = "D:\\Carpe_outputs\\2018_corn\\Bundesstrasse3\\ndvi"

for files in os.listdir(folder):
    if files.endswith('.tif'):
        filepath_out = os.path.join(folder, files)
        with rio.open(filepath_out) as input_raster_ndvi:
            ndvi = input_raster_ndvi.read(1)
            #print (ndvi)
        
        fn = files[:10]
        a1 = np.nanmean(ndvi)

        lists.append(a1)
        file_name.append(fn)

folder_2 = "D:\\Carpe_outputs\\2018_corn\\Gattberg1\\ndvi"

for files in os.listdir(folder_2):
    if files.endswith('.tif'):
        filepath_out = os.path.join(folder_2, files)
        with rio.open(filepath_out) as input_raster_ndvi:
            ndvi = input_raster_ndvi.read(1)
            #print (ndvi)
        
        #fn = files[:10]
        a2 = np.nanmean(ndvi)
        lists2.append(a2)

folder_2 = "D:\\Carpe_outputs\\2018_corn\\Kampe1\\ndvi"

for files in os.listdir(folder_2):
    if files.endswith('.tif'):
        filepath_out = os.path.join(folder_2, files)
        with rio.open(filepath_out) as input_raster_ndvi:
            ndvi = input_raster_ndvi.read(1)
            #print (ndvi)
        
        #fn = files[:10]
        a3 = np.nanmean(ndvi)
        lists3.append(a3)

folder_2 = "D:\\Carpe_outputs\\2018_corn\\Kampe2\\ndvi"

for files in os.listdir(folder_2):
    if files.endswith('.tif'):
        filepath_out = os.path.join(folder_2, files)
        with rio.open(filepath_out) as input_raster_ndvi:
            ndvi = input_raster_ndvi.read(1)
            #print (ndvi)
        
        #fn = files[:10]
        a4 = np.nanmean(ndvi)
        lists4.append(a4)
    
z = list(zip(months,lists,lists2,lists3,lists4))

x_val = [x[0] for x in z]
y_val = [x[1] for x in z]
y_val2 = [x[2] for x in z]
y_val3 = [x[3] for x in z]
y_val4 = [x[4] for x in z]

plt.plot(x_val,y_val,"-b", Label = "Bundesstrasse III")
plt.plot(x_val,y_val2,"-r", Label = "Gattberg I")
plt.plot(x_val,y_val3,"-g", Label = "Kämpe I")
plt.plot(x_val,y_val4,"-y", Label = "Kämpe II")
plt.plot(x_val,y_val,'or', c = "b")
plt.plot(x_val,y_val2, 'or', c = "r")
plt.plot(x_val,y_val3,'or', c = "g")
plt.plot(x_val,y_val4, 'or', c = "y")
plt.legend(loc="upper right")
plt.ylim(0,1)
plt.xticks(rotation=45)
plt.title("Corn field - 2018")
#plt.xticks(rotation=45)
plt.show() 