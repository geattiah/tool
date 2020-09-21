import rasterio as rio
from rasterio.plot import plotting_extent,show
from rasterio.mask import mask
import fiona
from fiona.crs import from_epsg
import matplotlib.pyplot as plt
import numpy as np

raster = rio.open("D:\\data\\corn_2018\\tiff_all_bands\\2018_07_17_An_der_Panzerstrasse.tif")


def normalize(array):
    array_min, array_max = array.min(), array.max()
    return (array - array_min) / (array_max - array_min)

blue = raster.read(1)
red = raster.read(3)
green = raster.read(2)

# Normalize band DN
blue_norm = normalize(blue)
red_norm = normalize(red)
green_norm = normalize(green)

# Stack bands
rgb = np.dstack((red_norm, green_norm, blue_norm))

# View the color composite
plt.imshow(rgb)   
plt.show()