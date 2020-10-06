import sys
import os
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np
from tkinter import Tk, Text, TOP, BOTH, X, N, LEFT, StringVar, RIGHT, ttk, Listbox, END, EXTENDED, Scrollbar
from tkinter import MULTIPLE
from tkinter.ttk import Frame, Label, Entry, OptionMenu,Button, Combobox
from tkinter import filedialog
from osgeo import gdal
import fnmatch
import fiona
from fiona.crs import from_epsg
import rasterio as rio
from rasterio.plot import plotting_extent,show
from rasterio.mask import mask

tiff_folder = "D:\\carpe_prog_data\\tiffs"  
shapefile_folder = "D:\\carpe_prog_data\\farms" 
elev_folder = "D:\\carpe_prog_data\\elevation"
elevation_tiff = "D:\\carpe_prog_data\\elevation\\farm_slope.tif"
soil_folder = "D:\\carpe_prog_data\\soil"
soilmap = "D:\\carpe_prog_data\\soil\\soilmap.tif"
elev_res = "D:\\carpe_prog_data\\elevation\\farm_slope_proj_Res.tif"
rain = pd.read_csv("D:\\carpe_prog_data\\weather\\rain.csv") 
temp = pd.read_csv("D:\\carpe_prog_data\\weather\\temp.csv") 

class Carpe(Frame):
    def __init__(self):
        super().__init__()

        self.GUI()
        self.heading_view()
        self.location_view()
        self.farm_heading_view()
        self.farm_view()
        self.date_heading_view()
        self.date_view()
        self.proxit_view()

    def GUI(self):
        self.master.title("Carpe Memoriam")
        self.pack(fill=BOTH, expand=True)

    # specifications for view of heading
    def heading_view(self):
        heading_frame = Frame(self)
        heading_frame.pack(fill=X)

        heading_label = Label(heading_frame, text="Carpe Memoriam", width=17, font = (None, 15))
        heading_label.pack()

    # location frame view and parameters
    def location_view(self):
        location_frame = Frame(self)
        location_frame.pack(fill=X)

        global folder_path
        folder_path = StringVar() 
        location_label = Label(location_frame, text = "Folder path", width=17, font = (None, 12))
        location_label.pack(side=LEFT, padx=20, pady=10)
        
        global location_entry
        location_entry = Entry(location_frame, textvariable = folder_path, width = 40)
        location_entry.pack(side=LEFT, padx=5, pady=10,)

        browse = ttk.Button(location_frame, text="Browse", command=self.browse_button)
        browse.pack(side=LEFT, padx=20, pady=10)
        
    # set browse button to select folder
    def browse_button(self):
        filename = filedialog.askdirectory()
        folder_path.set(filename)
              
    # Heading that apperas in farm selection view    
    def farm_heading_view(self):
        farm_frame = Frame(self)
        farm_frame.pack(fill=X)

        farm_label = Label(farm_frame, text="Select Field Name", width=17, font = (None, 12))
        farm_label.pack( padx=20, pady=10)       

    # farm listbox
    def farm_view(self):
        farm_frame = Frame(self)
        farm_frame.pack(fill=X)

        farm_label = Label(farm_frame, text="Field:", width=17, font = (None, 12))
        farm_label.pack(side=LEFT, padx=20, pady=10)

        farm_folder =  shapefile_folder
        global farm_list
        farm_list = [files for files in os.listdir(farm_folder)if files.endswith('.shp')]
        farm_list.sort()
        
        global farm_box
        farm_box = Listbox(farm_frame, width = 15, height = 5, selectmode = EXTENDED)
        farm_box.pack(side = LEFT, padx=5, pady=10)

        scrollbar = Scrollbar(farm_frame, orient="vertical",command=farm_box.yview)
        scrollbar.pack(side="left", fill="y")

        farm_box.config(yscrollcommand=scrollbar.set)
          
        for item in farm_list:
            item = os.path.splitext(item)[0]
            farm_box.insert(END, item)

        add_button = Button(farm_frame, text = "Add", command = self.add_farm,width =5)
        add_button.pack(side = LEFT,padx= 5)
        
        global sel_box_farms
        sel_box_farms = Listbox(farm_frame, width = 15, height = 5,selectmode = EXTENDED)
        sel_box_farms.pack(side = LEFT, padx= 5, pady=10)
       # sel_box_farms.bind("<<ListboxSelected>>")

        scrollbar = Scrollbar(farm_frame, orient="vertical",command=sel_box_farms.yview)
        scrollbar.pack(side="left", fill="y")

        sel_box_farms.config(yscrollcommand=scrollbar.set)

        remove_button= Button(farm_frame, text = "Delete", command = self.delete_farm,width =7)
        remove_button.pack(side = LEFT,padx= 5)
    
    #Button which adds dates to listbox
    def add_farm(self):
        global sel_farm
        sel_farm = farm_box.curselection()
        for item in sel_farm:
            farm_files = farm_box.get(item)
            sel_files = sel_box_farms.get(0, END)
            if farm_files not in sel_files:
                sel_box_farms.insert(END, farm_box.get(item))

    #Button which deletes farms in listbox
    def delete_farm(self):
        global rem_farm
        rem_farm = sel_box_farms.curselection()
        for item in rem_farm:
            sel_box_farms.insert(END, sel_box_farms.delete(item))  

    # Heading for date entries
    def date_heading_view(self):
        date_frame = Frame(self)
        date_frame.pack(fill=X)

        date_label = Label(date_frame, text="Select Date(s)", width=17, font = (None, 12))
        date_label.pack( padx=20, pady=10)       

    # Date listbox
    def date_view(self):
        date_frame = Frame(self)
        date_frame.pack(fill=X)

        date_label = Label(date_frame, text="Dates:", width=17, font = (None, 12))
        date_label.pack(side=LEFT, padx=20, pady=10)

        date_folder =  tiff_folder 
        global date_list
        date_list = [files for files in os.listdir(date_folder)if files.endswith('.tif')]
        date_list.sort()
        
        global date_box
        date_box = Listbox(date_frame, width = 15, height = 10, selectmode = EXTENDED)
        date_box.pack(side = LEFT, padx=5, pady=10)

        scrollbar = Scrollbar(date_frame, orient="vertical",command=date_box.yview)
        scrollbar.pack(side="left", fill="y")

        date_box.config(yscrollcommand=scrollbar.set)
          
        for item in date_list:
            item = os.path.splitext(item)[0]
            date_box.insert(END, item)


        add_button = Button(date_frame, text = "Add", command = self.add_date,width =5)
        add_button.pack(side = LEFT,padx= 5)
        
        global sel_box
        sel_box = Listbox(date_frame, width = 15, height = 10, selectmode = EXTENDED)
        sel_box.pack(side = LEFT, padx= 5, pady=10)
       # sel_box.bind("<<ListboxSelected>>")

        scrollbar = Scrollbar(date_frame, orient="vertical",command=sel_box.yview)
        scrollbar.pack(side="left", fill="y")

        sel_box.config(yscrollcommand=scrollbar.set)

        remove_button= Button(date_frame, text = "Delete", command = self.delete_date,width =7)
        remove_button.pack(side = LEFT,padx= 5)
    
    # Button which adds dates to listbox
    def add_date(self):
        global sel_date
        sel_date = date_box.curselection()
        for item in sel_date:
            date_files = date_box.get(item)
            sel_files = sel_box.get(0, END)
            if date_files not in sel_files:
                sel_box.insert(END, date_box.get(item))
    
    # Button which deleted dates in listbox
    def delete_date(self):
        global rem_date
        rem_date = sel_box.curselection()
        for item in rem_date:
            sel_box.insert(END, sel_box.delete(item))


    def proxit_view(self):
        proxit_frame = Frame(self)
        proxit_frame.pack(fill=X)

        process_button = Button(proxit_frame, text = "PROCESS", command = self.process )
        process_button.pack(padx = (150), pady = 10, side = LEFT)

        exit_button = Button(proxit_frame, text = "EXIT", command = self.close )
        exit_button.pack(padx = 120, pady = 10, side = LEFT)
    
    
    def process(self):
        self.create_subset()
        self.cal()
        self.elevation()
        self.get_soil()
        self.stack()
       

    # close the programe
    def close(self):
        root.quit()
    
    # Crops the raster file to the boudary of shape files
    def create_subset(self):
        root.iconify() 
        global output_folder 
        output_folder = folder_path.get()
        global process_folder
        process_folder = os.path.join(output_folder, 'dump')
        os.mkdir(process_folder)
    
        global shape_name
        shape_name = sel_box_farms.get(0,END)
        cropfiles = [item for item in shape_name]
        
        global crop_shapes
        crop_shapes = os.listdir(shapefile_folder)
        
        r = sel_box.get(0,END)
        tiff_dates = [item for item in r]

        folder_tiffs = os.listdir(tiff_folder)
        
        for files in folder_tiffs:
            for fname in tiff_dates:
                if fname in files and files.endswith('.tif'):
                    filepath = os.path.join(tiff_folder, files)
                    input_raster = gdal.Open(filepath)
                    output_raster = (os.path.join(process_folder, files))
                    gdal.Warp(output_raster , input_raster, dstSRS='EPSG:4326')
     
        global tiff_allbands_folder
        tiff_allbands_folder = os.path.join(output_folder, 'tiff_all_bands')
        os.mkdir(tiff_allbands_folder)

        for files in os.listdir(process_folder):
            if files.endswith('.tif'):
                filepath = os.path.join(process_folder, files)   
                for cfiles in crop_shapes:
                    for f_name in cropfiles:
                        if f_name in cfiles and cfiles.endswith('.shp'):
                            global shapepath
                            shapepath = os.path.join(shapefile_folder, cfiles)
                            with fiona.open(shapepath, "r") as shapefile:
                                shapes = [feature["geometry"] for feature in shapefile]
          
                            with rio.open(filepath) as src:
                                out_image, out_transform = rio.mask.mask(src, shapes, crop=True)
                                out_meta = src.meta

                            out_meta.update({"driver": "GTiff",
                                            "height": out_image.shape[1],
                                            "width": out_image.shape[2],
                                            "transform": out_transform})

                            with rio.open(os.path.join(tiff_allbands_folder,files[:-4]) + "_" + f_name + ".tif", "w", **out_meta) as dest:
                                dest.write(out_image)

    def cal(self):
        global indices_folder
        indices_folder = os.path.join(output_folder, 'indices')
        os.mkdir(indices_folder)
        for files in os.listdir(tiff_allbands_folder):
            if files.endswith('.tif'):
                filepath_out = os.path.join(tiff_allbands_folder, files)
                with rio.open(filepath_out) as input_raster:
                    bandRed = input_raster.read(3)
                    bandNir = input_raster.read(7)
                    bandSwir = input_raster.read(9)
                    bandBlue = input_raster.read(1)
                
                np.seterr(divide='ignore', invalid='ignore')

                ndvi_upper = (bandNir + bandRed)
                ndvi_lower = (bandNir.astype(float) - bandRed.astype(float))
    
                base = 0.05
                ndvi = ndvi_lower / ndvi_upper
                ndvi = np.round(base*np.around(ndvi/base),2)

                lai_upper = 2.5 * ((bandNir * 0.0001) - (bandRed * 0.0001))
                lai_lower = ((bandNir* 0.0001) + 6 *(bandRed* 0.0001) - 7.5 * (bandBlue*0.0001) + 1)

                evi = (lai_upper) / (lai_lower)
                lai = (3.618 * evi - 0.118)
                lai = np.round(base*np.around(lai/base),2)

                ndmi_upper = (bandNir + bandSwir)
                ndmi_lower = (bandNir.astype(float) - bandSwir.astype(float))
    
                ndmi = ndmi_lower / ndmi_upper
                ndmi = np.round(base*np.around(ndmi/base),2)

                kwargs = input_raster.meta
                kwargs.update(
                    dtype=rio.float32,
                    count=1,
                    compress='lzw')

                with rio.open(os.path.join(indices_folder,files[:-4]) + "_" + "NDVI" + ".tif", 'w', **kwargs) as dst:
                    dst.write_band(1, ndvi.astype(rio.float32))

                with rio.open(os.path.join(indices_folder,files[:-4]) + "_" + "NDMI" + ".tif", 'w', **kwargs) as dst:
                    dst.write_band(1, ndmi.astype(rio.float32))

                with rio.open(os.path.join(indices_folder,files[:-4]) + "_" + "LAI" + ".tif", 'w', **kwargs) as dst:
                    dst.write_band(1, lai.astype(rio.float32))
            
    def elevation(self):
        cropfiles = [item for item in shape_name]
        ele_interim = os.path.join(output_folder, 'ele_interim')
        os.mkdir(ele_interim)
        #elevation_folder = os.path.join(output_folder, 'elevation')
        #os.mkdir(elevation_folder)

        input_raster = gdal.Open(elev_res)
        output_raster = (os.path.join(elev_folder, "farm_slope_Res.tif"))
        gdal.Warp(output_raster , input_raster, dstSRS='EPSG:4326')

        for crfiles in crop_shapes:
            for fa_name in cropfiles:
                if fa_name in crfiles and crfiles.endswith('.shp'):
                    shape_path = os.path.join(shapefile_folder, crfiles)
                    with fiona.open(shape_path, "r") as shapefile:
                        shapes = [feature["geometry"] for feature in shapefile]

                    with rio.open(output_raster) as src:
                        out_image, out_transform = rio.mask.mask(src, shapes, crop=True)
                        out_meta = src.meta

                    out_meta.update({"driver": "GTiff",
                            "height": out_image.shape[1],
                            "width": out_image.shape[2],
                            "transform": out_transform})

                    with rio.open(os.path.join(ele_interim,crfiles[:-4]) + ".tif", "w", **out_meta) as dest:
                        dest.write(out_image)
        
        for files in os.listdir(ele_interim):
            if files.endswith('.tif'):
                filepath_out = os.path.join(ele_interim, files)

                np.seterr(divide='ignore', invalid='ignore')

                with rio.open(filepath_out) as input_raster:
                        bandSlope = input_raster.read(1)
                
                slope = bandSlope / 1

                kwargs = input_raster.meta
                kwargs.update(
                    dtype=rio.float32,
                    count=1,
                    compress='lzw')

                with rio.open(os.path.join(indices_folder,files[:-4]) + "_" + "SLOPE" + ".tif", 'w', **kwargs) as dst:
                    dst.write_band(1, slope.astype(rio.float32))





    def get_soil(self):
        cropfiles = [item for item in shape_name]
        soil_interim = os.path.join(output_folder, 'soil_interim')
        os.mkdir(soil_interim)

        input_raster = gdal.Open(soilmap)
        output_raster = (os.path.join(soil_folder, "soilmap_proj.tif"))
        gdal.Warp(output_raster , input_raster, dstSRS='EPSG:4326')

        for crfiles in crop_shapes:
            for fa_name in cropfiles:
                if fa_name in crfiles and crfiles.endswith('.shp'):
                    shape_path = os.path.join(shapefile_folder, crfiles)
                    with fiona.open(shape_path, "r") as shapefile:
                        shapes = [feature["geometry"] for feature in shapefile]

                    with rio.open(output_raster) as src:
                        out_image, out_transform = rio.mask.mask(src, shapes, crop=True)
                        out_meta = src.meta

                    out_meta.update({"driver": "GTiff",
                            "height": out_image.shape[1],
                            "width": out_image.shape[2],
                            "transform": out_transform})

                    with rio.open(os.path.join(soil_interim,crfiles[:-4]) + ".tif", "w", **out_meta) as dest:
                        dest.write(out_image)
        
        
        for files in os.listdir(soil_interim):
            if files.endswith('.tif'):
                filepath_out = os.path.join(soil_interim, files)

                np.seterr(divide='ignore', invalid='ignore')

                with rio.open(filepath_out) as input_raster:
                        bandSoil = input_raster.read(1)
                
                soil = bandSoil / 1

                kwargs = input_raster.meta
                kwargs.update(
                    dtype=rio.float32,
                    count=1,
                    compress='lzw')

                with rio.open(os.path.join(indices_folder,files[:-4]) + "_" + "SOIL" + ".tif", 'w', **kwargs) as dst:
                    dst.write_band(1, soil.astype(rio.float32))


                
            
     
    def stack(self):
        global stack_folder  
        stack_folder = os.path.join(output_folder,'stack')
        os.mkdir(stack_folder)
        list = os.listdir(indices_folder)
        list = [os.path.join(indices_folder, item) for item in list] 
        print(list)

        #Read metadata of first file
        with rio.open(list[0]) as src0:
            meta = src0.meta

        # Update meta to reflect the number of layers
        meta.update(count = len(list))

        # Read each layer and write it to stack
        with rio.open(os.path.join(stack_folder, 'stack.tif'), 'w', **meta) as dst:
            for id, layer in enumerate(list, start=1):
                with rio.open(layer) as src1:
                    dst.write_band(id, src1.read(1))

    def equ1(self):
        stackfile = os.path.join(stack_folder, stack.tif )
        with rio.open(stackfile) as input_raster:
            lai = input_raster.read(1)
            ndmi = input_raster.read(2)
            ndvi = input_raster.read(3)
            slope = input_raster.read(4)
            soil = input_raster.read(5)
            
 






def main():
    global root
    root = Tk()
    root.geometry("700x700+500+100")
    app = Carpe()
    root.mainloop()


if __name__ == '__main__':
    main()

