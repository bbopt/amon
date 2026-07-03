import numpy as np
import subprocess
from pymoo.core.problem import Problem
from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.optimize import minimize

N_VAR = 30
INT_IDX = list(range(12, 18))

PREVIOUS_EVAL = {'x' : None, "result" :  None}

def f(x):
    if PREVIOUS_EVAL['x'] == str(x):
        return PREVIOUS_EVAL['result'][0]
    
    with open("x1.txt", 'w') as file:
        for param in x:
            file.write(f'{param} ')
    result = subprocess.run(['amon',  'run',  '8', 'x1.txt', '-s',  '1', '-r', '--port', '1111'],capture_output=True, text=True)
    print(result.stdout)
    lines = result.stdout.strip().split()
    PREVIOUS_EVAL['x'] = str(x)
    PREVIOUS_EVAL['result'] = [float(l) for l in lines]
    return [float(l) for l in lines]

def f_1(x):
    return f(x)[0]

def f_2(x):
    return f(x)[1]

def c_1(x):
    return f(x)[2]

def c_2(x):
    return f(x)[3]

def c_3(x):
    return f(x)[4]

class MyProblem(Problem):
    def __init__(self):
        super().__init__(
            n_var=N_VAR,
            n_obj=2,
            n_ieq_constr=3,
        )

    def _evaluate(self, X, out, *args, **kwargs):
        X = X.copy()
        X[:, INT_IDX] = np.round(X[:, INT_IDX])

        n = X.shape[0]
        F = np.zeros((n, 2))
        G = np.zeros((n, 3))

        for i in range(n):
            values = f(X[i])
            F[i, 0] = values[0]
            F[i, 1] = values[1]
            G[i, 0] = values[2]
            G[i, 1] = values[3]
            G[i, 2] = values[4]

        out["F"] = F
        out["G"] = G

res = minimize(MyProblem(), NSGA2(pop_size=100), ('n_eval', 20000), seed=1, verbose=True)

print(res.X)
print(res.F)