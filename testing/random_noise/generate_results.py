import numpy as np
import subprocess

def main():
    obj = []
    for _ in range(300):
        output = subprocess.run(['amon', 'run', '2', 'x2.txt'], capture_output=True, text=True).stdout.strip().split()
        obj.append(output[0])
    with open('results.txt', 'w') as f:
        for elem in obj:
            f.write(f'{elem} ')

if __name__ == '__main__':
    main()