import matplotlib.pyplot as plt
from molecular_motion import RandomWalk

#   keep Making random walks and plot the points as long as active

#while True:
#   Make random walk and plot points
rw = RandomWalk(5000)
rw.fill_walk()

#  Set size of plotting window.
plt.figure(figsize=(10, 6))
points_numbers = list(range(rw.num_points))
plt.plot(rw.x_values, rw.y_values, c="red", linewidth=1)

#  Emphasize the first and last points
plt.scatter(0, 0, c="green", edgecolors="none", s=15)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c="red", edgecolors="none", s=15)

#  Remove the axes
plt.gca().get_xaxis().set_visible(False)
plt.gca().get_yaxis().set_visible(False)

# Save the RW_Visual
#plt.savefig("Random_Walk_Visual.png", bbox_inches="tight")
plt.show()

    #keep_running = input("Make Another Walk? (y/n): ")
    #if keep_running == "n".lower():
    #    break
        