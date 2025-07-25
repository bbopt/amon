import sys
import subprocess
import numpy as np
import pathlib

def make_point(point_file, nb_turbines):
    with open(point_file, 'r') as f:
        point = next(f).strip().split()
    coords = point[0:2*nb_turbines]
    types = [np.random.randint(0, 5) for _ in range(nb_turbines)]
    with open(point_file, 'w') as f:
        for coord in coords:
            f.write(coord)
            f.write(' ')
        for t in types:
            f.write(str(t))
            f.write(' ')
    return types

def main():
    nb_tests = 4
    obj_funcs = ['lcoe', 'roi']
    nb_turbines = [12, 21, 6, 11]

    for test in range(1, nb_tests):
        for obj_func in obj_funcs:
            best_obj = sys.maxsize
            best_types = [0 for _ in range(nb_turbines[test])]
            print(f'For test {test+1}, obj {obj_func}')
            param_file = pathlib.Path(f'test_{test+1}_{obj_func}/params_amon.txt')
            point_file = pathlib.Path(f'test_{test+1}_{obj_func}/x0.txt')
            result_file = pathlib.Path(f'test_{test+1}_{obj_func}/best_types.txt')
            for _ in range(int(sys.argv[test + 1])):
                types = make_point(point_file, nb_turbines[test])
                if test == 4: # constraint-free one
                    obj = float(subprocess.run(['amon', 'run', param_file, point_file, '-f', '0.6', '-r'], capture_output=True, text=True).stdout.strip())
                else:
                    output = subprocess.run(['amon', 'run', param_file, point_file, '-f', '0.6', '-r'], capture_output=True, text=True).stdout.strip().split()
                    output = [float(val) for val in output]
                    obj = output[0]
                if obj < best_obj:
                    best_obj = obj
                    best_types = types
                print(f'Best obj  : {best_obj}, obj: {obj}')
            with open(result_file, 'w') as f:
                f.write(' '.join(str(t) for t in best_types))

if __name__ == '__main__':
    main()