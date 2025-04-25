import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from scipy.stats import binom

# Binomial distribution parameters
n = 5     # number of trials
p = 0.5     # probability of success

# x and y values representing number of successes (discrete)
x = np.arange(0, n + 1)
y = np.arange(0, n + 1)

# Binomial PMF along x and y axes
prob_x = binom.pmf(x, n, p)
prob_y = binom.pmf(y, n, p)

# Normalize for colormap
norm_x = prob_x / np.max(prob_x)
norm_y = prob_y / np.max(prob_y)

# Choose colormap
cmap = cm.plasma

# Plotting
fig, ax = plt.subplots(figsize=(8, 6))

# Plot colored x-axis points
for i in range(len(x)):
    ax.plot(x[i], 0, 'o', color=cmap(norm_x[i]), markersize=10)

# Plot colored y-axis points
for i in range(len(y)):
    ax.plot(0, y[i], 'o', color=cmap(norm_y[i]), markersize=10)

# Draw zero axis lines
ax.axhline(0, color='gray', linewidth=1, linestyle='--')
ax.axvline(0, color='gray', linewidth=1, linestyle='--')

# Set limits
ax.set_xlim(-1, n + 1)
ax.set_ylim(-1, n + 1)
ax.set_aspect('equal')

# Labels and title
ax.set_title(f'Binomial Distribution Coloring on Axes (n={n}, p={p})')
ax.set_xlabel('x (number of successes)')
ax.set_ylabel('y (number of successes)')

plt.grid(True, linestyle='--', alpha=0.3)
plt.show()
