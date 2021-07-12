#Package neede to be installed
# pip install Pillow
# pip install ratserio, fiona
# pip install from osgeo import gdal

import sys,os,fnmatch,fiona,shutil
import matplotlib.pyplot as plt
import numpy as np
from tkinter import Tk, Text, TOP, BOTH, X, N, LEFT, StringVar, RIGHT, ttk, Listbox, END, EXTENDED, Scrollbar
from tkinter import MULTIPLE
from tkinter.ttk import Frame, Label, Entry, OptionMenu,Button, Combobox
from tkinter import filedialog
from osgeo import gdal
from fiona.crs import from_epsg
import rasterio as rio
from rasterio.plot import plotting_extent,show
from rasterio.mask import mask
import warnings

#Define folder locations
tiff_folder = "/home/gift/Documents/carpe_prog_data/tiffs" #"D:\\carpe_prog_data\\tiffs"  
shapefile_folder = "/home/gift/Documents/carpe_prog_data/farms" #"D:\\carpe_prog_data\\farms" 
elev_folder = "/home/gift/Documents/carpe_prog_data/elevation" #"D:\\carpe_prog_data\\elevation"
elevation_tiff = "/home/gift/Documents/carpe_prog_data/elevation/farm_slope.tif" #"D:\\carpe_prog_data\\elevation\\farm_slope.tif"

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
        self.para_heading_view()
        self.para_view()
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

    def para_heading_view(self):
        para_frame = Frame(self)
        para_frame.pack(fill=X)

        para_label = Label(para_frame, text="Select Parameter", width=17, font = (None, 12))
        para_label.pack( padx=20, pady=10)       

    # para listbox
    def para_view(self):
        para_frame = Frame(self)
        para_frame.pack(fill=X)

        para_label = Label(para_frame, text="Parameter:", width=17, font = (None, 12))
        para_label.pack(side=LEFT, padx=20, pady=10)

        para_folder =  tiff_folder 
        global para_list
        para_list = ["NDVI", "EVI", "LAI","Elevation", "Reflection", "Avg_NDVI", "NDMI", "SAVI", "Avg_NDMI"]
        para_list.sort()
        
        global para_box
        para_box = Listbox(para_frame, width = 15, height = 5, selectmode = EXTENDED)
        para_box.pack(side = LEFT, padx=5, pady=10)

        scrollbar = Scrollbar(para_frame, orient="vertical",command=para_box.yview)
        scrollbar.pack(side="left", fill="y")

        para_box.config(yscrollcommand=scrollbar.set)
          
        for item in para_list:
            item = os.path.splitext(item)[0]
            para_box.insert(END, item)


        add_button = Button(para_frame, text = "Add", command = self.add_para,width =5)
        add_button.pack(side = LEFT,padx= 5)
        
        global par_box
        par_box = Listbox(para_frame, width = 15, height = 5, selectmode = EXTENDED)
        par_box.pack(side = LEFT, padx= 5, pady=10)
       # sel_box.bind("<<ListboxSelected>>")

        scrollbar = Scrollbar(para_frame, orient="vertical",command=par_box.yview)
        scrollbar.pack(side="left", fill="y")

        par_box.config(yscrollcommand=scrollbar.set)

        remove_button= Button(para_frame, text = "Delete", command = self.delete_para,width =7)
        remove_button.pack(side = LEFT,padx= 5)
    
    # Button which adds paras to listbox
    def add_para(self):
        global sel_para
        sel_para = para_box.curselection()
        for item in sel_para:
            para_files = para_box.get(item)
            par_files = par_box.get(0, END)
            if para_files not in par_files:
                par_box.insert(END, para_box.get(item))
    
    # Button which deleted paras in listbox
    def delete_para(self):
        global rem_para
        rem_para = par_box.curselection()
        for item in rem_para:
            par_box.insert(END, par_box.delete(item))


    def proxit_view(self):
        proxit_frame = Frame(self)
        proxit_frame.pack(fill=X)

        process_button = Button(proxit_frame, text = "PROCESS", command = self.process )
        process_button.pack(padx = (150), pady = 10, side = LEFT)

        exit_button = Button(proxit_frame, text = "EXIT", command = self.close )
        exit_button.pack(padx = 120, pady = 10, side = LEFT)

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
                    warnings.filterwarnings("ignore")
     
        global tiff_allbands_folder
        tiff_allbands_folder = os.path.join(output_folder, 'tiff_all_bands')
        os.mkdir(tiff_allbands_folder)
        warnings.filterwarnings("ignore")

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
    
    def ndvi(self):
        for item in para_name:
            if item == "NDVI":
                ndvi_folder = os.path.join(output_folder, 'ndvi')
                os.mkdir(ndvi_folder)
                for files in os.listdir(tiff_allbands_folder):
                    if files.endswith('.tif'):
                        filepath_out = os.path.join(tiff_allbands_folder, files)
                        with rio.open(filepath_out) as input_raster_ndvi:
                            bandRed = input_raster_ndvi.read(3)
                            bandNir = input_raster_ndvi.read(7)
                        
                        np.seterr(divide='ignore', invalid='ignore')

                        ndvi_upper = (bandNir + bandRed)
                        ndvi_lower = (bandNir.astype(float) - bandRed.astype(float))
            
                        base = 0.05
                        ndvi = ndvi_lower / ndvi_upper
                        ndvi = np.round(base*np.around(ndvi/base),2)

                        kwargs = input_raster_ndvi.meta
                        kwargs.update(
                            dtype=rio.float32,
                            count=1,
                            compress='lzw')

                        with rio.open(os.path.join(ndvi_folder,files[:-4]) + "_" + "NDVI" + ".tif", 'w', **kwargs) as dst:
                            dst.write_band(1, ndvi.astype(rio.float32))
            

                for files in os.listdir(ndvi_folder):
                    fig, axes = plt.subplots(nrows=1, ncols=1, sharex=True, sharey=True)
                    file_out = os.path.join(ndvi_folder, files)
                    with rio.open(file_out) as ndvi:
                        p = ndvi.read(1)
                    cmap="RdYlGn"
                    plt.imshow(p, cmap=cmap)
                    
                    plt.clim(-0.1,0.9)
                    plt.colorbar()
                    plt.title(str(files)[:-4])
                #plt.show()

    def savi(self):
        for item in para_name:
            if item == "SAVI":
                savi_folder = os.path.join(output_folder, 'savi')
                os.mkdir(savi_folder)
                for files in os.listdir(tiff_allbands_folder):
                    if files.endswith('.tif'):
                        filepath_out = os.path.join(tiff_allbands_folder, files)
                        with rio.open(filepath_out) as input_raster_savi:
                            bandRed = input_raster_savi.read(3)
                            bandNir = input_raster_savi.read(7)
                        
                        np.seterr(divide='ignore', invalid='ignore')

                        savi_lower = ((bandNir * 0.0001) + (bandRed*0.0001) + 0.5)
                        savi_upper = ((bandNir* 0.0001) - (bandRed* 0.0001))
                        savi_side = (1 + 0.5)
            
                        base = 0.05
                        savi = (savi_upper / savi_lower) * savi_side
                        savi = np.round(base*np.around(savi/base),2)

                        kwargs = input_raster_savi.meta
                        kwargs.update(
                            dtype=rio.float32,
                            count=1,
                            compress='lzw')

                        with rio.open(os.path.join(savi_folder,files[:-4]) + "_" + "SAVI" + ".tif", 'w', **kwargs) as dst:
                            dst.write_band(1, savi.astype(rio.float32))
            

                for files in os.listdir(savi_folder):
                    fig, axes = plt.subplots(nrows=1, ncols=1, sharex=True, sharey=True)
                    file_out = os.path.join(savi_folder, files)
                    with rio.open(file_out) as savi:
                        p = savi.read(1)

                    p = np.ma.masked_where(p < 0.05, p)
                    cmap="RdYlGn"
                    plt.imshow(p, cmap=cmap)
                    plt.clim(0,0.8)
                    plt.colorbar()
                    plt.title(str(files)[:-4])
                #plt.show()
    
    def ndmi(self):
        for item in para_name:
            if item == "NDMI":
                ndmi_folder = os.path.join(output_folder, 'ndmi')
                os.mkdir(ndmi_folder)
                for files in os.listdir(tiff_allbands_folder):
                    if files.endswith('.tif'):
                        filepath_out = os.path.join(tiff_allbands_folder, files)
                        with rio.open(filepath_out) as input_raster_ndmi:
                            bandSwir = input_raster_ndmi.read(9)
                            bandNir = input_raster_ndmi.read(7)
                        
                        np.seterr(divide='ignore', invalid='ignore')

                        ndmi_upper = (bandNir + bandSwir)
                        ndmi_lower = (bandNir.astype(float) - bandSwir.astype(float))
            
                        base = 0.05
                        ndmi = ndmi_lower / ndmi_upper
                        ndmi = np.round(base*np.around(ndmi/base),2)

                        kwargs = input_raster_ndmi.meta
                        kwargs.update(
                            dtype=rio.float32,
                            count=1,
                            compress='lzw')

                        with rio.open(os.path.join(ndmi_folder,files[:-4]) + "_" + "NDMI" + ".tif", 'w', **kwargs) as dst:
                            dst.write_band(1, ndmi.astype(rio.float32))
            

                for files in os.listdir(ndmi_folder):
                    fig, axes = plt.subplots(nrows=1, ncols=1, sharex=True, sharey=True)
                    file_out = os.path.join(ndmi_folder, files)
                    with rio.open(file_out) as ndmi:
                        p = ndmi.read(1)

                    #p = np.ma.masked_where(p < 0.005, p)
                    cmap = plt.cm.RdBu
                    plt.imshow(p, cmap=cmap)
                    
                    plt.clim(-0.3,0.6)
                    plt.colorbar()
                    plt.title(str(files)[:-4])
                #plt.show()
    
    def lai(self):
        for item in para_name:
            if item == "LAI":
                lai_folder = os.path.join(output_folder, 'lai')
                os.mkdir(lai_folder)
                for files in os.listdir(tiff_allbands_folder):
                    if files.endswith('.tif'):
                        filepath_out = os.path.join(tiff_allbands_folder, files)
                        with rio.open(filepath_out) as input_raster_lai:
                            bandNir = input_raster_lai.read(7)
                            bandred = input_raster_lai.read(3)
                            bandblue = input_raster_lai.read(1)
                        
                        np.seterr(divide='ignore', invalid='ignore')
                    
                        lai_upper = 2.5 * ((bandNir * 0.0001) - (bandred * 0.0001))
                        lai_lower = ((bandNir* 0.0001) + 6 *(bandred* 0.0001) - 7.5 * (bandblue*0.0001) + 1)

                        base = 0.05
                        evi = (lai_upper) / (lai_lower)
                        lai = (3.618 * evi - 0.118)
                        lai = np.round(base*np.around(lai/base),2)

                        kwargs = input_raster_lai.meta
                        kwargs.update(
                            dtype=rio.float32,
                            count=1,
                            compress='lzw')

                        with rio.open(os.path.join(lai_folder,files[:-4]) + "_" + "LAI" + ".tif", 'w', **kwargs) as dst:
                            dst.write_band(1, lai.astype(rio.float32))
            

                for files in os.listdir(lai_folder):
                    fig, axes = plt.subplots(nrows=1, ncols=1, sharex=True, sharey=True)
                    file_out = os.path.join(lai_folder, files)
                    with rio.open(file_out) as lai:
                        p = lai.read(1)

                    p = np.ma.masked_where(p < 0.05, p)
                    cmap="RdYlGn"
                    plt.imshow(p, cmap = cmap)
                    plt.clim(0,3.5)
                    plt.colorbar()
                    plt.title(str(files)[:-4])
                #plt.show()

    def evi(self):
        for item in para_name:
            if item == "EVI":
                evi_folder = os.path.join(output_folder, 'evi')
                os.mkdir(evi_folder)
                for files in os.listdir(tiff_allbands_folder):
                    if files.endswith('.tif'):
                        filepath_out = os.path.join(tiff_allbands_folder, files)
                        with rio.open(filepath_out) as input_raster_evi:
                            bandNir = input_raster_evi.read(7)
                            bandred = input_raster_evi.read(3)
                            bandblue = input_raster_evi.read(1)
                        
                        np.seterr(divide='ignore', invalid='ignore')
                    
                        evi_upper = 2.5 * ((bandNir * 0.0001) - (bandred * 0.0001))
                        evi_lower = ((bandNir* 0.0001) + 6 *(bandred* 0.0001) - 7.5 * (bandblue*0.0001) + 1)

                        base = 0.05
                        evi = (evi_upper) / (evi_lower)
                        evi = np.round(base*np.around(evi/base),2)

                        kwargs = input_raster_evi.meta
                        kwargs.update(
                            dtype=rio.float32,
                            count=1,
                            compress='lzw')

                        with rio.open(os.path.join(evi_folder,files[:-4]) + "_" + "EVI" + ".tif", 'w', **kwargs) as dst:
                            dst.write_band(1, evi.astype(rio.float32))


                for files in os.listdir(evi_folder):
                    fig, axes = plt.subplots(nrows=1, ncols=1, sharex=True, sharey=True)
                    file_out = os.path.join(evi_folder, files)
                    with rio.open(file_out) as evi:
                        p = evi.read(1)

                    p = np.ma.masked_where(p < 0.05, p)
                    cmap="RdYlGn"
                    plt.imshow(p, cmap = cmap)
                    plt.clim(0,1)
                    plt.colorbar()
                    plt.title(str(files)[:-4])
                #plt.show()

    def avg_ndvi(self):
        for item in para_name:
            if item == "Avg_NDVI":
                ndvi_avg = []
                fn = []
                for files in os.listdir(tiff_allbands_folder):
                    #fig, axes = plt.subplots(nrows=1, ncols=1, sharex=True, sharey=True)
                    if files.endswith('.tif'):
                        filepath_out = os.path.join(tiff_allbands_folder, files)
                        with rio.open(filepath_out) as input_raster_ndvi:
                            bandRed = input_raster_ndvi.read(3)
                            bandNir = input_raster_ndvi.read(7)
                        
                        np.seterr(divide='ignore', invalid='ignore')

                        ndvi_upper = (bandNir + bandRed)
                        ndvi_lower = (bandNir.astype(float) - bandRed.astype(float))
            
                        base = 0.05
                        ndvi = ndvi_lower / ndvi_upper
                        avg = np.nanmean(ndvi)
                        ndvi_avg.append(avg)
                        fn.append(files[:10])
                        #ndvi = np.round(base*np.around(ndvi/base),2)

                z = list(zip(fn,ndvi_avg))
                z.sort()
                x_val = [x[0] for x in z]
                y_val = [x[1] for x in z]
                plt.plot(x_val,y_val,"-g", Label = "NDVI_Averages")
                plt.plot(x_val,y_val, "or", c = "g" )
                plt.legend(loc="upper left")
                plt.ylim(0,0.9)
                plt.xticks(rotation=45)
                plt.title(str(files)[:-4])
                #plt.xticks(rotation=45)
                #plt.show()   

    def avg_ndmi(self):
        for item in para_name:   
            if item == "Avg_NDMI":
                ndmi_avg = []
                fn1 = []
                for files in os.listdir(tiff_allbands_folder):
                    #fig, axes = plt.subplots(nrows=1, ncols=1, sharex=True, sharey=True)
                    if files.endswith('.tif'):
                        filepath_out = os.path.join(tiff_allbands_folder, files)
                        with rio.open(filepath_out) as input_raster_ndmi:
                            bandSwir = input_raster_ndmi.read(9)
                            bandNir = input_raster_ndmi.read(7)
                        
                        np.seterr(divide='ignore', invalid='ignore')

                        ndmi_upper = (bandNir + bandSwir)
                        ndmi_lower = (bandNir.astype(float) - bandSwir.astype(float))
            
                        base = 0.05
                        ndmi = ndmi_lower / ndmi_upper
                        #ndmi = np.round(base*np.around(ndmi/base),2)
                        avg1 = np.nanmean(ndmi)
                        ndmi_avg.append(avg1)
                        fn1.append(files[:10])
                
                z = list(zip(fn1,ndmi_avg))
                z.sort()
                x_val = [x[0] for x in z]
                y_val = [x[1] for x in z]
                plt.plot(x_val,y_val,"-b", Label = "NDMI_Averages")
                plt.plot(x_val,y_val,"or", c = "b")
                plt.legend(loc="upper left")
                plt.ylim(-0.2,1)
                plt.xticks(rotation=45)
                plt.title(str(files)[:-4])
                #plt.show() 
    
    def elevation(self):
        for item in para_name:
            if item == "Elevation":
                cropfiles = [item for item in shape_name]
                elevation_folder = os.path.join(output_folder, 'elevation')
                os.mkdir(elevation_folder)

                input_raster = gdal.Open(elevation_tiff)
                output_raster = (os.path.join(elev_folder, "farm_slope_proj.tif"))
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

                            with rio.open(os.path.join(elevation_folder,crfiles[:-4]) + "_" + "DEM" + ".tif", "w", **out_meta) as dest:
                                dest.write(out_image)

                for files in os.listdir(elevation_folder):
                    fig, axes = plt.subplots(nrows=1, ncols=1, sharex=True, sharey=True)
                    file_out = os.path.join(elevation_folder, files)
                    with rio.open(file_out) as dem:
                        p = dem.read(1)
                    cmap = plt.cm.OrRd
                    cmap.set_bad(color='white')

                    p = np.ma.masked_where(p < 0.05, p)
                    plt.imshow(p, interpolation='none', cmap=cmap)
                    plt.title(str(files)[:-4])
                    cbar = plt.colorbar()
                    cbar.set_label('metres')
                #plt.show()

    def reflection(self):
        for item in para_name:
            if item == "Reflection":
                for files in os.listdir(tiff_allbands_folder):
                    fig, axes = plt.subplots(nrows=1, ncols=1, sharex=True, sharey=True)   
                    if files.endswith('.tif'):
                        filepath_out = os.path.join(tiff_allbands_folder, files)
                        with rio.open(filepath_out) as input_raster:
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
                    bandnames = ["Blue", "Green", "Red", "Red_Edge_1", "Red_Edge_2", "Red_Edge_3", "NIR", "NIR_2", "SWIR", "SWIR_2"]
                    print(List)
                    
                    z = list(zip(bandnames,List))
                    print(z)
                    x_val = [x[0] for x in z]
                    y_val = [x[1] for x in z]

                    plt.plot(x_val, y_val, "-b", Label = "Reflection")
                    plt.plot(x_val, y_val,'or', c = "b" )
                    plt.legend(loc="upper left")  
                    plt.title(str(files)[:-4])
                    plt.ylim(0,2200)
                    plt.xticks(rotation=45) 
                     
    #Calculates the vaious indices
    def calculate_index(self):
        global para_name
        para_name = par_box.get(0,END)
        self.ndvi()
        self.savi()
        self.ndmi()
        self.lai()
        self.evi()
        self.avg_ndvi()
        self.avg_ndmi()
        self.elevation()
        self.reflection()
        
        plt.show() 

        #shutil.rmtree()
    def delete_dump(self):
        os.rmdir(process_folder)    
    
    def process(self): 
        self.create_subset()
        self.calculate_index()
        self.close()
       # self.delete_dump()
   
           
def main():
    global root
    root = Tk()
    root.geometry("700x700+500+100")
    app = Carpe()
    root.mainloop()


if __name__ == '__main__':
    main()
