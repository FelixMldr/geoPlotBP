import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from scipy.stats import binom

# Central binomial distribution: n = 2k, p = 0.5
k = 2
n = 2 * k
p = 0.5

# Discrete values from 0 to n
values = np.arange(0, n + 1)

# PMF values
pmf = binom.pmf(values, n, p)

# Normalize for coloring
norm_pmf = pmf / np.max(pmf)
cmap = cm.magma

# Create the plot
fig, ax = plt.subplots(figsize=(8, 6))

# Plot x-axis colored points
for i, val in enumerate(values):
    ax.plot(val, 0, 'o', color=cmap(norm_pmf[i]), markersize=7)

# Plot y-axis colored points
for i, val in enumerate(values):
    ax.plot(0, val, 'o', color=cmap(norm_pmf[i]), markersize=7)

# Formatting
ax.set_xlim(-1, n + 1)
ax.set_ylim(-1, n + 1)
ax.set_aspect('equal')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title(f'Central Binomial Distribution Coloring (n={n}, p={p})')
ax.axhline(0, color='gray', linestyle='--', linewidth=1)
ax.axvline(0, color='gray', linestyle='--', linewidth=1)
ax.grid(True, linestyle='--', alpha=0.3)

# Add colorbar
sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=0, vmax=np.max(pmf)))
sm.set_array([])
plt.colorbar(sm, ax=ax, label='Probability Mass')

plt.show()
