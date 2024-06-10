import matplotlib.pyplot as plt

#   Plotting Squares against their numbers

numbers = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(numbers, squares, linewidth=2, color="black")     

#  Set chart title and label axes.
plt.title("Squares Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

#   Set size of tick labels.
plt.tick_params(axis="both", labelsize=14)

plt.show()