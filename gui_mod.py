from osgeo import gdal
import os
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import shapely
from shapely import geos
from shapely.geometry import mapping
import geopandas as gpd
import rasterio as rio
from rasterio.plot import plotting_extent,show
from rasterio.mask import mask
#import earthpy as et
#import earthpy.spatial as es
#import earthpy.plot as ep
from tkinter import Tk, Text, TOP, BOTH, X, N, LEFT, StringVar, RIGHT, ttk, Listbox, END, EXTENDED, Scrollbar
from tkinter import MULTIPLE
from tkinter.ttk import Frame, Label, Entry, OptionMenu,Button, Combobox
from tkinter import filedialog


ds = rio.open("/home/gift/Dropbox/carpe_data/tiffs/2020_03_23.tif")
#raster = rio.open(ds)
#raster
#show(raster)
#band_4 = raster.read(3)
#band_8 = raster.read(7)

#show_band_4 = plt.imshow(band_4, cmap='pink')
#show_band_8 = plt.imshow(band_8, cmap='pink')
#plt.show()
from pyproj import Proj, transform
import fiona
from fiona.crs import from_epsg
import rasterio
import rasterio.mask


#If you want to work with the GeoJSON forma


with fiona.open("/home/gift/Dropbox/carpe_data/shapes/Ellerkamp.shp", "r") as shapefile:
    shapes = [feature["geometry"] for feature in shapefile]
    #print(shapes)


#print(yard)

#shapes = [x for x in shapes if x is not None]

with rasterio.open("/home/gift/Dropbox/carpe_data/tiffs/cr_2020_06_01.tif") as src:
    out_image, out_transform = rasterio.mask.mask(src, shapes, crop=True)
    out_meta = src.meta

out_meta.update({"driver": "GTiff",
                 "height": out_image.shape[1],
                 "width": out_image.shape[2],
                 "transform": out_transform})

with rasterio.open("/home/gift/Dropbox/carpe_data/tiffs/cr_2020_06_01.tif.masked.tif", "w", **out_meta) as dest:
    dest.write(out_image)

out = rasterio.open("/home/gift/Dropbox/carpe_data/tiffs/cr_2020_06_01.tif.masked.tif")
plt.imshow(out.read(1), cmap='pink')
plt.show()


#tif = "/home/gift/Dropbox/carpe_data/tiffs/2020_06_01.tif"
#out_tiff = "/home/gift/Dropbox/carpe_data/tiffs/2020_06_01_crop.tif"
#tiff = tif.crs
#print(str(tiff))
#with rio.open(tif) as src:
    #pre_arr = src.read(1)


#show((out_image, 4), cmap='terrain')

#shapes = "/home/gift/Dropbox/carpe_data/shapes/Binnenkamp_2.shp"
#print(shapes.schema)

#crop_extent = gpd.read_file(shapes)


#print('crop extent crs: ', crop_extent.crs)
#print('tiff: ', pre_arr.crs)
#shapes = shapes['geometry'].to_crs(crs = data.crs.data)