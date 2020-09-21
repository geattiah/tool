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


folder = "D:\\data\\vtebach1\\ndvi"

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

folder_2 = "D:\\data\\aufdembrik\\ndvi"

for files in os.listdir(folder_2):
    if files.endswith('.tif'):
        filepath_out = os.path.join(folder_2, files)
        with rio.open(filepath_out) as input_raster_ndvi:
            ndvi = input_raster_ndvi.read(1)
            #print (ndvi)
        
        #fn = files[5:7]
        a2 = np.nanmean(ndvi)
        lists2.append(a2)
        #file_name.append(fn)

# folder_2 = "D:\\Carpe_outputs\\Bundes3\\bund2\\2019\\ndvi"

# for files in os.listdir(folder_2):
#     if files.endswith('.tif'):
#         filepath_out = os.path.join(folder_2, files)
#         with rio.open(filepath_out) as input_raster_ndvi:
#             ndvi = input_raster_ndvi.read(1)
#             #print (ndvi)
        
#         #fn = files[:10]
#         a3 = np.nanmean(ndvi)
#         lists3.append(a3)

z = list(zip(file_name,lists,lists2))
print(lists)
print(file_name)
print(z)

x_val = [x[0] for x in z]
y_val = [x[1] for x in z]
y_val2 = [x[2] for x in z]
#y_val3 = [x[3] for x in z]

plt.plot(x_val,y_val,"-b", Label = "Körnermais")
plt.plot(x_val,y_val2,"-g", Label = "Winterweizen")
#plt.plot(x_val,y_val3,"-r", Label = "2019")

plt.plot(x_val,y_val,'or', c = "b")
plt.plot(x_val,y_val2, 'or', c = "g")
#plt.plot(x_val,y_val3,'or', c = "r")

plt.legend(loc="upper left")
plt.ylim(0,0.8)
plt.xticks(rotation=45)
plt.title("CROP TYPE")
#plt.xticks(rotation=45)
plt.show()  