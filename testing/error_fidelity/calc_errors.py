import subprocess
import numpy as np

def main():
    sum_differences = []
    for fidelity in range(6):
        sum_differences.append(0)

    for i in range(100):
        truth = float(subprocess.run(['amon', 'run', 'params.txt', f'x{i}.txt', '-s', '1'], capture_output=True, text=True).stdout.strip().split()[0])
        print(f'Iteration {i}')
        print('----')
        for fidelity in range(6):
            obj = float(subprocess.run(['amon', 'run', 'params.txt', f'x{i}.txt', '-s', '1', '-f', str(fidelity)], capture_output=True, text=True).stdout.strip().split()[0])
            sum_differences[fidelity] += (abs((truth-obj)/obj))
    
    with open('results.txt', 'w') as file:
        file.write(f'Fidelities: ')
        for fidelity in range(6):
            file.write(f'    {fidelity}     ')
        file.write(f'\nAvg diff : ')
        for sum_diff in sum_differences:
            file.write(f'{float(sum_diff/100):2.8f} ')


if __name__ == '__main__':
    main()