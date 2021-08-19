import pandas as pd
from matplotlib import pyplot as plt
import numpy as np


class Stats:
    countries: object = pd.read_excel(r"C:\Users\USER\PycharmProjects\pythonProject3\Project_File.xlsx")
#122-241
Stats()
Cunt_List=[13, 14, 15, 16, 17, 18, 30, 31, 32, 33, 34]
print(Stats.countries)

df = Stats.countries
df = df.iloc[:,lambda df:[0,13, 14, 15, 16, 17, 18, 30, 31, 32, 33, 34]]
df2 = df.set_index('Unnamed: 0')
df2 = df2.loc['1998 Jan':'2007 Dec']
print (df2)

Sums = df2.sum(axis=0)
Sums = Sums.sort_values(ascending=False)
print (Sums)

mos1 = Sums.index[0]
mos2 = Sums.index[1]
mos3 = Sums.index[2]


print("")

vis1 = Sums[mos1]
vis2 = Sums[mos2]
vis3 = Sums[mos3]


print("")

means = df2.mean(axis=0)
means = means.sort_values(ascending=False)
print (means)
mean1 = round(means[0],2)
mean2 = round(means[1],2)
mean3 = round(means[2],2)


print("")

medians = df2.median(axis=0)
medians = medians.sort_values(ascending=False)
print (medians)
med1 = medians[0]
med2 = medians[1]
med3 = medians[2]
print("The Median visitors from the top 3 countries are", med1 , med2 , med3, "respectively")
print("The top 3 countries with the most visitors are", mos1 , mos2 , mos3)
print("The Amount of visitors from the top 3 countries are", vis1 , vis2 , vis3, "respectively")
print("The Average visitors from the top 3 countries are", mean1 , mean2 , mean3, "respectively")
print("")


date_sum = df2.mean(axis=1)
months = np.zeros((12,), dtype=int).tolist()
month_names = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
for j in range(0,12):
    for i in np.arange(j,120,12):
        months[j] += date_sum.iat[i]
print (months)
plt.plot(month_names,months)

plt.show()