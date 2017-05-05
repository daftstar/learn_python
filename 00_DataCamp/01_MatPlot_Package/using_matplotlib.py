import matplotlib.pyplot as plt

year = [1950, 1970, 1990, 2010]
population = [2.519, 3.692, 5.263, 6.972]

# this builds the plot as a standard line graph
# plt.plot(year, population)

# this builds as a scatter plot
# plt.scatter(year, population)

# these two lines build the plot as a line graph WITH plots
plt.plot(year, population)
plt.scatter(year, population)



# this visualizes the plot.
# you have to explicitly execute this, in case you want to add anything
# prior to building the chart.
plt.show()
