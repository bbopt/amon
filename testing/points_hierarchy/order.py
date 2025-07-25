import subprocess
import sys
import numpy as np

for fidelity in np.arange(0, 1.05, 0.05):
    results = {}
    for i in range(int(sys.argv[1])):
        print(f'{i+1}th iteration')
        results[i] = float(subprocess.run(['amon', 'run', 'params.txt', f'x{i}.txt', '-s', '1', '-f', f'{fidelity}'], capture_output=True, text=True).stdout.strip().split()[0])
    results = dict(sorted(results.items(), key=lambda item: item[1]))
    print('Writing...')
    with open("order.txt", 'a') as f:
        f.write(f'\nFidelity = {fidelity:.2f}\n')
        f.write('---------------\n')
        for point, obj in results.items():
            f.write(f'Point {point:2} : obj = {obj}\n')
    with open("quick_comparison.txt", 'a') as f:
        f.write(f'Fidelity = {fidelity:1.2f}: [ ')
        for point in results:
            f.write(f'{point:2} ')
        f.write(']\n')
