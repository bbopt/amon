import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

def main():
    with open('results.txt', 'r') as f:
        objs = f.readline().strip().split()
    objs = [float(obj) for obj in objs]

    mean, std = np.mean(objs), np.std(objs)

    count, bins, _ = plt.hist(objs, bins=100, density=True, alpha=0.6, edgecolor='black', label='Data')

    x = np.linspace(min(objs), max(objs), 1000)
    plt.plot(x, norm.pdf(x, mean, std), label='Gaussian approximation')

    plt.title(f'Random noise in the objective function of instance 2\n' + r'$\mu \semeq {mean}$, $\sigma \semeq {std}')
    plt.grid()
    plt.xlabel('Objective function')
    plt.ylabel('Proportion')
    plt.show()

if __name__ == '__main__':
    main()

