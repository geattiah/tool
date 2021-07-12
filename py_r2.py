import sys
import os
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import pandas as pd 
import numpy as np



#Read csv files as variables
commonsRNAs = pd.read_csv("/home/gift/Downloads/gfity/commonsRNAs.csv",sep = None, header = 1)
O104_04sRNAs = pd.read_csv("/home/gift/Downloads/gfity/O104-04sRNAs.csv", sep = None)
O104_12sRNAs = pd.read_csv("/home/gift/Downloads/gfity/O104-12sRNAs.csv", sep = None)
summary = pd.read_csv("/home/gift/Downloads/gfity/summarytable.csv", sep = None)

#Print file to dtermine if loaded correctly
print(commonsRNAs)
print(O104_04sRNAs)
print(O104_12sRNAs)
print(summary)

plot_O4_04 = sorted(list(zip(commonsRNAs.Name, commonsRNAs.iloc[:,9], commonsRNAs.TSS)))
x_val, x_val1, y_val = zip(*plot_O4_04)


fig = plt.figure() 
ax1 = fig.add_subplot(111, label = "1")
ax2 = fig.add_subplot(111, label="2", frame_on=False)

color = 'tab:blue'
ax1.set_xlabel('LBO14_04', color= color, fontsize = 14)
ax1.plot(x_val,y_val,"w")
ax1.ticklabel_format(useOffset=False, style='plain', axis = 'y')
ax1.legend(loc="upper left")
ax1.xaxis.tick_bottom()
ax1.tick_params(labeltop=False)
fig.autofmt_xdate(rotation=90)


color = 'tab:blue'
ax2.set_xlabel('LBO14_12', color=color, fontsize = 14)
ax2.set_ylabel('TSS-Values', color= color, fontsize = 14)
ax2.plot(x_val1,y_val,"-r", Label = "TSS")
ax2.ticklabel_format(useOffset=False, style='plain', axis = 'y')
ax2.legend(loc="upper left")
ax2.xaxis.tick_top()
ax2.xaxis.set_label_position('top')


plt.xticks(rotation=90)
#plt.title("TSS / Step Height", fontsize = 20)
#plt.xticks(rotation=45)
plt.show() 