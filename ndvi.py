import numpy
import rasterio

import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap

viridis = cm.get_cmap('viridis', 12)
print(viridis)
#matplotlib inline
#import subprocess

# Read raster bands directly to Numpy arrays.
tiff_image = rasterio.open("C:\\Users\\attiah\\Documents\\Carpe_output\\Am_hal\\ndvi\\2017_02_02_Am_Halterner_Weg_1_ndvi.tif")
bandRed = tiff_image.read(4)
bandNir = tiff_image.read(8)

#ndvi = numpy.zeros(tiff_image.shape, dtype=rasterio.uint16)

numpy.seterr(divide='ignore', invalid='ignore')

ndvi_upper = (bandNir + bandRed)
ndvi_lower = (bandNir.astype(float) - bandRed.astype(float))

ndvi = ndvi_lower / ndvi_upper

kwargs = tiff_image.meta
kwargs.update(
    dtype=rasterio.float32,
    count=1,
    compress='lzw')

with rasterio.open('/home/gift/Dropbox/example-total.tif', 'w', **kwargs) as dst:
    dst.write_band(1, ndvi.astype(rasterio.float32))


mpl.colors.LinearSegmentedColormap.from_list(
        'green2red', ['green', 'orangered'])


plt.imshow(ndvi)
plt.show()

