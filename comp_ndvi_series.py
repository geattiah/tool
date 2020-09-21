import os
import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import mapping
import rasterio as rio
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
import matplotlib.colors as mcolors

lists = []
lists2 = []
lists3 = []
file_name = []
months = [ "May", "Jun", "Jul", "Aug", "Sep", "Oct"]


folder = "D:\\data\\kam2\\dump\\ndvi\\Kaempe_1"

for files in os.listdir(folder):
    if files.endswith('.tif'):
        filepath_out = os.path.join(folder, files)
        with rio.open(filepath_out) as input_raster_ndvi:
            ndvi = input_raster_ndvi.read(1)
            #print (ndvi)
        
        
       
        a1 = np.nanmean(ndvi)

        lists.append(a1)
        #file_name.append(fn)

folder_2 = "D:\\data\\kam2\\dump\\ndvi\\Kaempe_2"

for files in os.listdir(folder_2):
    if files.endswith('.tif'):
        filepath_out = os.path.join(folder_2, files)
        with rio.open(filepath_out) as input_raster_ndvi:
            ndvi = input_raster_ndvi.read(1)
            #print (ndvi)
        
        #fn = files[:10]
        a2 = np.nanmean(ndvi)
        lists2.append(a2)
        #file_name.append(fn)

folder_2 = "D:\\data\\kam2\\dump\\ndvi\\Bundes"

for files in os.listdir(folder_2):
    if files.endswith('.tif'):
        filepath_out = os.path.join(folder_2, files)
        with rio.open(filepath_out) as input_raster_ndvi:
            ndvi = input_raster_ndvi.read(1)
            #print (ndvi)
        
        #fn = files[:8]
        fn = files[:7]
        file_name.append(fn)
        a3 = np.nanmean(ndvi)
        lists3.append(a3)

z = list(zip(months,lists,lists2,lists3))
print(lists)
print(file_name)
print(z)

x_val = [x[0] for x in z]
y_val = [x[1] for x in z]
y_val2 = [x[2] for x in z]
y_val3 = [x[3] for x in z]

#plt.plot(x_val,y_val,"-b", Label = "2017")
plt.plot(x_val,y_val2,"-y", Label = "Kaempe_II")
plt.plot(x_val,y_val3,"-b", Label = "Bundesstrasse_III")

#plt.plot(x_val,y_val,'or', c = "b")
plt.plot(x_val,y_val2, 'or', c = "y")
plt.plot(x_val,y_val3,'or', c = "b")

plt.legend(loc="upper right")
plt.ylim(0,1)
plt.xticks(rotation=45)
plt.title("Maize Crop - 2018")
#plt.xticks(rotation=45)
plt.show()  