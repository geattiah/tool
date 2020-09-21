import os
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from shapely.geometry import mapping
#import geopandas as gpd
import rasterio as rio
#from rio.plot import plotting_extent
#from rio.mapipsk import mask
#import earthpy as et
plt.show()
#import earthpy.spatial as es
#import earthpy.plot as ep
from tkinter import Tk, Text, TOP, BOTH, X, N, LEFT, StringVar, RIGHT, ttk, Listbox, END, EXTENDED, Scrollbar, BOTTOM, W
from tkinter import MULTIPLE
from tkinter.ttk import Frame, Label, Entry, OptionMenu,Button, Combobox
plt.show()
from tkinter import filedialog
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
import matplotlib.colors as mcolors
viridis = cm.get_cmap('viridis', 12)
print(viridis)


a = rio.open("C:\\Users\\attiah\\Documents\\Carpe_output\\Am_hal\\ndvi\\2017_02_02_Am_Halterner_Weg_1_ndvi.tif") 
d = a.read(1)

#b = rio.open("/home/gift/Dropbox/try/dump/2018_09_05_Am_Hof_I_ndvi.tif") 
#e = b.read(1)

#c = rio.open("/home/gift/Dropbox/try/dump/2018_07_27_Am_Hof_I_ndvi.tif") 
#f= c.read(1)

# viridis = cm.get_cmap('viridis', 256)
# newcolors = viridis(np.linspace(0, 1, 256))
# pink = np.array([248/256, 24/256, 148/256, 1])
# newcolors[:25, :] = pink
# newcmp = ListedColormap(newcolors)

# print(viridis(0.56))

# cmap = mcolors.ListedColormap(d)
# data = np.random.rand(10,10)
# plt.imshow(data, cmap=cmap)

#caxis([0 ,1])
fig, axes = plt.subplots(nrows=1, ncols=1, sharex=True, sharey=True)

plt.imshow(d)
plt.clim(0,1)
#plt.colorbar(boundaries=np.linspace(0, 1, 10, endpoint=True))
plt.colorbar()
plt.show()

#plt.imshow(d)
#plt.show()

#plt.imshow(e)
#plt.show()

#plt.imshow(f)
#plt.show()

