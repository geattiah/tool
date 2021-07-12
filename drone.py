import sys
import os
import shutil
import os
import rasterio as rio
import seaborn as sns
import numpy as py

tiff_file =  "D:\\Beispieldaten\\Multispektral\\langsenkamp_20200724_altum_46m_orthophoto.tif"

with rio.open(tiff_file) as input_raster:
    bandRed = input_raster.read(1)
    bandRed = input_raster.read(2)
    bandRed = input_raster.read(3)
    bandRed = input_raster.read(4)
    bandRed = input_raster.read(5)
    bandRed = input_raster.read(6)
    bandRed = input_raster.read(7)

