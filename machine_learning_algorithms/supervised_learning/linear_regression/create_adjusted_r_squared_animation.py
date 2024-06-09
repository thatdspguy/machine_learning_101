import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Generate integer data for n and k
n = np.arange(10, 201, 1)  # number of observations from 10 to 200
k = np.arange(1, 51, 1)  # number of predictors from 1 to 50
n, k = np.meshgrid(n, k)

# Create figure
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")


# Function to update the plot
def update(frame):
    R_squared = frame[0]
    angle = frame[1]
    ax.clear()
    with np.errstate(divide="ignore", invalid="ignore"):
        adjusted_R_squared = 1 - ((1 - R_squared) * (n - 1)) / (n - k - 1)
        adjusted_R_squared[n - k <= 1] = np.nan
        adjusted_R_squared[adjusted_R_squared <= 0] = 0
    ax.plot_surface(n, k, adjusted_R_squared, cmap="viridis")
    ax.set_xlabel("Number of Observations (n)")
    ax.set_ylabel("Number of Predictors (k)")
    ax.set_zlabel("Adjusted $R^2$")
    ax.set_zlim(0, 1)
    ax.set_title(f"Adjusted $R^2$\n($R^2$={R_squared:.2f})", fontsize=14, y=0.90)
    ax.view_init(elev=5, azim=angle)


# Create animation frames
R_squared_values = np.arange(0.05, 1, 0.01)
min_angle = 30
max_angle = 70
angles_1 = np.linspace(min_angle, max_angle, len(R_squared_values) // 2)
angles_2 = np.linspace(max_angle, min_angle, len(R_squared_values) // 2)
angles = np.concatenate((angles_1, angles_2))
angles = np.linspace(min_angle, max_angle, len(R_squared_values))
frames = list(zip(R_squared_values, angles))

# Create animation
ani = animation.FuncAnimation(fig, update, frames=frames, repeat=True)

# Save animation as GIF
ani.save(f"{os.path.dirname(__file__)}/adjusted_r_squared_animation.gif", writer="imagemagick", fps=10)

plt.close(fig)  # Close the figure to avoid displaying a static image here
