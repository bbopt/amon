import cma
import subprocess
from scipy.optimize import minimize

PREVIOUS_EVAL = {'x' : None, "result" :  None}

def f(x):
    if PREVIOUS_EVAL['x'] == str(x):
        return PREVIOUS_EVAL['result'][0]
    
    with open("x1.txt", 'w') as file:
        for param in x:
            file.write(f'{param} ')
    result = subprocess.run(['amon',  'run',  '1', 'x1.txt', '-s',  '1', '-r', '--port', '1111'],capture_output=True, text=True)
    print(result.stdout)
    lines = result.stdout.strip().split()
    PREVIOUS_EVAL['x'] = str(x)
    PREVIOUS_EVAL['result'] = [float(l) for l in lines]
    return float(lines[0])

def constraints(x):
    if PREVIOUS_EVAL['x'] == str(x):
        return PREVIOUS_EVAL['result'][1:]

    with open("x1.txt", 'w') as file:
        for param in x:
            file.write(f'{param} ')
    result = subprocess.run(['amon',  'run',  '1', 'x1.txt', '-s',  '1', '-r', '--port', '1111'],capture_output=True, text=True)
    print(result.stdout)
    lines = result.stdout.strip().split()
    PREVIOUS_EVAL['x'] = str(x)
    PREVIOUS_EVAL['result'] = [float(l) for l in lines]
    return [float(l) for l in lines[1:]]

def c1(x):
    return constraints(x)[0]

def c2(x):
    return constraints(x)[1]


def main():
    x0 = []
    with open('x0.txt', 'r') as initial_point_file:
        point = initial_point_file.readline().strip().split()
        for param in point:
            x0.append(float(param))
    constraints_dicts = [{'type':'ineq', 'fun':c1}, {'type':'ineq', 'fun':c2}]

    result = minimize(f, x0, method='COBYLA', constraints=constraints_dicts)
    print(f'Best f value : {result.fun}')
    print(f'Point : {result.x}')

if __name__ == '__main__':
    main()
