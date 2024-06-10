import matplotlib.pyplot as plt
from matplotlib import colormaps

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values,y_values , c=y_values,cmap=plt.cm.Reds, edgecolor="none", s=40)

#   Set chart title and label axes
plt.title("Square Numbers", fontsize=24)
plt.xlabel("value", fontsize=24)
plt.ylabel("Square Of Value", fontsize=14)

#Set size of tick labels
plt.tick_params(axis="both", which="major", labelsize=14)

#   Set the range of Each axis
plt.axis([0, 1100, 0, 1100000])

plt.show()

#   To save your plot
#plt.savefig("Squares_Plot.png", bbox_inches="tight")