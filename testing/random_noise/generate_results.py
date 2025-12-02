import numpy as np
import subprocess

def main():
    obj = []
    for i in range(300):
        print(f'{i+1}th iteration of 300')
        output = subprocess.run(['amon', 'run', '2', 'point_3.txt'], capture_output=True, text=True).stdout.strip().split()
        # output = np.random.normal(0, 1), 0
        obj.append(output[0])
    with open('results/point_3.txt', 'w') as f:
        for elem in obj:
            f.write(f'{elem} ')

if __name__ == '__main__':
    main()
