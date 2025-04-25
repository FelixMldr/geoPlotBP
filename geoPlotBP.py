import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from scipy.stats import binom

#Constants/Parameters
ETA = 2
ETA2 = 3


# Parameters for the two binomial distributions
n1, p1 = 4, 0.5  # X-axis binomial
n2, p2 = 4, 0.5  # Y-axis binomial

B = 5 # Number of different b 

bo = n1/2

# Generate points along the x and y axes
x = np.arange(0, n1 + 1)
y = np.arange(0, n1 + 1)
X, Y = np.meshgrid(x,y)

xlat = np.arange(-bo,bo+1)
xlon = np.arange(-bo, bo+1)

# Compute probability values along the axes
prob_x = binom.pmf(X,n1,p1)
prob_y = binom.pmf(Y,n2,p2)
#prob_b = binom.pmf(B, )

#joint probability
joint_pmf = prob_x * prob_y

# Normalize probabilities for colormap
#norm_x = prob_x / np.max(prob_x)
#norm_y = prob_y / np.max(prob_y)

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
    eqs.append(((b+n1)/eqcs[1]) - (eqcs[0]/eqcs[1])*x)


# Plot
#fig, ax = plt.subplots(figsize=(8, 8))


for (a,b) in zip(eqs,dist):
    plt.plot(xlat,a,color='red', alpha=b)
    
plt.plot(sec[0],sec[1], 'bo', markersize=5, label="Sec")

heatmap = plt.imshow(joint_pmf, extent=(-bo, bo, -bo, bo), origin='lower', cmap='viridis', aspect='auto', alpha=0.7)

plt.colorbar(heatmap, label='Probability')

# Plot the x-axis with color
#for i in range(len(x) - 1):
#    ax.plot(x[i], 0,'o', color=cmap(norm_x[i]), markersize=10)

# Plot the y-axis with color
#for i in range(len(y) - 1):
#    ax.plot(0, y[i],'o', color=cmap(norm_y[i]), markersize=10)

def ploting(distx1, distx2, hint):
    #distx1 = [-nu, ..., nu]
    return 0

# Set limits and aspect
#ax.set_xlim(-4, 4)
#ax.set_ylim(-4, 4)
#ax.set_aspect('equal')

# Add grid and labels
plt.title(f'BP initial joint binomial dist')
plt.xlabel('x1')
plt.ylabel('x2')
plt.xticks(np.arange(-bo, bo + 1))
plt.yticks(np.arange(-bo, bo + 1))
plt.grid(True, linestyle='--', alpha=0.3)
plt.savefig('my_plot.png', dpi=300, bbox_inches='tight')
plt.show()

