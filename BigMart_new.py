# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 20:40:21 2019
@author: Minesh Gandhi
"""
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 00:36:04 2019

@author: Minesh Gandhi
"""

import pandas
import matplotlib.pyplot as plot
from sklearn.metrics.pairwise import pairwise_distances
from scipy import stats

# read data form csv file and print
selectedFiels = ["Item_Identifier","Item_Weight","Item_Visibility","Item_Type","Item_MRP"]
trainData = pandas.read_csv("TestDateset.csv")

"""
print("Infromation for attributed of dataset:")
trainData.info() # gives information about attributes
print('\n')
"""
"""
* Get the mean median Q1(25%) Q3(75%) std AND 5 number summery
"""
print(trainData.iloc[:,:].describe())

a = pandas.DataFrame(trainData.iloc[:,:].describe())
variance = a.iloc[2]*a.iloc[2]
#print(IQR,variance)
print("\nartile range: IQR(Q3-Q1) = \n{}".format(a.iloc[6] - a.iloc[4]))
print(f"\nVariance:-\n{variance}")

"""
*******Plots********
"""
df = pandas.DataFrame(trainData.iloc[:,:],
                  columns=["Item_Weight",'Outlet_Size','Outlet_Identifier',"Item_Visibility","Item_MRP","Item_Type","Outlet_Establishment_Year","Item_Fat_Content","Item_Identifier"])

"""
BOXPLOT
"""

boxplot = df.boxplot(column=["Item_MRP"], by=['Item_Type',"Item_Fat_Content"],layout=(1,1), grid=(True),rot=90,figsize=(15,15),return_type='axes')
fig = plot.savefig(fname='Boxplot_1')

boxplot = df.boxplot(column=["Item_Weight"], by=['Outlet_Establishment_Year','Outlet_Size'],layout=(1,1), grid=(True),rot=90,figsize=(12,12),return_type='axes')
fig = plot.savefig(fname='Boxplot_2')

boxplot = df.boxplot(column=["Item_Weight"], by=['Outlet_Identifier','Outlet_Establishment_Year'],layout=(1,1), grid=(True),rot=90,figsize=(12,12),return_type='axes')
fig = plot.savefig(fname='Boxplot_3')

"""
HISTOGRAM
"""
#x="Item_Type"
histo = df.plot.hist(alpha=0.75,figsize=(12,12),x="Outlet_Establishment_Year",y=["Item_Visibility","Item_MRP"])
plot.title('BigMart Item_MRP vs Item_Type')
plot.xlabel('Outlet_Establishment_Year')
plot.ylabel(["Item_Visibility","Item_MRP"])
fig = plot.savefig(fname="histogram")

"""
QQPLOT
"""
nsample = 100
fig=plot.figure()
ax=fig.add_subplot(111)

qqploy=stats.probplot(x= df["Item_MRP"],plot=ax)
ax.get_lines()[0].set_marker('.')
ax.get_lines()[0].set_markerfacecolor('r')
ax.get_lines()[0].set_markersize(5.0)
ax.get_lines()[1].set_linewidth(2.0)
ax.set_title("Q-Q plot")
fig = plot.savefig(fname="QQplot",figsize=(12,12))

"""
SCATTER plot
""" 
scatter = df.plot.scatter(x='Item_MRP',y="Item_Weight",c='Outlet_Establishment_Year',colormap='viridis',figsize=(12,12))
plot.xlabel('Item_MRP')
plot.ylabel('Item_Weight')
plot.title('SCATTER PLOT')
fig=plot.savefig(fname='scatter_plot')

"""
Proximity Measure for Niminal attribute
"""
# Construct dissimilarity matrix for nominal attributes of first 'n' records

records = int(input("Required Record:" ))
display = df['Item_Weight'].head(records)
dissimalarity_matrix = [[int(display[i] != display[j]) if j < i else 0 for j in range(i+1)] for i in range(records)]
print(dissimalarity_matrix)

"""
Minkowski Distance
"""

"""
Implement data smoothing 
"""

