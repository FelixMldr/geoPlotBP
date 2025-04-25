import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from scipy.stats import binom

# Parameters for the two binomial distributions
n1, p1 = 10, 0.5  # X-axis binomial
n2, p2 = 10, 0.5  # Y-axis binomial

# Values for x and y
x = np.arange(0, n1 + 1)
y = np.arange(0, n2 + 1)
X, Y = np.meshgrid(x, y)

# Compute individual PMFs
px = binom.pmf(X, n1, p1)
py = binom.pmf(Y, n2, p2)

# Compute joint PMF (assuming independence)
joint_pmf = px * py

# Plotting the joint PMF as a heatmap
plt.figure(figsize=(8, 6))
heatmap = plt.imshow(joint_pmf, extent=(-5, 5, -5, 5), origin='lower', cmap='plasma', aspect='auto')
plt.colorbar(heatmap, label='Joint Probability')

# Axis labels and ticks
plt.title(f'Joint PMF of Two Binomial Distributions (n={n1}, p={p1})')
plt.xlabel('x (Successes from Binomial 1)')
plt.ylabel('y (Successes from Binomial 2)')
plt.xticks(np.arange(-5, 5 + 1))
plt.yticks(np.arange(-5, 5 + 1))
plt.grid(True, linestyle='--', alpha=0.3)

plt.show()
