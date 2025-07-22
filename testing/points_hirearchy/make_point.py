import subprocess
import numpy as np

for i in range(20):
    while True:
        with open(f'x{i}.txt', 'w') as f:
            for _ in range(10):
                f.write(f'{np.random.uniform(104545, 107487)} {np.random.uniform(1043680, 1045498)} ')
        output = subprocess.run(['amon', 'run', 'params.txt', f'x{i}.txt', '-f', '0.1', '-s', '1'], capture_output=True, text=True).stdout.strip().split()
        print(output)
        if float(output[1]) <= 0 and float(output[2]) <= 0:
            break