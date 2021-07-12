#some of them you need to install...just use sudo/make to do that
import sys
import os
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np

#Read csv files as variables
commonsRNAs = pd.read_csv("C:\\Users\\attiah\\Downloads\\gfity\\commonsRNAs.csv",sep = None,engine = 'python', header = 1)
O104_04sRNAs = pd.read_csv("C:\\Users\\attiah\\Downloads\\gfity\\O104-04sRNAs.csv", engine = 'python',sep = None)
O104_12sRNAs = pd.read_csv("C:\\Users\\attiah\\Downloads\\gfity\\O104-12sRNAs.csv",engine = 'python', sep = None)
summary = pd.read_csv("C:\\Users\\attiah\\Downloads\\gfity\\summarytable.csv",engine = 'python', sep = None)

#Print file to dtermine if loaded correctly
print(commonsRNAs)
print(O104_04sRNAs)
print(O104_12sRNAs)
print(summary)

#Variable to plot the TSS by calling the TSS and name column 
#It is safer to sort them to prevent chaos for repeated values 
plot_TSS = sorted(list(zip(O104_04sRNAs.Name, O104_04sRNAs.TSS)))

#Assign the x and y values
#The * means plot all. You can specify what to select
x_val, y_val = zip(*plot_TSS)

#Variable to Plot stepHeight
plot_stepHeight = sorted(list(zip(O104_04sRNAs.Name, O104_04sRNAs.stepHeight)))
x_val1, y_val1 = zip(*plot_stepHeight)

#Assign figure in whihc plotting would be done
fig = plt.figure() 
#set both axes since we are plotting two graphs on one
ax1 = fig.add_subplot(111, label = "1")
ax2 =fig.add_subplot(111, label="2", frame_on=False)

#Properties for the first plot
#set colour 
color = 'tab:blue'
#set label and fontsize
ax1.set_ylabel('TSS', color= color, fontsize = 16)
#plot TSS
ax1.plot(x_val,y_val,"-b", Label = "TSS")
#Location legend
ax1.legend(loc="upper left")
#location of ticks in x axis
ax1.xaxis.tick_top()
#position of ticks..can be sppecified in this case not
ax1.xaxis.set_ticks_position('none') 
ax1.tick_params(labeltop=False)

#Properties for the second plot
color = 'tab:red'
ax2.set_ylabel('Step Height', color=color, fontsize = 16)
ax2.plot(x_val1,y_val1,"-r", Label = "Step height")
ax2.legend(loc="best")
ax2.xaxis.tick_bottom()
ax2.yaxis.tick_right()
#ax2.xaxis.set_label_position('top') 
ax2.yaxis.set_label_position('right') 


plt.xticks(rotation=90)
plt.title("TSS / Step Height", fontsize = 20)
plt.show() 