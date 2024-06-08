import matplotlib.pyplot as plt
import numpy as np

plot_filename = "slope_intercept_plot.png"


# Parameters for the line
m = 2  # slope
b = 9  # bias

# Generate x values
x = np.linspace(-5, 2, 100)


# Calculate y values based on the slope-intercept form
def y(x):
    return m * x + b


# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(x, y(x), label=f"$y = {m}x + {b}$", color="blue")
plt.axhline(0, color=(0.2, 0.2, 0.2), linewidth=1)
plt.axvline(0, color=(0.2, 0.2, 0.2), linewidth=1)
plt.grid(color=(0.7, 0.7, 0.7), linestyle="--", linewidth=0.5)

# Highlight the y-intercept
plt.scatter(0, b, color="red")
plt.text(0.1, b * 0.9, f"$b = {b}$", fontsize=12)

# Add slope triangle
x1 = -2.5
x2 = x1 + 1
y1 = y(x1)
y2 = y(x2)
plt.plot([x1, x2], [y1, y1], color=(0.2, 0.2, 0.2), linestyle="--")
plt.plot([x2, x2], [y1, y2], color=(0.2, 0.2, 0.2), linestyle="--")
# x delta
plt.plot([x1, (x1 + x2) / 2 - 0.15], [y1 - 0.25, y1 - 0.25], color="black", linewidth=0.5)
plt.plot([(x1 + x2) / 2 + 0.15, x2], [y1 - 0.25, y1 - 0.25], color="black", linewidth=0.5)
plt.plot([x1, x1], [y1 - 0.35, y1 - 0.15], color="black", linewidth=0.5)
plt.plot([x2, x2], [y1 - 0.35, y1 - 0.15], color="black", linewidth=0.5)
plt.text((x1 + x2) / 2 - 0.1, y1 - 0.5, r"$\Delta x$", fontsize=10)
# y delta
plt.plot([x2 + 0.09, x2 + 0.09], [y1, (y1 + y2) / 2 - 0.35], color="black", linewidth=0.5)
plt.plot([x2 + 0.09, x2 + 0.09], [(y1 + y2) / 2 + 0.35, y2], color="black", linewidth=0.5)
plt.plot([x2 + 0.06, x2 + 0.12], [y1, y1], color="black", linewidth=0.5)
plt.plot([x2 + 0.06, x2 + 0.12], [y2, y2], color="black", linewidth=0.5)
plt.text(x2 + 0.05, (y1 + y2) / 2 - 0.2, r"$\Delta y$", fontsize=10)

# m formula
plt.text(x2 + 0.1, y1 - 1.2, rf"$m = \frac{{\Delta y}}{{\Delta x}} = \frac{{{m}}}{{1}} = {{{m}}}$", fontsize=12)

# Add labels and title
plt.xlabel("$x$", fontsize=14)
plt.ylabel("$y$", fontsize=14, rotation=0, labelpad=10)
plt.title("Equation of a Line\n$y = m x + b$", fontsize=16, pad=15)
plt.xlim((-5, 2))
plt.legend()
plt.savefig("machine_learning_algorithms/supervised_learning/linear_regression/slope_intercept_plot.png", dpi=300)
plt.show()
