import numpy as np
import subprocess

def main():
    obj = []
    for i in range(300):
        print(f'{i+1}th iteration')
        output = subprocess.run(['amon', 'run', '2', 'x2.txt'], capture_output=True, text=True).stdout.strip().split()
        # output = np.random.normal(0, 1), 0
        obj.append(output[0])
    with open('results.txt', 'w') as f:
        for elem in obj:
            f.write(f'{elem} ')

if __name__ == '__main__':
    main()