import csv
import pandas as pd
import matplotlib.pyplot as plt
import os
import rasterio as rio
import matplotlib.pyplot as plt
import numpy as np

dates = []
temperature = []

temp = 'C:\\Users\\attiah\\Downloads\\temp\\data\data_TMK_MN004.csv.'
precip = 'C:\\Users\\attiah\\Downloads\\precip_mm\\data\\data_RS_MN006.csv'


df = pd.read_csv(temp)
df.Zeitstempel = df.Zeitstempel.astype(str)
df.Zeitstempel = pd.to_datetime((df.Zeitstempel),format='%Y%m%d')

daf = pd.read_csv(precip)
daf.Zeitstempel = daf.Zeitstempel.astype(str)
daf.Zeitstempel = pd.to_datetime((daf.Zeitstempel),format='%Y%m%d')

lists = []
lists2 = []
lists3 = []
file_name = []
months = [ "April","May", "Jun", "Jul", "Aug", "Sep", "Oct"]


folder = "D:\\data\\J\\dump\\dump\\ndmi"

for files in os.listdir(folder):
    if files.endswith('.tif'):
        filepath_out = os.path.join(folder, files)
        with rio.open(filepath_out) as input_raster_ndvi:
            ndvi = input_raster_ndvi.read(1)
            #print (ndvi)
        
        #fn = files[6]
        a1 = np.nanmean(ndvi)

        lists.append(a1)
        #file_name.append(fn)

folder_2 = "D:\\data\\bund\\2018\\ndvi"

for files in os.listdir(folder_2):
    if files.endswith('.tif'):
        filepath_out = os.path.join(folder_2, files)
        with rio.open(filepath_out) as input_raster_ndvi:
            ndvi = input_raster_ndvi.read(1)
            #print (ndvi)
        
        fn = files[5:7]
        a2 = np.nanmean(ndvi)
        lists2.append(a2)
        file_name.append(fn)

folder_2 = "D:\\data\\bund\\2019\\ndvi"

for files in os.listdir(folder_2):
    if files.endswith('.tif'):
        filepath_out = os.path.join(folder_2, files)
        with rio.open(filepath_out) as input_raster_ndvi:
            ndvi = input_raster_ndvi.read(1)
            #print (ndvi)
        
        #fn = files[:10]
        a3 = np.nanmean(ndvi)
        lists3.append(a3)

z = list(zip(months,lists,lists2,lists3))
#z = z[4:10]

#["date"] = (df.Zeitstempel[:4])
data = list(zip(df.Zeitstempel, df.Wert))
prec = list(zip(daf.Zeitstempel, daf.Wert))
#data = list(df.Zeitstempel)
#data = str(data[0:])
#das = data[:4]
#print(data)
# 
# d_2017 = data[121:274]
#d_2018 = data[488:641]
# d_2019 = data[853:1006]

da_2017 = prec[90:274]
da_2018 = prec[457:641]
da_2019 = prec[822:1006]

#d_2020 = data[1096:]

#x_val = [x[0] for x in d_2017]
#y_val = [x[1] for x in d_2017]
#y_val1 = [x[1] for x in d_2018]
# y_val2 = [x[1] for x in d_2019]

x_val2 = [x[0] for x in da_2018]
y_val3 = [x[1] for x in da_2017]
y_val4 = [x[1] for x in da_2018]
y_val5 = [x[1] for x in da_2019]

fig = plt.figure() 
ax1 = fig.add_subplot(111, label = "1")
ax2 =fig.add_subplot(111, label="2", frame_on=False)



color = 'tab:blue'
ax1.set_ylabel('rainfall (mm)', color= color)


#plt.plot(x_val,y_val,"-b", Label = "2017")
#plt.plot(x_val2,y_val1,"-r", Label = "°C - Temperature")
#plt.plot(x_val,y_val2,"-r", Label = "2019")
ax1.plot(x_val2,y_val3,"-b", Label = "2017")
#ax1.plot(x_val2,y_val4,"-g", Label = "2018")
ax1.plot(x_val2,y_val5,"-r", Label = "2019")
ax1.legend(loc="upper left")
ax1.xaxis.tick_top()
ax1.xaxis.set_ticks_position('none') 
ax1.tick_params(labeltop=False)


x_val = [x[0] for x in z]
y_val = [x[1] for x in z]
y_val2 = [x[2] for x in z]
y_val3 = [x[3] for x in z]

#ax2 = ax1.twinx()
color = 'tab:green'
ax2.set_ylabel('NDVI', color=color)
ax2.plot(x_val,y_val,"-b", Label = "2017")
#ax2.plot(x_val,y_val2,"-g", Label = "2018")
ax2.plot(x_val,y_val3,"-r", Label = "2019")
ax2.xaxis.tick_bottom()
ax2.yaxis.tick_right()
#ax2.xaxis.set_label_position('top') 
ax2.yaxis.set_label_position('right') 
#ax1.set_xlabel('Dates')



ax2.plot(x_val,y_val,'or', c = "b")
ax2.plot(x_val,y_val2, 'or', c = "g")
ax2.plot(x_val,y_val3,'or', c = "r")



#ax1.ylim(0,35)
#plt.plot(x_val,y_val3,"-y")
plt.xticks(rotation=45)
plt.title("NDVI / Rainfall")
plt.show()
