import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Load the data
data = pd.read_csv("lorenz.csv")
x, y, z = data["x"].values, data["y"].values, data["z"].values

# Create figure
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

# Dark background
plt.style.use("dark_background")

# Initialize line and point
line, = ax.plot([], [], [], lw=0.8, color="cyan")
point, = ax.plot([], [], [], "o", color="red", markersize=3)

# Set axes limits
ax.set_xlim(min(x), max(x))
ax.set_ylim(min(y), max(y))
ax.set_zlim(min(z), max(z))

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Lorenz Attractor Animation")

# Animation function
def update(num):
    # Line (history)
    line.set_data(x[:num], y[:num])
    line.set_3d_properties(z[:num])
    
    # Current point (must be passed as list/array)
    point.set_data([x[num]], [y[num]])
    point.set_3d_properties([z[num]])
    return line, point

# Animate
ani = FuncAnimation(fig, update, frames=len(x), interval=1, blit=True)

plt.show()


