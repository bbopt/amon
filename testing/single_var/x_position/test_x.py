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
    x_values = np.arange(13552, 16005, (16005-13552)/500)
    for val in x_values:
        print(f'{(val - 13552)/((16005-13552)/500)}% done')
        changeVariable(10, val, 'x3.txt')
        results.append(Result(subprocess.run(['amon', 'run', '3', 'x0.txt', '-s', '1', '-r', '--port', '9191'], capture_output=True, text=True).stdout.strip().split()))
    feasible_objs = []
    feasible_x    = []
    infeasible_objs = []
    infeasible_x    = []
    for x, result in zip(x_values, results):
        print(f'{result.obj:.4f}: {result.is_feasible}')
        if result.is_feasible:
            feasible_objs.append(result.obj)
            feasible_x.append(x)
        else:
            infeasible_objs.append(result.obj)
            infeasible_x.append(x)

    with open('results_feasible.txt', 'w') as f:
        for x in feasible_x:
            f.write(f' {x} ')
        f.write('\n')
        for obj in feasible_objs:
            f.write(f' {obj} ')

    with open('results_infeasible.txt', 'w') as f:
        for x in infeasible_x:
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
