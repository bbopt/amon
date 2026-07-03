import cma
import subprocess

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

def main():
    # penalized_objective = cma.ConstrainedFitnessAL(f, constraints)
    x0 = []
    with open('x0.txt', 'r') as initial_point_file:
        point = initial_point_file.readline().strip().split()
        for param in point:
            x0.append(float(param))

    xopt, es = cma.fmin2(f, x0, 1, options={'maxfevals': 20000}, constraints=constraints)

    print(xopt)

if __name__ == '__main__':
    main()
