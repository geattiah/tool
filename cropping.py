from osgeo import gdal

filename = "/home/gift/Dropbox/carpe_data/tiffs/2020_06_01.tif"
output_raster = "/home/gift/Dropbox/carpe_data/tiffs/cr_2020_06_01.tif"
input_raster = gdal.Open(filename)
gdal.Warp(output_raster , input_raster, dstSRS='EPSG:4326')