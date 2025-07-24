import subprocess
import time
import numpy as np
import matplotlib.pyplot as plt

def main():
    sum_differences = {}
    for fidelity in np.arange(0, 0.15, 0.05):
        sum_differences[fidelity] = 0

    for i in range(2):
        truth = float(subprocess.run(['amon', 'run', 'params.txt', f'x{i}.txt', '-s', '1'], capture_output=True, text=True).stdout.strip().split()[0])
        print(truth)
        print('----')
        for fidelity in np.arange(0, 0.15, 0.05):
            obj = float(subprocess.run(['amon', 'run', 'params.txt', f'x{i}.txt', '-s', '1', '-f', str(fidelity)], capture_output=True, text=True).stdout.strip().split()[0])
            sum_differences[fidelity] += (abs((truth-obj)/obj))
            print(sum_differences)
    
    with open('results.txt', 'w') as file:
        file.write(f'Fidelities: ')
        for fidelity in sum_differences:
            file.write(f'   {fidelity:1.2f}    ')
        file.write(f'\nAvg diff : ')
        for sum_diff in sum_differences.values():
            file.write(f'{float(sum_diff/100):2.8f} ')


if __name__ == '__main__':
    main()