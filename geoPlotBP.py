import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from scipy.stats import binom

# Constants/Parameters
ETA = 2
ETA2 = 3
PINIT = 0.5
RSZ = 2*ETA + 1 # Range size {-2,..,2} => 5    

def ploting(distx1, dists1, hint, sec):
    #distx1 = [-ETA,...,ETA]
    #distx2 = [-ETA,...,ETA]
    #hint = 2d-equation ([INT],[(INT,float)])
    #sec = 2d-point [s1,s2]
    
    joint_pmf = np.outer(distx1, dists1)

    # For one hint plot the lines for different b with their prob.
    xlat = np.linspace(-ETA,ETA)
    (s,t) = hint
    mar = 0
    for i in t:
        a = (i[0]/s[1]) - (s[0]/s[1])*xlat
        plt.plot(xlat,a,color='red', alpha=i[1])
        for z in a:
            u = np.abs(z)
            if mar < u:
                mar = u
    
    # Plot heatmap
    heatmap = plt.imshow(joint_pmf, extent=(-mar, mar, -mar, mar), origin='lower', cmap='viridis', aspect='auto',interpolation='bilinear', alpha=0.7)
    
    # Project the secret in 2D
    secp = sum(vi*xi for vi,xi in zip(hint[0][1:],sec[1:]))
    # Plot secret
    plt.plot(sec[0],secp,'bo', markersize=5, label="sec")
    
    # Plot heatmap bar
    plt.colorbar(heatmap, label='Probability')
    # Add grid and labels
    plt.title(f'Geometric depiction of dist. hint solver')
    plt.xlabel('x1')
    plt.ylabel('S1')
    plt.xticks(np.arange(-mar, mar+1))
    plt.yticks(np.arange(-mar, mar+1))
    plt.grid(True, linestyle='--', alpha=0.5)
    return plt

def main():
    # Create distx1
    distx1 = [0.0625,0.25,0.375,0.25,0.0625]
    # Create distx2
    distx2 = [0.0625,0.25,0.375,0.25,0.0625]
    # Create distx3
    distx3 = [0.0625,0.25,0.375,0.25,0.0625]
    
    jointdist = np.outer(distx2,distx3)
    # Create sec
    sec = [1,-1,-1]
    # Create hint
    eq = [1,1,1]
    # Compute b
    b = sum(vi*wi for vi,wi in zip(eq,sec))
    # Create hintDist
    hintDist = [(b,0.9),(b-1,0.1)] 
    # Create hint
    hint = (eq,hintDist)
    # Plot graph and save it
    plots = ploting(distx1,jointdist,hint,sec)
    plots.savefig('GeoAppBPsolver.png', dpi=300, bbox_inches='tight')
    plots.show()


if __name__ == "__main__":
    main()