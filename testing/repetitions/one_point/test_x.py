import numpy as np
import subprocess

def main():
    results = []
    for i in range(1000):
        print(f'Iteration {i+1} of 1000')
        results.append(float(subprocess.run(['amon', 'run', '3', 'x0.txt', '-r', '--port', '8989'], capture_output=True, text=True).stdout.strip().split()[0]))

    with open('results.txt', 'w') as f:
        for result in results:
            f.write(f' {result} ')

if __name__ == '__main__':
    main()
