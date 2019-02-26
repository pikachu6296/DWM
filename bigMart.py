# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 00:36:04 2019

@author: Minesh Gandhi
"""

import pandas
import matplotlib.pyplot as plt
import matplotlib
import csv
import scipy
import pylab
import numpy


# read data form csv file and print
selectedFiels = ["Item_Identifier","Item_Weight","Item_Visibility","Item_Type","Item_MRP"]
trainData = pandas.read_csv("TestDateset.csv")

#print(trainData[selectedFiels].describe())
#trainData.info() # givs 
#print('\n')
#outputFile = open("BigMart.docx",'r')
#store = outputFile.write(trainData.iloc[:,:].describe())
#outputFile.writelines(store)
#outputFile.close()
#print(trainData.iloc[:,:].describe())
#print('\n')

a = pandas.DataFrame(trainData.iloc[:,:].describe())
print("a:",a,"\n")
#print("Q1 for all attributes: \n", a.iloc[4]) # print Q1
#print("Q3 for all attributes: \n", a.iloc[6]) #print Q3
#print("IQR for all attributes: \n", (a.iloc[6] - a.iloc[4])) #print IQR
Q1 = a.iloc[4]
Q3 = a.iloc[6]
IQR = (Q3 - Q1)
print(IQR,Q1,Q3)

q25, q75 = numpy.percentile(trainData.Item_Weight.dropna(),[25,75])
iqr = q75 - q25

min = q25 - (iqr*1.5)
max = q75 + (iqr*1.5)

i = 'Item_Weight'
 
plt.figure(figsize=(10,8))
plt.subplot(211)
plt.xlim(trainData[i].min(), trainData[i].max()*1.1)
plt.axvline(x=min)
plt.axvline(x=max)
 
ax = trainData[i].plot(kind='kde')
 
plt.subplot(212)
plt.xlim(trainData[i].min(), trainData[i].max()*1.1)
sns.boxplot(x=trainData[i])
plt.axvline(x=min)
plt.axvline(x=max)


#fig, ax = plot.subplot(x="diagnosis", y="area_mean", d trainData,)

#print(trainData)
#
#Dataarr = []
#for DataFile in trainData:
#fetchFields = trainData.columns 
#print(fetchFields)

# Find meadin 
#medianOfItem_Weight = statistics.median(pandas.read_csv("TestDateset.csv",usecols="Item_Weight"))
#print(medianOfItem_Weight)

## agg backend is used to create plot as a .png file

matplotlib.use('agg')
with open("TestDateset.csv", 'r') as f:
    d_reader = csv.DictReader(f)

    #get fieldnames from DictReader object and store in list
    headers = d_reader.fieldnames
print(headers)
fig = plt.figure(1,figsize=(10,8))

ax = fig.add_subplot(111)

#boxplot = ax.boxplot(trainData.dtypes(include=['float64','int64']).apply())
fig.savefig('fig.png', bbox_inches='tight')

scipy.stats.probplot(trainData,dist="norm",plot=pylab)
pylab.show()