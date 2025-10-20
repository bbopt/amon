import subprocess
import numpy as np

with open('x4.txt', 'r') as f:
    point = f.readline().split()

prices = []

for i in range(500):
    types = np.random.randint(0, 6, size=11)
    point[22:33] = [str(t) for t in types]
    with open('x4.txt', 'w') as f:
        for elem in point:
            f.write(f'{elem} ')

    result = subprocess.run(['amon', 'run', '4', 'x4.txt', '-r', '--port', '4444'], capture_output=True, text=True).stdout.strip().split()
    print(f'Iteration {i:3} \n\t {types} : {result}')
    prices.append(float(result[4]))

with open('results.txt', 'w') as f:
    for price in prices:
        f.write(f'{price} ')
