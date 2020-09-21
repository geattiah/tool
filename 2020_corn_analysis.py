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
lists4 = []
lists5 = []
lists6 = []
lists7 = []
file_name = []

folder = "D:\\Carpe_outputs\\2020_Corn-analysis\\auf_dem_2\\ndvi"

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

folder_2 = "D:\\Carpe_outputs\\2020_Corn-analysis\\bundes2\\ndvi"

for files in os.listdir(folder_2):
    if files.endswith('.tif'):
        filepath_out = os.path.join(folder_2, files)
        with rio.open(filepath_out) as input_raster_ndvi:
            ndvi = input_raster_ndvi.read(1)
            #print (ndvi)
        
        #fn = files[:10]
        a2 = np.nanmean(ndvi)
        lists2.append(a2)

folder_2 = "D:\\Carpe_outputs\\2020_Corn-analysis\\faenger2\\ndvi"

for files in os.listdir(folder_2):
    if files.endswith('.tif'):
        filepath_out = os.path.join(folder_2, files)
        with rio.open(filepath_out) as input_raster_ndvi:
            ndvi = input_raster_ndvi.read(1)
            #print (ndvi)
        
        #fn = files[:10]
        a3 = np.nanmean(ndvi)
        lists3.append(a3)

folder_2 = "D:\\Carpe_outputs\\2020_Corn-analysis\\kaempe1\\ndvi"

for files in os.listdir(folder_2):
    if files.endswith('.tif'):
        filepath_out = os.path.join(folder_2, files)
        with rio.open(filepath_out) as input_raster_ndvi:
            ndvi = input_raster_ndvi.read(1)
            #print (ndvi)
        
        #fn = files[:10]
        a4 = np.nanmean(ndvi)
        lists4.append(a4)
    
folder_2 = "D:\\Carpe_outputs\\2020_Corn-analysis\\niegerts\\ndvi"

for files in os.listdir(folder_2):
    if files.endswith('.tif'):
        filepath_out = os.path.join(folder_2, files)
        with rio.open(filepath_out) as input_raster_ndvi:
            ndvi = input_raster_ndvi.read(1)
            #print (ndvi)
        
        #fn = files[:10]
        a5 = np.nanmean(ndvi)
        lists5.append(a5)

folder_2 = "D:\\Carpe_outputs\\2020_Corn-analysis\\vehtbach1\\ndvi"

for files in os.listdir(folder_2):
    if files.endswith('.tif'):
        filepath_out = os.path.join(folder_2, files)
        with rio.open(filepath_out) as input_raster_ndvi:
            ndvi = input_raster_ndvi.read(1)
            #print (ndvi)
        
        #fn = files[:10]
        a6 = np.nanmean(ndvi)
        lists6.append(a6)

folder_2 = "D:\\Carpe_outputs\\2020_Corn-analysis\\wellen\\ndvi"

for files in os.listdir(folder_2):
    if files.endswith('.tif'):
        filepath_out = os.path.join(folder_2, files)
        with rio.open(filepath_out) as input_raster_ndvi:
            ndvi = input_raster_ndvi.read(1)
            #print (ndvi)
        
        #fn = files[:10]
        a7 = np.nanmean(ndvi)
        lists7.append(a7)


z = list(zip(file_name,lists,lists2,lists3,lists4,lists5,lists6,lists7))
print(lists)
print(file_name)
print(z)

x_val = [x[0] for x in z]
y_val = [x[1] for x in z]
y_val2 = [x[2] for x in z]
y_val3 = [x[3] for x in z]
y_val4 = [x[4] for x in z]
y_val5 = [x[5] for x in z]
y_val6 = [x[6] for x in z]
y_val7 = [x[7] for x in z]
        
plt.plot(x_val,y_val,"-b", Label = "Auf dem Stockum II")
plt.plot(x_val,y_val2,"-k", Label = "Bundesstrasse III")
plt.plot(x_val,y_val3,"-g", Label = "Fänger II")
plt.plot(x_val,y_val4,"-y", Label = "Kämpe I")
plt.plot(x_val,y_val5,"-r", Label = "Niegerts")
plt.plot(x_val,y_val6,"-c", Label = "Vehrter Bach I")
plt.plot(x_val,y_val7,"-m", Label = "Wellenbreite")
# plt.plot(x_val,y_val,'or', c = "b")
# plt.plot(x_val,y_val2, 'or', c = "k")
# plt.plot(x_val,y_val3,'or', c = "g")
# plt.plot(x_val,y_val4, 'or', c = "y")
# plt.plot(x_val,y_val5,'or', c = "r")
# plt.plot(x_val,y_val6, 'or', c = "c")
# plt.plot(x_val,y_val7,'or', c = "m")

plt.legend(loc="upper left")
plt.ylim(0,0.8)
plt.xticks(rotation=45)
plt.title("Corn field")
#plt.xticks(rotation=45)
plt.show()      



