import numpy as np
import subprocess

class Result:
    def __init__(self, amon_output):
        self.obj = float(amon_output[0])
        self.is_feasible = True
        for elem in amon_output[1:]:
            if float(elem) > 0:
                self.is_feasible = False


def main():
    results = []
    y_values = np.arange(-5920, -4100, (5920-4100)/500)
    for i, val in enumerate(y_values):
        print(f'Iteration {i+1} of {len(y_values)}')
        changeVariable(9, val, 'x3.txt')
        results.append(Result(subprocess.run(['amon', 'run', '3', 'x0.txt'], capture_output=True, text=True).stdout.strip().split()))
    feasible_objs = []
    feasible_y    = []
    infeasible_objs = []
    infeasible_y    = []
    for y, result in zip(y_values, results):
        print(f'{result.obj:.4f}: {result.is_feasible}')
        if result.is_feasible:
            feasible_objs.append(result.obj)
            feasible_y.append(y)
        else:
            infeasible_objs.append(result.obj)
            infeasible_y.append(y)

    with open('results_feasible.txt', 'w') as f:
        for x in feasible_y:
            f.write(f' {x} ')
        f.write('\n')
        for obj in feasible_objs:
            f.write(f' {obj} ')

    with open('results_infeasible.txt', 'w') as f:
        for x in infeasible_y:
            f.write(f' {x} ')
        f.write('\n')
        for obj in infeasible_objs:
            f.write(f' {obj} ')
    

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
    main()
