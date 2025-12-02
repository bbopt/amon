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
    x_values = np.arange(13552, 16005, (16005-13552)/499)
    for i, val in enumerate(x_values):
        print(f'Iteration {i+1} of {len(x_values)}')
        changeVariable(10, val, 'x3.txt')
        point_results = []
        for i in range(250):
            point_results.append(Result(subprocess.run(['amon', 'run', '3', 'x0.txt', '-r', '--port', '4321'], capture_output=True, text=True).stdout.strip().split()))
        results.append(point_results)
    feasible_objs = []
    feasible_x    = []
    infeasible_objs = []
    infeasible_x    = []
    for x, point_results in zip(x_values, results):
        point_objs = []
        if point_results[0].is_feasible:
            for result in point_results:
                point_objs.append(result.obj)
            feasible_x.append(x)
            feasible_objs.append(point_objs)
        else:
            for result in point_results:
                point_objs.append(result.obj)
            infeasible_x.append(x)
            infeasible_objs.append(point_objs)

    with open('x_feasible.txt', 'w') as f:
        for x in feasible_x:
            f.write(f'{x}\n')

    with open('obj_feasible.txt', 'w') as f:
        for point_objs in feasible_objs:
            for obj in point_objs:
                f.write(f'{obj} ')
            f.write('\n')

    with open('x_infeasible.txt', 'w') as f:
        for x in infeasible_x:
            f.write(f'{x}\n')

    with open('obj_infeasible.txt', 'w') as f:
        for point_objs in infeasible_objs:
            for obj in point_objs:
                f.write(f'{obj} ')
            f.write('\n')



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
