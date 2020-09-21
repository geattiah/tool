import rasterio as rio
from rasterio.plot import plotting_extent,show
from rasterio.mask import mask
import fiona
from fiona.crs import from_epsg
import matplotlib.pyplot as plt
import numpy as np

file_out = "C:\\Users\\attiah\\Desktop\\eleva\\subset_0_of_2018_07_24_Am_Halterner_Weg_1_ndvi.tif_dem.tif"

with rio.open(file_out) as ndnp:
    p = ndnp.read(1)

plt.imshow(p)
#plt.imshow(p)
plt.clim(140,143)
plt.colorbar()
#plt.title(str(files)[:-4])
plt.show()


