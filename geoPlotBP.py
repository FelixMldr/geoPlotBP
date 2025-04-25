import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from scipy.stats import binom

# Define the 2D Gaussian probability density function
def gaussian_2d(x, y):
    return (1 / (2 * np.pi)) * np.exp(-0.5 * (x**2 + y**2))

# Generate points along the x and y axes
x = np.linspace(-4, 4, 500)
y = np.linspace(-4, 4, 500)

# Compute probability values along the axes
#prob_x = binom.pmf(x,5,0.5)
#prob_y = binom.pmf(y,5,0.5)

prob_x = gaussian_2d(x, np.zeros_like(x))  # y = 0
prob_y = gaussian_2d(np.zeros_like(y), y)  # x = 0

# Normalize probabilities for colormap
norm_x = prob_x / np.max(prob_x)
norm_y = prob_y / np.max(prob_y)

# Choose a colormap
cmap = cm.viridis

#Set up the x axis
#x = np.linspace(-4, 4, 500)

#secret from {-eta, ..., eta}
sec = [1, -1]

#eq_coeffs from {-eta2, ..., eta2}
eqcs = [2, 2]

dist = [0.125,0.25,0.5,0.25,0.125]

rhs = sum(vi*wi for vi,wi in zip(eqcs,sec)) 

eqs = []
for b in range(rhs-2,rhs+3):
    eqs.append((b/eqcs[1]) - (eqcs[0]/eqcs[1])*x)


# Plot
fig, ax = plt.subplots(figsize=(8, 8))


for (a,b) in zip(eqs,dist):
    plt.plot(x,a,color='red', alpha=b)

# Plot the x-axis with color
for i in range(len(x) - 1):
    ax.plot(x[i:i+2], [0, 0], color=cmap(norm_x[i]), linewidth=1)

# Plot the y-axis with color
for i in range(len(y) - 1):
    ax.plot([0, 0], y[i:i+2], color=cmap(norm_y[i]), linewidth=1)

# Set limits and aspect
ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)
ax.set_aspect('equal')

# Add grid and labels
ax.set_title('Color-Coded Axes by 2D Gaussian Probability')
ax.set_xlabel('x1')
ax.set_ylabel('x2')

plt.grid(True, linestyle='--', alpha=0.5)
plt.show()

