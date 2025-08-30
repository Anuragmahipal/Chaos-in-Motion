import numpy as np
import pandas as pd 

from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


#importing data 
data = pd.read_csv("lorenz.csv")
x1, y1, z1 = data["x"].values, data["y"].values, data["z"].values

# Lorenz system
def lorenz(t, state, sigma=10, beta=8/3, rho=28):
    x, y, z = state
    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z
    return [dxdt, dydt, dzdt]

# Time range and initial condition
t_span = (0, 40)
y0 = [1, 1, 1]
t_eval = np.linspace(t_span[0], t_span[1], 10000)

# Solve using RK45 (like ode45 in MATLAB)
sol = solve_ivp(lorenz, t_span, y0, method="RK45", t_eval=t_eval)

x, y, z = sol.y




# Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Dark background
plt.style.use("dark_background")

# Initialize line and point
line1, = ax.plot([], [], [], lw=0.8, color="lime")
point1, = ax.plot([], [], [], "o", color="red", markersize=3)


line, = ax.plot([], [], [], lw=0.8, color="magenta")
point, = ax.plot([], [], [], "o", color="blue", markersize=3)

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
    # Line (history) of Inbuilt
    line.set_data(x[:num], y[:num])
    line.set_3d_properties(z[:num])

    #Line (history) of manual 
    line1.set_data(x1[:num], y1[:num])
    line1.set_3d_properties(z1[:num])
    
    # Current point (must be passed as list/array) of inbuilt
    point.set_data([x[num]], [y[num]])
    point.set_3d_properties([z[num]])

    # Current point (must be passed as list/array) of manual 
    point1.set_data([x1[num]], [y1[num]])
    point1.set_3d_properties([z1[num]])


    return line, line1 ,  point , point1

# Animate
ani = FuncAnimation(fig, update, frames=len(x), interval=1, blit=True)


plt.show()

