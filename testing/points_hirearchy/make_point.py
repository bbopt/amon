import subprocess
import numpy as np

for i in range(20):
    while True:
        with open(f'x{i}.txt', 'w') as f:
            for _ in range(15):
                f.write(f'{np.random.uniform(-1000, 2500)} {np.random.uniform(-1300, 800)} ')
        output = subprocess.run(['amon', 'run', 'params.txt', f'x{i}.txt', '-f', '0.1', '-s', '1'], capture_output=True, text=True).stdout.strip().split()
        print(output)
        if float(output[1]) <= 0 and float(output[2]) <= 0:
            break