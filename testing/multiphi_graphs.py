from scipy.stats import qmc
import subprocess
from itertools import combinations
import matplotlib.pyplot as plt
import numpy as np
from math import comb

###############
#Problems list#
###############

N_HELIOSTATS_UPPER = 5001-1e-9
N_BAFFLES_UPPER = 11-1e-9
N_TUBES_UPPER = 30001-1e-9
problem2 = {'n' : 14,
			'm' : 12,
			'upper' : (40.0, 40.0, 250.0, 30.0, 30.0, N_HELIOSTATS_UPPER, 89.0, 20.0, 20.0, 995.0, 9425-1e-9, 5.00,  0.100, 0.1),
			'lower' : (1.0, 1.0, 20.0, 1.0, 1.0, 1, 1.0, 0.0, 1.0, 793.0, 1, 0.01, 0.005, 0.005),
			'id':2,
			'A': [[2,0,-1,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,-1,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,1,-1]], #Linear constraints matrix
			'linearAPrioriConstraintsIndices': (4,5,10),
			'integerVariablesIndices':(6,11)
			}
problem3 = {'n' : 20,
			'm' : 13,
			'upper' : (40.0, 40.0, 250.0, 30.0, 30.0, N_HELIOSTATS_UPPER, 89.0, 20.0, 20.0, 995.0, 50.0, 30.0, 5.00, 5.00, 650.0, 9425-1e-9, 5.00, 0.100, 0.100, 9-1e-9 ),
			'lower' : (1.0, 1.0, 20.0, 1.0, 1.0, 1, 1.0, 0.0, 1.0, 793.0, 1.0, 1.0, 0.01, 0.01, 495.0, 1, 0.01, 0.005, 0.005, 1),
			'id':3,
			'A' : [[2,0,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,-1,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,-1,0]],
			'linearAPrioriConstraintsIndices': (3,4,10),
			'integerVariablesIndices':(6,16,20)
			}
problem4 = {'n' : 29,
			'm' : 16,
			'upper' : (40.0, 40.0, 250.0, 30.0, 30.0, N_HELIOSTATS_UPPER, 89.0, 20.0, 20.0, 995.0, 50.0, 30.0, 5.00, 5.00, 650.0, 7854-1e-9, 5.00, 0.1000, 0.100, 0.200, 10.0, 0.1000, 0.100, 0.40, N_BAFFLES_UPPER, N_TUBES_UPPER, 11-1e-9, 10-1e-9, 9-1e-9),
			'lower' : (1.0, 1.0, 20.0, 1.0, 1.0, 1, 1.0, 0.0, 1.0, 793.0, 1.0, 1.0, 0.01, 0.01, 495.0, 1, 0.01, 0.0050, 0.006, 0.007, 0.5 , 0.0050, 0.006, 0.15, 2, 1, 1, 1, 1),
			'id':4,
			'A' : [[2,0,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
				   [0,0,0,0,0,0,0,1,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
				   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,-1,0,0,0,0,0,0,0,0,0,0],
				   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,0,0,1,0,0,0,0,0,0],
				   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,-1,0,0,0,0,0,0]],
			'linearAPrioriConstraintsIndices': (3,4,10,14,15),
			'integerVariablesIndices':(6,16,25,26,27,28,29)
			}
problem7 = {'n' : 7,
			'm' : 6,
			'upper' : (30.0, 30.0, 995.0, 8568-1e-9, 5.00, 0.100, 0.1000),
			'lower' : (1.0, 1.0, 793.0, 1 , 0.01, 0.005, 0.0055),
			'id':7,
			'A':[[0,0,0,0,0,1,-1]],
			'linearAPrioriConstraintsIndices': (3,),
			'integerVariablesIndices':(4,)
			}
problems = (problem2, problem3, problem4, problem7)
######################
#Function definitions#
######################

def precedes(x1,x2):
    # x1 and x2 are of the form [obj cst cst cst ...]
    #Returns True if x1 precedes x2.
    
    x1feas = all(x1i<=0 for x1i in x1[1:])
    x2feas = all(x2i<0 for x2i in x2[1:])
    
    if x1feas and x2feas:
        return x1[0] < x2[0]
    
    elif x1feas or x2feas:
        return x1feas
    
    else:
        def h(x):
            return sum([max(0,xi) for xi in x[1:]])
        return h(x1)<h(x2)

def generateLHS(problem, nbPoints):
    sampler = qmc.LatinHypercube(problem['n'])
    sample = sampler.random(n=nbPoints)
    points = qmc.scale(sample, problem['lower'], problem['upper'])

    #Truncate integer variables
    for p in points:
        for i in range(len(p)):
            if i+1 in problem['integerVariablesIndices']:
                p[i] = int(p[i])

    with open(f"solar{problem['id']}_x0.txt", "w") as f:
        for p in points:
            f.write(' '.join(map(str, p))+ '\n')

def runSolar(phi):
    print("Phi = "+ str(phi))
    out = subprocess.run(f"$SOLAR_HOME/bin/solar {problem['id']} solar{problem['id']}_x0.txt -fid={phi}",
                        shell=True, text=True, capture_output=True, check=False).stdout.split()
    out = [float(elem) for elem in out]
    out = [out[i:i+problem['m']+1] for i in range(0, len(out), problem['m']+1)]
    return out

def computeCombinations(phi):
    return [precedes(x1,x2) for x1,x2 in combinations(runSolar(phi), 2)]

def computePercentage(phi):
    return sum([a==b for a,b in zip(computeCombinations(phi), resultsHighFid)])/comb(N_POINTS,2)

#################
#Plotting graphs#
#################
fid = np.linspace(0,0.95,20)
N_POINTS = 1000

for problem in problems:
    generateLHS(problem, N_POINTS)
    resultsHighFid = computeCombinations(1)
    plt.figure()
    plt.plot(fid, [computePercentage(phi) for phi in fid])
    plt.title(f"Instance {problem['id']}, {N_POINTS} points")
    plt.xlabel(r"$\phi$")
    plt.ylabel("% de combinaisons de deux points ayant la même relation de précédence qu'à fidélité maximale")
    plt.savefig(f"graphe_fid_{problem['id']}.png")



