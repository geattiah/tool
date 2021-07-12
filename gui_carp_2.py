#Package neede to be installed
# pip install Pillow
# pip install 

#ipi install from osgeo import gdal
import sys
import os
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from shapely.geometry import mapping
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


#Define folder locations
tiff_folder = "/home/gift/Dropbox/carpe_data/tiffs"
shapefile_folder = "/home/gift/Dropbox/carpe_data/shapes"
#processing_folder = "/home/gift/Dropbox/carpe_data/georef_tiffs"

class Carpe(Frame):
    def __init__(self):
        super().__init__()

        self.GUI()
        self.heading_view()
        self.location_view()
        self.farm_selection_view()
        self.date_heading_view()
        self.date_view()
        self.parameter_view()
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
        
    
    def browse_button(self):
        filename = filedialog.askdirectory()
        folder_path.set(filename)
              
    # list that apperas in farm selection view    
    def farm_selection_view(self):
        farm_frame = Frame(self)
        farm_frame.pack(fill=X)

        farm_label = Label(farm_frame, text="Select farm:", width=17, font = (None, 12))
        farm_label.pack(side=LEFT, padx=20, pady=10)
        farm_folder = shapefile_folder
        global file_list
        file_list = [files for files in os.listdir(farm_folder) if files.endswith('.shp')]
        file_name = [os.path.splitext(files)[0] for files in file_list]
        file_name.sort()

        global farm_dropdown
        farm_dropdown = Combobox(farm_frame, values = file_name, width = 54)
        #farm_dropdown.set(file_name[0])
        farm_dropdown.pack (side = LEFT, padx=5, pady=10)
        farm_dropdown.bind("<<ComboboxSelected>>")

    def selected_farm(self,event):
        print(event.widget.get())   

    # Heading for date entries
    def date_heading_view(self):
        date_frame = Frame(self)
        date_frame.pack(fill=X)

        date_label = Label(date_frame, text="Enter Range of Dates", width=17, font = (None, 12))
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


        add_button = Button(date_frame, text = "Add", command = self.add_item,width =5)
        add_button.pack(side = LEFT,padx= 5)
        
        global sel_box
        sel_box = Listbox(date_frame, width = 15, height = 10)
        sel_box.pack(side = LEFT, padx= 5, pady=10)
       # sel_box.bind("<<ListboxSelected>>")

        scrollbar = Scrollbar(date_frame, orient="vertical",command=sel_box.yview)
        scrollbar.pack(side="left", fill="y")

        sel_box.config(yscrollcommand=scrollbar.set)

        remove_button= Button(date_frame, text = "Delete", command = self.delete_item,width =7)
        remove_button.pack(side = LEFT,padx= 5)
    
    def add_item(self):
        global sel_date
        sel_date = date_box.curselection()
        for item in sel_date:
            date_files = date_box.get(item)
            sel_files = sel_box.get(0, END)
            if date_files not in sel_files:
                sel_box.insert(END, date_box.get(item))

    def delete_item(self):
        global rem_date
        rem_date = sel_box.curselection()
        for item in rem_date:
            sel_box.insert(END, sel_box.delete(item))

    def parameter_view(self):
        parameter_frame = Frame(self)
        parameter_frame.pack(fill=X)

        parameter_label = Label(parameter_frame, text="Parameter:", width=17, font = (None, 12))
        parameter_label.pack(side=LEFT, padx=20, pady=10)

        parameters = ["NDVI", "NDWI"]
        parameters.sort()

        global parameter_dropdown
        parameter_dropdown = Combobox(parameter_frame, values = parameters, width = 54)
        parameter_dropdown.set(parameters[0])
        parameter_dropdown.pack(side = LEFT, padx=5, pady=10)
        parameter_dropdown.bind("<<ComboboxSelected>>")
    
    def proxit_view(self):
        proxit_frame = Frame(self)
        proxit_frame.pack(fill=X)

        process_button = Button(proxit_frame, text = "PROCESS", command = self.process )
        process_button.pack(padx = (150), pady = 10, side = LEFT)

        exit_button = Button(proxit_frame, text = "EXIT", command = self.close )
        exit_button.pack(padx = 120, pady = 10, side = LEFT)
    
    def close(self):
        root.quit()
 
    def create_subset(self):
        root.iconify() 
        global output_folder 
        output_folder = folder_path.get()
        global process_folder
        process_folder = os.path.join(output_folder, 'dump')
        os.mkdir(process_folder)

        shape_name = farm_dropdown.get()
        crop_shape = os.path.join(shapefile_folder, shape_name + '.shp')
        
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
        
        with fiona.open(crop_shape, "r") as shapefile:
            shapes = [feature["geometry"] for feature in shapefile]
        
        global tiff_allbands_folder
        tiff_allbands_folder = os.path.join(output_folder, 'tiff_all_bands')
        os.mkdir(tiff_allbands_folder)

        for files in os.listdir(process_folder):
            if files.endswith('.tif'):
                filepath = os.path.join(process_folder, files)
                with rio.open(filepath) as src:
                    out_image, out_transform = rio.mask.mask(src, shapes, crop=True)
                    out_meta = src.meta

                out_meta.update({"driver": "GTiff",
                                "height": out_image.shape[1],
                                "width": out_image.shape[2],
                                "transform": out_transform})

                with rio.open(os.path.join(tiff_allbands_folder,files[:-4]) + "_" + shape_name + ".tif", "w", **out_meta) as dest:
                    dest.write(out_image)

    def calculate_index(self):
        index = parameter_dropdown.get()
        if index == "NDVI":
            ndvi_folder = os.path.join(output_folder, 'ndvi')
            os.mkdir(ndvi_folder)
            for files in os.listdir(tiff_allbands_folder):
                if files.endswith('.tif'):
                    filepath_out = os.path.join(tiff_allbands_folder, files)
                    with rio.open(filepath_out) as input_raster_ndvi:
                        bandRed = input_raster_ndvi.read(4)
                        bandNir = input_raster_ndvi.read(6)
                    
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

                    with rio.open(os.path.join(ndvi_folder,files[:-4]) + "_" + "ndvi" + ".tif", 'w', **kwargs) as dst:
                        dst.write_band(1, ndvi.astype(rio.float32))
        

            for files in os.listdir(ndvi_folder):
                fig, axes = plt.subplots(nrows=1, ncols=1, sharex=True, sharey=True)
                file_out = os.path.join(ndvi_folder, files)
                with rio.open(file_out) as ndvi:
                    p = ndvi.read(1)
                plt.imshow(p)
                plt.clim(0,0.8)
                plt.colorbar()
                plt.title(str(files)[:-4])
            plt.show()

        elif index == "NDWI":
            ndwi_folder = os.path.join(output_folder, 'ndwi')
            os.mkdir(ndwi_folder)
            for files in os.listdir(tiff_allbands_folder):
                if files.endswith('.tif'):
                    filepath_out = os.path.join(tiff_allbands_folder, files)
                    with rio.open(filepath_out) as input_raster_ndwi:
                        bandNir = input_raster_ndwi.read(7)
                        bandSwir = input_raster_ndwi.read(9)
                    
                    np.seterr(divide='ignore', invalid='ignore')

                    ndwi_upper = (bandNir + bandSwir)
                    ndwi_lower = (bandNir.astype(float) - bandSwir.astype(float))
        
                    base = 0.05
                    ndwi = ndwi_lower / ndwi_upper
                    ndwi = np.round(base*np.around(ndwi/base),2)

                    kwargs = input_raster_ndwi.meta
                    kwargs.update(
                        dtype=rio.float32,
                        count=1,
                        compress='lzw')

                    with rio.open(os.path.join(ndwi_folder,files[:-4]) + "_" + "ndwi" + ".tif", 'w', **kwargs) as dst:
                        dst.write_band(1, ndwi.astype(rio.float32))
        

            for files in os.listdir(ndwi_folder):
                fig, axes = plt.subplots(nrows=1, ncols=1, sharex=True, sharey=True)
                file_out = os.path.join(ndwi_folder, files)
                with rio.open(file_out) as ndwi:
                    p = ndwi.read(1)
                plt.imshow(p)
                plt.clim(0,0.8)
                plt.colorbar()
                plt.title(str(files)[:-4])
            plt.show()
        


    def process(self): 
        self.create_subset()
        self.calculate_index()
        self.close()

        


    #os.rmdir(process_folder)    
            
def main():
    global root
    root = Tk()
    root.geometry("700x500+700+500")
    app = Carpe()
    root.mainloop()
   

if __name__ == '__main__':
    main()
