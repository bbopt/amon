import cma
import subprocess

PREVIOUS_EVAL = {'x' : None, "result" :  None}

def f(x):
    if PREVIOUS_EVAL['x'] == str(x):
        return PREVIOUS_EVAL['result'][0]
    
    with open("x1.txt", 'w') as file:
        for param in x:
            file.write(f'{param} ')
    result = subprocess.run(['amon',  'run',  '6', 'x1.txt', '-s',  '1'],capture_output=True, text=True)
    print(result.stdout)
    lines = result.stdout.strip().split()
    PREVIOUS_EVAL['x'] = str(x)
    PREVIOUS_EVAL['result'] = [float(l) for l in lines]
    return float(lines[0])

def main():
    x0 = []
    with open('x0.txt', 'r') as initial_point_file:
        point = initial_point_file.readline().strip().split()
        for param in point:
            x0.append(float(param))

    xopt, _ = cma.fmin2(f, x0, 1000, options={'maxfevals': 500})
    
    print(xopt)

if __name__ == '__main__':
    main()