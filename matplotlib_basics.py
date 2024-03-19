# Matplotlib is a plotting library used for visualization of data
import matplotlib.pyplot as plt

year = [1950, 1970, 1990, 2010]
population = [2.519, 3.692, 5.263, 6.972]
plt.plot(year, population) # (horizontal axis, vertical axis)
plt.show() # line plot
plt.scatter(year, population) # this plot only shows data points and not connecting line
plt.show()

# if our data is very much large for a linear scale, we can change scale to log using:
# plt.xscale('log')
# or
# plt.yscale('log')
# when we use a logarithmic scale, distance is multiplied and divided
# on the other hand, using a linear scale would add or subtract the distance
# for ex if we move distance 10 on linear scale it would be: 0 10 20 30
# whereas on a log scale it would be : 1 10 100 1000

# histogram : very useful to get idea of distribution
values = [0, 0.6, 1.4, 1.6, 2.2, 2.5, 2.6, 3.2, 3.5, 3.9, 4.2, 6]
plt.hist(values, bins = 3) # bins are argument decides into how many bins data should be divided, by default it is 10
plt.show()
plt.clf() # clears the current figure

# adding more data
year = [1800, 1900] + year
population = [1.0, 1.650] + population

plt.plot(year, population)

# data customization
plt.xlabel("Year") # adds label
plt.ylabel("Population") 
plt.title("World Population Projections") # adds title to plot
plt.yticks([0,2,4,6, 8, 10], ['0', '2B', '4B', '6B', '8B', '10B']) # first argument changes y axis to start from 0 with interval of 2
# second argument changes the display name of yticks, it should be same length as first argument

# shows a grid
plt.grid(True)

plt.show()

# s is size of marker
# c defines list of colors
# alpha changes opacity
# plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c = col, alpha=0.8)

