import rasterio as rio
from rasterio.plot import plotting_extent,show
from rasterio.mask import mask
import fiona
from fiona.crs import from_epsg
import matplotlib.pyplot as plt
import numpy as np

shapefile = "D:\\carpe_prog_data\\farms\\Am_Halterner_Weg_1.shp"

with fiona.open(shapefile, "r") as shapefile:
    shapes = [feature["geometry"] for feature in shapefile]

filepath = "C:\\Users\\attiah\\Desktop\\eleva\\subset_0_of_2018_07_24_Am_Halterner_Weg_1_ndvi.tif"

with rio.open(filepath) as src:
    out_image, out_transform = rio.mask.mask(src, shapes, crop=True)
    out_meta = src.meta

out_meta.update({"driver": "GTiff",
                "height": out_image.shape[1],
                "width": out_image.shape[2],
                "transform": out_transform})

with rio.open(filepath + ".masked.tif", "w", **out_meta) as dest:
    dest.write(out_image)

out = "C:\\Users\\attiah\\Desktop\\eleva\\subset_0_of_2018_07_24_Am_Halterner_Weg_1_ndvi.tif.masked.tif.masked.tif"
with rio.open(out) as input_raster_ndvi:
    band = input_raster_ndvi.read(1)

cmap = plt.cm.gray
cmap.set_bad(color='white')

band = np.ma.masked_where(band < 0.05, band)

plt.imshow(band, interpolation='none', cmap=cmap)
#plt.imshow(p)
plt.clim(141,143.5)
cbar = plt.colorbar()
cbar.set_label('meters')
plt.title("Am_Halterner_Weg_1 - Elevation")
plt.show()


