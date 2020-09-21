import csv
import pandas as pd
import matplotlib.pyplot as plt

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

#["date"] = (df.Zeitstempel[:4])
data = list(zip(df.Zeitstempel, df.Wert))
prec = list(zip(daf.Zeitstempel, daf.Wert))
#data = list(df.Zeitstempel)
#data = str(data[0:])
#das = data[:4]
#print(data)
# 
# d_2017 = data[121:274]
d_2018 = data[488:641]
# d_2019 = data[853:1006]

da_2017 = prec[121:274]
da_2018 = prec[488:641]
da_2019 = prec[853:1006]

#d_2020 = data[1096:]

#x_val = [x[0] for x in d_2017]
#y_val = [x[1] for x in d_2017]
y_val1 = [x[1] for x in d_2018]
# y_val2 = [x[1] for x in d_2019]

x_val2 = [x[0] for x in da_2018]
y_val3 = [x[1] for x in da_2017]
y_val4 = [x[1] for x in da_2018]
y_val5 = [x[1] for x in da_2019]

#plt.plot(x_val,y_val,"-b", Label = "2017")
plt.plot(x_val2,y_val1,"-r", Label = "°C - Temperature")
#plt.plot(x_val,y_val2,"-r", Label = "2019")
# plt.plot(x_val2,y_val3,"-b", Label = "2017")
plt.plot(x_val2,y_val4,"-b", Label = "mm - Rainfall")
# plt.plot(x_val2,y_val5,"-r", Label = "2019")
plt.legend(loc="upper left")
plt.ylim(0,35)
#plt.plot(x_val,y_val3,"-y")
plt.xticks(rotation=45)
plt.title("Climate - 2018")
plt.show()
