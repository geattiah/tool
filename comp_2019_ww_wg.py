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
lists8 = []
file_name = []

folder = "D:\\Carpe_outputs\\WW_analysis\\2017_WW_analysis\\comp_ww_wg_2020\\ndvi\\ander_pan"

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

folder_2 = "D:\\Carpe_outputs\\WW_analysis\\2017_WW_analysis\\comp_ww_wg_2020\\ndvi\\auf_dem_br"

for files in os.listdir(folder_2):
    if files.endswith('.tif'):
        filepath_out = os.path.join(folder_2, files)
        with rio.open(filepath_out) as input_raster_ndvi:
            ndvi = input_raster_ndvi.read(1)
            #print (ndvi)
        
        #fn = files[:10]
        a2 = np.nanmean(ndvi)
        lists2.append(a2)

folder_2 = "D:\\Carpe_outputs\\WW_analysis\\2017_WW_analysis\\comp_ww_wg_2020\\ndvi\\auf_stock"

for files in os.listdir(folder_2):
    if files.endswith('.tif'):
        filepath_out = os.path.join(folder_2, files)
        with rio.open(filepath_out) as input_raster_ndvi:
            ndvi = input_raster_ndvi.read(1)
            #print (ndvi)
        
        #fn = files[:10]
        a3 = np.nanmean(ndvi)
        lists3.append(a3)

folder_2 = "D:\\Carpe_outputs\\WW_analysis\\2017_WW_analysis\\comp_ww_wg_2020\\ndvi\\faenger1"

for files in os.listdir(folder_2):
    if files.endswith('.tif'):
        filepath_out = os.path.join(folder_2, files)
        with rio.open(filepath_out) as input_raster_ndvi:
            ndvi = input_raster_ndvi.read(1)
            #print (ndvi)
        
        #fn = files[:10]
        a4 = np.nanmean(ndvi)
        lists4.append(a4)
    
folder_2 = "D:\\Carpe_outputs\\WW_analysis\\2017_WW_analysis\\comp_ww_wg_2020\\ndvi\\gattb"

for files in os.listdir(folder_2):
    if files.endswith('.tif'):
        filepath_out = os.path.join(folder_2, files)
        with rio.open(filepath_out) as input_raster_ndvi:
            ndvi = input_raster_ndvi.read(1)
            #print (ndvi)
        
        #fn = files[:10]
        a5 = np.nanmean(ndvi)
        lists5.append(a5)

folder_2 = "D:\\Carpe_outputs\\WW_analysis\\2017_WW_analysis\\comp_ww_wg_2020\\ndvi\\kaempe1"

for files in os.listdir(folder_2):
    if files.endswith('.tif'):
        filepath_out = os.path.join(folder_2, files)
        with rio.open(filepath_out) as input_raster_ndvi:
            ndvi = input_raster_ndvi.read(1)
            #print (ndvi)
        
        #fn = files[:10]
        a6 = np.nanmean(ndvi)
        lists6.append(a6)

folder_2 = "D:\\Carpe_outputs\\WW_analysis\\2017_WW_analysis\\comp_ww_wg_2020\\ndvi\\Niegerts"

for files in os.listdir(folder_2):
    if files.endswith('.tif'):
        filepath_out = os.path.join(folder_2, files)
        with rio.open(filepath_out) as input_raster_ndvi:
            ndvi = input_raster_ndvi.read(1)
            #print (ndvi)
        
        #fn = files[:10]
        a7 = np.nanmean(ndvi)
        lists7.append(a7)

folder_2 = "D:\\Carpe_outputs\\WW_analysis\\2017_WW_analysis\\comp_ww_wg_2020\\ndvi\\wellen"

for files in os.listdir(folder_2):
    if files.endswith('.tif'):
        filepath_out = os.path.join(folder_2, files)
        with rio.open(filepath_out) as input_raster_ndvi:
            ndvi = input_raster_ndvi.read(1)
            #print (ndvi)
        
        #fn = files[:10]
        a8 = np.nanmean(ndvi)
        lists8.append(a8)

z = list(zip(file_name,lists,lists2,lists3,lists4,lists5,lists6,lists7,lists8))
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
y_val8 = [x[8] for x in z]
        
print(x_val)
plt.plot(x_val,y_val,"-r", Label = "An der Panzerstrasse")
plt.plot(x_val,y_val2,"-b", Label = "Auf dem Brink")
plt.plot(x_val,y_val3,"-b", Label = "Auf dem Stockum II")
plt.plot(x_val,y_val4,"-r", Label = "Fänger II")
plt.plot(x_val,y_val5,"-r", Label = "Gattberg I")
plt.plot(x_val,y_val6,"-b", Label = "Kämpe I")
plt.plot(x_val,y_val7,"-r", Label = "Niegerts")
plt.plot(x_val,y_val8,"-r", Label = "Wellenbreite")
# # plt.plot(x_val,y_val,'or', c = "b")
# plt.plot(x_val,y_val2, 'or', c = "b")
# plt.plot(x_val,y_val3,'or', c = "g")
# plt.plot(x_val,y_val4, 'or', c = "y")
# #plt.plot(x_val,y_val5,'or', c = "r")
# plt.plot(x_val,y_val6, 'or', c = "c")
# plt.plot(x_val,y_val7,'or', c = "m")
# plt.plot(x_val,y_val8, 'or', c = "k")
# plt.plot(x_val,y_val9, 'or', c = "r")
plt.legend(loc="upper left")
plt.ylim(0,0.8)
plt.xticks(rotation=45)
plt.title("Corn field")
#plt.xticks(rotation=45)
plt.show()      



