import matplotlib.pyplot as plt
from matplotlib import patches

# how to make a circle in matplotlib

circle1 = plt.Circle((2, 2), 0.2, color="r")
rectangle = patches.Rectangle(
    (1, 1), 2, 2, linewidth=1, facecolor="none", color="white"
)
background = patches.Rectangle((0, 0), 4, 4, color="black")

# show the circle
fig, ax = plt.subplots()
fig.set_visible(True)
ax.add_artist(background)
ax.add_artist(rectangle)
ax.add_artist(circle1)
ax.set_xlim((0, 4))
ax.set_ylim((0, 4))
plt.show()
