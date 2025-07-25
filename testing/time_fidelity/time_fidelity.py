import subprocess
import time
import numpy as np
import matplotlib.pyplot as plt

total_runtime = {}
for fidelity in np.arange(0, 1.05, 0.05):
    total_runtime[fidelity] = 0

# Alternate fidelities ran to remove variation of cpu usage throughout the day bias
with open('x4.txt', 'r') as f:
    try:
        point = [int(val) for val in f.readline().strip().split()]
    except Exception:
        point = [float(val) for val in f.readline().strip().split()]
for i in range(1000):
    print(f'{i}th iteration')
    for fidelity in np.arange(0, 1.05, 0.05):
        with open('x0.txt', 'w') as f:
            for pt in point[:22]:
                f.write(f'{np.random.normal(1, 1) * pt}')        
            for pt in point[22:]:
                f.write(point)
        start_time = time.time()
        subprocess.run(['amon', 'run', '4', 'x0.txt', '-s', '1', '-f', f'{fidelity}'], capture_output=True)
        total_runtime[fidelity] += time.time() - start_time

avg_runtime = {}
for fidelity in np.arange(0, 1.05, 0.05):
    avg_runtime[fidelity] = total_runtime[fidelity] / 300

with open('results.txt', 'w') as f:
    for fidelity in np.arange(0, 1.05, 0.05):
        f.write(f'{fidelity:1.2f}  ')
    f.write('\n')
    for fidelity in np.arange(0, 1.05, 0.05):
        f.write(f'{avg_runtime[fidelity]:2.3f} ')

fidelity = np.arange(0, 1.05, 0.05)
avg_runtime = list(avg_runtime.values())
plt.plot(fidelity, avg_runtime)
plt.xlabel('Fidelity')
plt.ylabel('Runtime [s]')
plt.title('Average runtime of instance 4 for different fidelities\n(seed = 1)')
