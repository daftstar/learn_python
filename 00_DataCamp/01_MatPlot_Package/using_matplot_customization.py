import matplotlib.pyplot as plt

# Populate test data (data list append)
# year = []
# for i in range(1950, 2101):
#     year.append(i)
# print (year)

# OR List Comprehension (data list append)
# http://www.secnetix.de/olli/Python/list_comprehensions.hawk

year = [x + 1 for x in range(1949, 2100)]
pop =  [x * 1.13 for x in range(1, 152)]

# set graph titles and axis titles
plt.plot(year, pop)
plt.xlabel("Year")
plt.ylabel("Population")
plt.title("World Population Projections")

# automate y_axis ticks
# y_axis_ticks = [x * 20 for x in range(1, 10)]


# set the tick increments & label each tick with custom names
plt.yticks([20, 40, 60, 80, 100, 120, 140, 160, 180],
           ['0 Billion', '2B', '4B', '6B', '8B', "10B", "12B", "14B", "16B"])
plt.show()