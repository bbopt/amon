import sys
import numpy as np
import subprocess
import csv


class Result:
    def __init__(self, x, y, amon_output):
        self.x = float(x)
        self.y = float(y)
        self.obj = float(amon_output[0])
        self.is_feasible = True
        for constraint in amon_output[1:]:
            if float(constraint) > 0:
                self.is_feasible = False

def main(filename):
    results = []
    x_values = np.arange(6750, 8000, (8000-6750)/100)
    y_values = np.arange(-2950, -2000, (2950-2000)/100)
    for i, y in enumerate(y_values):
        for j, x in enumerate(x_values):
            print(f'{((i*len(x_values) + j)/(len(y_values)*len(x_values))) * 100:.2f}% done')
            changeVariable(0, x, 'x7.txt')
            changeVariable(1, y, 'x0.txt')
            output = subprocess.run(['amon', 'run', 'params.txt', 'x0.txt', '-s', '1', '-r', '--port', '4321'], capture_output=True, text=True).stdout.strip().split()
            results.append(Result(x, y, output))

    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["x", "y", "obj", "is_feasible"])
        for r in results:
            writer.writerow([r.x, r.y, r.obj, r.is_feasible])
    

def changeVariable(index, value, point_file):
    with open(point_file, 'r') as source_file:
        point = source_file.readline().strip().split()
    try:
        point[index] = value
    except IndexError as e:
        print(f'No index {index}: {e}')
    with open('x0.txt', 'w') as target_file:
        for var in point:
            target_file.write(f'{var} ')

if __name__ == '__main__':
    if len(sys.argv) == 1:
        main('results.csv')
    else:
        main(sys.argv[1])
