import rasterio
from rasterio.enums import Resampling

# referenceFile = "D:\\carpe_prog_data\\tiffs\\2017_02_02.tif"
# reference = gdal.Open(referenceFile, 0)  # this opens the file in only reading mode
# referenceTrans = reference.GetGeoTransform()
# x_res = referenceTrans[1]
# y_res = -referenceTrans[5]  # make sure this value is positive

# specify input and output filenames
inputFile = "D:\\carpe_prog_data\\elevation\\farm_slope.tif"
outputFile = "D:\\carpe_prog_data\\elevation\\farm_slope\\farm_slope_res.tif"

# call gdal Warp
#kwargs = {"format": "GTiff", "xRes": x_res, "yRes": y_res}
#ds = gdal.Translate(outputFile, outputFile, xres=10, yres=10, resampleAlg="bilinear", format='vrt')


input_Dir = "D:\\carpe_prog_data\\elevation\\farm_slope.tif"
#src = rasterio.open(input_Dir) 
#show(src,cmap="magma")

upscale_factor = 1/3

with rasterio.open(input_Dir) as dataset:
    
    # resample data to target shape
    data = dataset.read(
        out_shape=(
            dataset.count,
            int(dataset.height * upscale_factor),
            int(dataset.width * upscale_factor)
        ),
        resampling=Resampling.bilinear
    )

    # scale image transform
    transform = dataset.transform * dataset.transform.scale(
        (dataset.width / data.shape[-1]),
        (dataset.height / data.shape[-2])
    )

    