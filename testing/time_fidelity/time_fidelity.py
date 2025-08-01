import subprocess
import time
import numpy as np
import matplotlib.pyplot as plt

total_runtime = []
for _ in range(6):
    total_runtime.append(0)

# Alternate fidelities ran to remove variation of cpu usage throughout the day bias
with open('x4.txt', 'r') as f:
    point = [float(val) for val in f.readline().strip().split()]
for i in range(200):
    print(f'{i}th iteration')
    for fidelity in range(6):
        print(f'Fidelity = {fidelity}')
        with open('x0.txt', 'w') as f:
            for pt in point[:22]:
                f.write(f'{np.random.normal(1, 1) * pt} ')        
            for pt in point[22:]:
                f.write(str(pt) + ' ')
        start_time = time.time()
        subprocess.run(['amon', 'run', '4', 'x0.txt', '-r', '-s', '1', '-f', f'{fidelity}'], capture_output=True)
        total_runtime[fidelity] += time.time() - start_time

avg_runtime = {}
for fidelity in range(6):
    avg_runtime[fidelity] = total_runtime[fidelity] / 200

with open('results.txt', 'w') as f:
    for fidelity in range(6):
        f.write(f'{fidelity}  ')
    f.write('\n')
    for fidelity in range(6):
        f.write(f'{avg_runtime[fidelity]:2.3f} ')

fidelity = range(6)
avg_runtime = list(avg_runtime.values())
plt.plot(fidelity, avg_runtime)
plt.xlabel('Fidelity')
plt.ylabel('Runtime [s]')
plt.title('Average runtime of instance 4 for different fidelities\n(seed = 1)')
