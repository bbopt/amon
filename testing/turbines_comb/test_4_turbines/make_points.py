import subprocess
import numpy as np
import itertools
import sys

def main():
    for i in range(int(sys.argv[1])):
        print(f'Point {i}')
        print('---------')
        while True:
            with open(f'x{i}.txt', 'w') as f:
                for _ in range(4):
                    f.write(f'{np.random.uniform(-1000, 2500)} {np.random.uniform(-1300, 800)} ')
            output = subprocess.run(['amon', 'run', 'params.txt', f'x{i}.txt', '-f', '0.1', '-s', '1'], capture_output=True, text=True).stdout.strip().split()
            print(output)
            if float(output[1]) <= 0 and float(output[2]) <= 0:
                break