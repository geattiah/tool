import rasterio as rio
from rasterio.plot import plotting_extent,show
from rasterio.mask import mask
import fiona
from fiona.crs import from_epsg
import matplotlib.pyplot as plt
import numpy as np

bandnames = ["Blue", "Green", "Red", "Red_Edge_1", "Red_Edge_2", "Red_Edge_3", "NIR", "NIR_2", "SWIR", "SWIR_2"]

#List = []

raster = "D:\\data\\a\\tiff_all_bands\\2018_08_06_Am_Halterner_Weg_2.tif"
with rio.open(raster) as input_raster:
    bandblue = input_raster.read(1)
    bandgreen = input_raster.read(2)
    bandred = input_raster.read(3)
    bandred1 = input_raster.read(4)
    bandred2 = input_raster.read(5)
    bandred3 = input_raster.read(6)
    bandnir = input_raster.read(7)
    bandnir_a = input_raster.read(8)
    bandswir = input_raster.read(9)
    bandswir2 = input_raster.read(10)

    np.seterr(divide='ignore', invalid='ignore')

blue = np.round(np.nanmean(bandblue))
green = np.round(np.nanmean(bandgreen))
red = np.round(np.nanmean(bandred))
red1 = np.round(np.nanmean(bandred1))
red2 = np.round(np.nanmean(bandred2))
red3 = np.round(np.nanmean(bandred3))
nir = np.round(np.nanmean(bandnir))
nir_a = np.round(np.nanmean(bandnir_a))
swir = np.round(np.nanmean(bandswir))
swir2 = np.round(np.nanmean(bandswir2))

List = [blue,green,red,red1,red2,red3,nir,nir_a,swir,swir2]
print(List)

plt.plot(bandnames,List)
plt.plot(bandnames,List,'or', c = "b")
plt.xticks(rotation=45)
plt.show() 


