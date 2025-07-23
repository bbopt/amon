import subprocess
import time
import numpy as np
import matplotlib.pyplot as plt

total_runtime = {}
for fidelity in np.arange(0, 1.01, 0.01):
    total_runtime[fidelity] = 0

# Alternate instances ran to remove variation of cpu usage throughout the day bias
for i in range(300):
    for fidelity in np.arange(0, 1.01, 0.01):
        start_time = time.time()
        subprocess.run(['amon', 'run', '4', 'x4.txt', '-s', '1', '-f', f'{fidelity}'], capture_output=True)
        total_runtime[fidelity] += time.time() - start_time

avg_runtime = {}
for fidelity in np.arange(0, 1.01, 0.01):
    avg_runtime[fidelity] = total_runtime[fidelity] / 300

with open('results.txt', 'w') as f:
    for fidelity in np.arange(0, 1.01, 0.01):
        f.write(f'{fidelity:1.2f}  ')
    f.write('\n')
    for fidelity in np.arange(0, 1.01, 0.01):
        f.write(f'{avg_runtime[fidelity]:2.3f} ')

fidelity = np.arange(0, 1.01, 0.01)
avg_runtime = list(avg_runtime.values())
plt.plot(fidelity, avg_runtime)
plt.xlabel('Fidelity')
plt.ylabel('Runtime [s]')
plt.title('Average runtime of instance 4 for different fidelities\n(seed = 1)')
