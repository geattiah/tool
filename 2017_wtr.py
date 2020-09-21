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
lists9 = []
file_name = []

folder = "D:\\Carpe_outputs\\2017_wtr_ana\\ndvi\\hof"

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

folder_2 = "D:\\Carpe_outputs\\2017_wtr_ana\\ndvi\\nieg"

for files in os.listdir(folder_2):
    if files.endswith('.tif'):
        filepath_out = os.path.join(folder_2, files)
        with rio.open(filepath_out) as input_raster_ndvi:
            ndvi = input_raster_ndvi.read(1)
            #print (ndvi)
        
        #fn = files[:10]
        a2 = np.nanmean(ndvi)
        lists2.append(a2)

# folder_2 = "D:\\Carpe_outputs\\2019_Corn-analysis\\benni1\\ndvi"

# for files in os.listdir(folder_2):
#     if files.endswith('.tif'):
#         filepath_out = os.path.join(folder_2, files)
#         with rio.open(filepath_out) as input_raster_ndvi:
#             ndvi = input_raster_ndvi.read(1)
#             #print (ndvi)
        
#         #fn = files[:10]
#         a3 = np.nanmean(ndvi)
#         lists3.append(a3)

# folder_2 = "D:\\Carpe_outputs\\2019_Corn-analysis\\benni2\\ndvi"

# for files in os.listdir(folder_2):
#     if files.endswith('.tif'):
#         filepath_out = os.path.join(folder_2, files)
#         with rio.open(filepath_out) as input_raster_ndvi:
#             ndvi = input_raster_ndvi.read(1)
#             #print (ndvi)
        
#         #fn = files[:10]
#         a4 = np.nanmean(ndvi)
#         lists4.append(a4)
    
# folder_2 = "D:\\Carpe_outputs\\2019_Corn-analysis\\bundes_3\\ndvi"

# for files in os.listdir(folder_2):
#     if files.endswith('.tif'):
#         filepath_out = os.path.join(folder_2, files)
#         with rio.open(filepath_out) as input_raster_ndvi:
#             ndvi = input_raster_ndvi.read(1)
#             #print (ndvi)
        
#         #fn = files[:10]
#         a5 = np.nanmean(ndvi)
#         lists5.append(a5)

# folder_2 = "D:\\Carpe_outputs\\2019_Corn-analysis\\hof_niegerts\\ndvi"

# for files in os.listdir(folder_2):
#     if files.endswith('.tif'):
#         filepath_out = os.path.join(folder_2, files)
#         with rio.open(filepath_out) as input_raster_ndvi:
#             ndvi = input_raster_ndvi.read(1)
#             #print (ndvi)
        
#         #fn = files[:10]
#         a6 = np.nanmean(ndvi)
#         lists6.append(a6)

# folder_2 = "D:\\Carpe_outputs\\2019_Corn-analysis\\niegets2\\ndvi"

# for files in os.listdir(folder_2):
#     if files.endswith('.tif'):
#         filepath_out = os.path.join(folder_2, files)
#         with rio.open(filepath_out) as input_raster_ndvi:
#             ndvi = input_raster_ndvi.read(1)
#             #print (ndvi)
        
#         #fn = files[:10]
#         a7 = np.nanmean(ndvi)
#         lists7.append(a7)

# folder_2 = "D:\\Carpe_outputs\\2019_Corn-analysis\\pingelklogen\\ndvi"

# for files in os.listdir(folder_2):
#     if files.endswith('.tif'):
#         filepath_out = os.path.join(folder_2, files)
#         with rio.open(filepath_out) as input_raster_ndvi:
#             ndvi = input_raster_ndvi.read(1)
#             #print (ndvi)
        
#         #fn = files[:10]
#         a8 = np.nanmean(ndvi)
#         lists8.append(a8)

# folder_2 = "D:\\Carpe_outputs\\2019_Corn-analysis\\vehr_bach\\ndvi"

# for files in os.listdir(folder_2):
#     if files.endswith('.tif'):
#         filepath_out = os.path.join(folder_2, files)
#         with rio.open(filepath_out) as input_raster_ndvi:
#             ndvi = input_raster_ndvi.read(1)
#             #print (ndvi)
        
#         #fn = files[:10]
#         a9 = np.nanmean(ndvi)
#         lists9.append(a9)


z = list(zip(file_name,lists,lists2))
print(lists)
print(file_name)
print(z)

x_val = [x[0] for x in z]
y_val = [x[1] for x in z]
y_val2 = [x[2] for x in z]
# y_val3 = [x[3] for x in z]
# y_val4 = [x[4] for x in z]
# y_val5 = [x[5] for x in z]
# y_val6 = [x[6] for x in z]
# y_val7 = [x[7] for x in z]
# y_val8 = [x[8] for x in z]
# y_val9 = [x[9] for x in z]
        
print(x_val)
plt.plot(x_val,y_val,"-b", Label = "Am Teich II")
plt.plot(x_val,y_val2,"-b", Label = "Auf dem Stockum I")
#plt.plot(x_val,y_val3,"-g", Label = "Binnenkamp - 1")
# plt.plot(x_val,y_val4,"-y", Label = "Binnenkamp - 2")
# #plt.plot(x_val,y_val5,"-r", Label = "Bundesstrasse III")
# plt.plot(x_val,y_val6,"-c", Label = "Hof Niegerts")
# plt.plot(x_val,y_val7,"-m", Label = "Niegerts II")
# plt.plot(x_val,y_val8,"-k", Label = "Pingelglocken")
# plt.plot(x_val,y_val9,"-r", Label = "Vehrter Bach I")
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
plt.show()   
#plt.xticks(rotatio