import sys
import os
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np
import scipy
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score, recall_score


pred = pd.read_csv("D:\\predict.csv",sep = ";", engine = 'python', header = 0)

prediction = list(pred.prediction)

crop = list(pred.Crop)

labels = ['Grassland', 'Maize', 'Potato',"Wheat and barley"]
cm = confusion_matrix(crop, prediction, labels)
print(cm)
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(cm )
plt.title('Confusion matrix of Classification')
fig.colorbar(cax)
for (i, j), z in np.ndenumerate(cm):
    ax.text(j, i, '{:0.1f}'.format(z), ha='center', va='center')

#ax.matshow(cm, cmap='seismic')
ax.set_xticklabels([''] + labels)
ax.xaxis.tick_bottom()
ax.set_yticklabels([''] + labels)
plt.xlabel('Predicted')
plt.ylabel('True')
#plt.show()


def precision(label, confusion_matrix):
    col = confusion_matrix[:, label]
    return confusion_matrix[label, label] / col.sum()
    
def recall(label, confusion_matrix):
    row = confusion_matrix[label, :]
    return confusion_matrix[label, label] / row.sum()

def precision_macro_average(confusion_matrix):
    rows, columns = confusion_matrix.shape
    sum_of_precisions = 0
    for label in range(rows):
        sum_of_precisions += precision(label, confusion_matrix)
    return sum_of_precisions / rows

def recall_macro_average(confusion_matrix):
    rows, columns = confusion_matrix.shape
    sum_of_recalls = 0
    for label in range(columns):
        sum_of_recalls += recall(label, confusion_matrix)
    return sum_of_recalls / columns

print(precision_macro_average(cm))
#print(recall_macro_average(cm))

com = np.array(cm)
print(com)

for label in range(4):
    print(f"{label:5d} {precision(label, com):9.3f} {recall(label, com):6.3f}")


def accuracy(confusion_matrix):
    diagonal_sum = confusion_matrix.trace()
    sum_of_all_elements = confusion_matrix.sum()
    return diagonal_sum / sum_of_all_elements 


print(accuracy(cm))
