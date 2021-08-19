# Importing of required modules
import pandas as pd
import matplotlib.pyplot as pt
import numpy as np

#Class with the junk
class stats:

    # Reading the data from the spreadsheet
    def __init__(self):
        self.countries = pd.read_excel(r"Project_File.xlsx")

    def top3(self):
        # Identify the specified data for computation
        countries = self.countries
        countries = countries.iloc[:,lambda countries:[0, 13, 14, 15, 16, 17, 18, 30, 31, 32, 33, 34]]
        countries = countries.replace("na", 0)
        europe = countries.set_index("Unnamed: 0")
        europe = europe.loc['1998 Jan':'2007 Dec']

        # Print top 3 countries in Europe over the span of 10 years
        sums = europe.sum(axis=0)
        sums = sums.sort_values(ascending=False)
        print()
        print()
        print(sums, "\n")
        top1 = sums.index[0]
        top2 = sums.index[1]
        top3 = sums.index[2]
        print("The top 3 countries with the most visitors in Europe are: ", top1, ",", top2, ",", top3, "\n")

        # Print amount of visitors for the top 3 countries in Europe over the span of 10 years
        amount1 = sums[top1]
        amount2 = sums[top2]
        amount3 = sums[top3]
        print("The amount of visitors from the top 3 countries are", amount1, ",", amount2, ",", amount3,
              "respectively.", "\n")

        # Print the mean amount of visitors for the top 3 countries in Europe over the span of 10 years (Rounded to nearest whole number)
        means = europe.mean(axis=0)
        means = means.sort_values(ascending=False)
        mean1 = round(means[0], 2)
        mean2 = round(means[1], 2)
        mean3 = round(means[2], 2)
        print("The mean amount of visitors from the top 3 countries are", round(mean1), ",", round(mean2), ",",
              round(mean3), "respectively. (Rounded to nearest whole number)", "\n")

        # Print the median amount of visitors for the top 3 countries in Europe over the span of 10 years (Rounded to nearest whole number)
        medians = europe.median(axis=0)
        medians = medians.sort_values(ascending=False)
        median1 = medians[0]
        median2 = medians[1]
        median3 = medians[2]
        print("The median amount of visitors from the top 3 countries are", round(median1), ", ", round(median2), ", ",
              round(median3), "respectively. (Rounded to nearest whole number)")

    def bottom3(self):
        # Identify the specified data for computation
        countries = self.countries
        countries = countries.iloc[:, lambda countries: [0, 13, 14, 15, 16, 17, 18, 30, 31, 32, 33, 34]]
        countries = countries.replace("na", 0)
        europe = countries.set_index("Unnamed: 0")
        europe = europe.loc['1998 Jan':'2007 Dec']

        # Print bottom 3 countries in Europe over the span of 10 years
        sums = europe.sum(axis = 0)
        sums = sums.sort_values(ascending = True)
        print()
        print()
        print()
        print(sums, "\n")
        top1 = sums.index[0]
        top2 = sums.index[1]
        top3 = sums.index[2]
        print("The top 3 countries with the most visitors in Europe are: ", top1, ",", top2, ",", top3, "\n")

        # Print amount of visitors for the bottom 3 countries in Europe over the span of 10 years
        amount1 = sums[top1]
        amount2 = sums[top2]
        amount3 = sums[top3]
        print("The amount of visitors from the bottom 3 countries are", amount1, ",", amount2, ",", amount3,
              "respectively.", "\n")

        # Print the mean amount of visitors for the bottom 3 countries in Europe over the span of 10 years (Rounded to nearest whole number)
        means = europe.mean(axis=0)
        means = means.sort_values(ascending=True)
        mean1 = round(means[0], 2)
        mean2 = round(means[1], 2)
        mean3 = round(means[2], 2)
        print("The mean amount of visitors from the bottom 3 countries are", round(mean1), ",", round(mean2), ",",
              round(mean3), "respectively. (Rounded to nearest whole number)", "\n")

        # Print the median amount of visitors for the bottom 3 countries in Europe over the span of 10 years (Rounded to nearest whole number)
        medians = europe.median(axis=0)
        medians = medians.sort_values(ascending=True)
        median1 = medians[0]
        median2 = medians[1]
        median3 = medians[2]
        print("The median amount of visitors from the bottom 3 countries are", round(median1), ", ", round(median2), ", ", round(median3), "respectively. (Rounded to nearest whole number)", "\n")

    def barGraphs(self):
        # Identify the specified data for computation
        countries = self.countries
        countries = countries.iloc[:, lambda countries: [0, 13, 14, 15, 16, 17, 18, 30, 31, 32, 33, 34]]
        countries = countries.replace("na", 0)
        europe = countries.set_index("Unnamed: 0")
        europe = europe.loc['1998 Jan':'2007 Dec']

        date_sum = europe.sum(axis = 1)
        months = np.zeros((12,), dtype=int).tolist()
        month_names = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
        for j in range(0,12):
            for i in np.arange(j,120,12):
                months[j] += date_sum.iat[i]
        pt.bar(month_names,months, color="lightgreen")
        pt.title("Sum of visitors from all countries each month in each year")
        pt.show()

    def plotGraphs(self):
        # Identify the specified data for computation
        countries = self.countries
        countries = countries.iloc[:, lambda countries: [0, 13, 14, 15, 16, 17, 18, 30, 31, 32, 33, 34]]
        countries = countries.replace("na", 0)
        europe = countries.set_index("Unnamed: 0")
        europe = europe.loc['1998 Jan':'2007 Dec']

        date_sum = europe.mean(axis = 1)
        months = np.zeros((12,), dtype=int).tolist()
        month_names = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
        for j in range(0,12):
            for i in np.arange(j,120,12):
                months[j] += date_sum.iat[i]
        pt.plot(month_names,months, color="lightgreen")
        pt.title("Mean of visitors from all countries each month in each year")
        pt.show()

        date_sum = europe.median(axis=1)
        months = np.zeros((12,), dtype=int).tolist()
        month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        for j in range(0, 12):
            for i in np.arange(j, 120, 12):
                months[j] += date_sum.iat[i]
        pt.plot(month_names, months, color="pink")
        pt.title("Median of visitors from all countries each month in each year")
        pt.show()

Stats = stats()
Stats.top3()
Stats.bottom3()
Stats.barGraphs()
Stats.plotGraphs()
#dgadjahd