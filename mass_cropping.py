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
from pyproj import Proj, transform
import fiona
from fiona.crs import from_epsg                                                                      


folder = "/home/gift/Dropbox/carpe_data/tiffs"
output_folder = "/home/gift/Dropbox/carpe_data/georef_tiffs/"
def reproject():
    for files in os.listdir(folder):
        if files.endswith('.tif'):
            filepath = os.path.join(folder, files)
            input_raster = gdal.Open(filepath)
            output_raster = (os.path.join(output_folder, (str(files))[:-4] + '_geo_ref.tif'))
            gdal.Warp(output_raster , input_raster, dstSRS='EPSG:4326')

#reproject()

def crop(shapefile):

    with fiona.open(shapefile, "r") as shapefile:
        shapes = [feature["geometry"] for feature in shapefile]
        #print(shapes)

    for files in os.listdir(output_folder):
        if files.endswith('.tif'):
            filepath = os.path.join(output_folder, files)
            with rio.open(filepath) as src:
                out_image, out_transform = rio.mask.mask(src, shapes, crop=True)
                out_meta = src.meta

            out_meta.update({"driver": "GTiff",
                            "height": out_image.shape[1],
                            "width": out_image.shape[2],
                            "transform": out_transform})

            with rio.open(filepath + ".masked.tif", "w", **out_meta) as dest:
                dest.write(out_image)

    #out = rasterio.open("/home/gift/Dropbox/carpe_data/tiffs/cr_2020_06_01.tif.masked.tif")
    #plt.imshow(out.read(1), cmap='pink')
    #plt.show()
shapefile = "/home/gift/Dropbox/carpe_data/shapes/Ellerkamp.shp"
crop(shapefile)