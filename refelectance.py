import sys
import os
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import pandas as pd 
import numpy as np
from pandas import read_csv
from matplotlib import pyplot
import scipy
from scipy.interpolate import make_interp_spline, BSpline
from scipy.ndimage.filters import gaussian_filter1d

#Read csv files as variables
BM_all = pd.read_csv("D:\\BM2l\\processed\\CSV_Combined.csv",engine = 'python', sep = ";")
print(BM_all)


kaempe = (list(zip(BM_all.Wavelength, BM_all.BM_001, BM_all.BM_002, BM_all.BM_003, BM_all.BM_004, BM_all.BM_005, BM_all.BM_006)))
print(kaempe)
x, y1,y2,y3,y4,y5,y6 = zip(*kaempe)

plt.plot(x,y1, "-b", Label = "BM_001")
plt.plot(x,y2, "-r", Label = "BM_002")
plt.plot(x,y3, "-g", Label = "BM_003")
plt.plot(x,y4, "-y", Label = "BM_004")
plt.plot(x,y5, "-m", Label = "BM_005")
plt.plot(x,y6, "-c", Label = "BM_006")
plt.legend(loc="upper left")
plt.xticks(rotation=45)
plt.title("Kaempe II Soil Reflectance")
plt.xticks(rotation=45)
plt.show() 


Pingengloken = (list(zip(BM_all.Wavelength, BM_all.BM_007, BM_all.BM_008)))
print(Pingengloken)
x,y7,y8 = zip(*Pingengloken)

plt.plot(x,y7, "-b", Label = "BM_007")
plt.plot(x,y8, "-r", Label = "BM_008")
plt.legend(loc="upper left")
plt.xticks(rotation=45)
plt.title("Pingengloken Soil Reflectance")
plt.xticks(rotation=45)
plt.show()


Binnenkemp_II = (list(zip(BM_all.Wavelength, BM_all.BM_009, BM_all.BM_010, BM_all.BM_011, BM_all.BM_012)))
print(Binnenkemp_II)
x, y9,y10,y11,y12 = zip(*Binnenkemp_II)

plt.plot(x,y9, "-b", Label = "BM_009")
plt.plot(x,y10, "-r", Label = "BM_010")
plt.plot(x,y11, "-g", Label = "BM_011")
plt.plot(x,y12, "-y", Label = "BM_012")
plt.legend(loc="upper left")
plt.xticks(rotation=45)
plt.title("Binnenkemp_II Soil Reflectance")
plt.show()


Binnenkemp_I = (list(zip(BM_all.Wavelength, BM_all.BM_013, BM_all.BM_014, BM_all.BM_015, BM_all.BM_016, BM_all.BM_017)))
print(Binnenkemp_I)
x, y13,y14,y15,y16,y17 = zip(*Binnenkemp_I)

plt.plot(x,y13, "-b", Label = "BM_013")
plt.plot(x,y14, "-r", Label = "BM_014")
plt.plot(x,y15, "-g", Label = "BM_015")
plt.plot(x,y16, "-y", Label = "BM_016")
plt.plot(x,y17, "-m", Label = "BM_017")

plt.legend(loc="upper left")
plt.xticks(rotation=45)
plt.title("Binnenkemp_I Soil Reflectance")
plt.show() 

all = (list(zip(BM_all.Wavelength,BM_all.BM_001, BM_all.BM_002, BM_all.BM_003, BM_all.BM_004, BM_all.BM_005, BM_all.BM_006, BM_all.BM_007, BM_all.BM_008, BM_all.BM_009, BM_all.BM_010, BM_all.BM_011, BM_all.BM_012, BM_all.BM_013, BM_all.BM_014, BM_all.BM_015, BM_all.BM_016, BM_all.BM_017)))
x,y1,y2,y3,y4,y5,y6, y7,y8, y9,y10,y11,y12, y13,y14,y15,y16,y17 = zip(*all)


plt.plot(x,y1, "-b", Label = "BM_001")
plt.plot(x,y2, "-r", Label = "BM_002")
plt.plot(x,y3, "-g", Label = "BM_003")
plt.plot(x,y4, "-y", Label = "BM_004")
plt.plot(x,y5, "-m", Label = "BM_005")
plt.plot(x,y6, "-c", Label = "BM_006")
plt.plot(x,y7, "-c", Label = "BM_007")
plt.plot(x,y8, "-r", Label = "BM_008")
plt.plot(x,y9, "-b", Label = "BM_009")
plt.plot(x,y10, "-r", Label = "BM_010")
plt.plot(x,y11, "-g", Label = "BM_011")
plt.plot(x,y12, "-y", Label = "BM_012")
plt.plot(x,y13, "-b", Label = "BM_013")
plt.plot(x,y14, "-r", Label = "BM_014")
plt.plot(x,y15, "-g", Label = "BM_015")
plt.plot(x,y16, "-y", Label = "BM_016")
plt.plot(x,y17, "-m", Label = "BM_017")
plt.legend(loc="upper left")
plt.xticks(rotation=45)
plt.title("Soil Reflectance")
plt.show() 







##series = BM_001.value
#s = int(series)
#print(s)
#series.plot()
#yplot.show()