from scipy.optimize import minimize
import subprocess
import numpy as np

PREVIOUS_EVAL = {'x': None, 'result': None}


def run_amon(x, integer_indices):
    x_eval = x.copy()
    for i in integer_indices:
        x_eval[i] = round(x_eval[i])

    key = str(x_eval)
    if PREVIOUS_EVAL['x'] == key:
        return PREVIOUS_EVAL['result']

    with open("x1.txt", 'w') as file:
        for param in x_eval:
            file.write(f'{param} ')

    result = subprocess.run(['amon', 'run', '9', 'x1.txt', '-s', '1'],
                            capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        raise RuntimeError(result.stderr)

    lines = result.stdout.strip().split()
    parsed = [float(l) for l in lines]
    PREVIOUS_EVAL['x'] = key
    PREVIOUS_EVAL['result'] = parsed
    return parsed


def f(x_scaled, integer_indices, unscale):
    return run_amon(unscale(x_scaled), integer_indices)[0]


def constraints_fn(x_scaled, integer_indices, unscale):
    return [-g for g in run_amon(unscale(x_scaled), integer_indices)[1:]]


def make_scalers(x0, lower_bound, upper_bound):
    lower = np.array(lower_bound, dtype=float)
    upper = np.array(upper_bound, dtype=float)
    x0 = np.array(x0, dtype=float)

    ranges  = np.ones(len(x0))
    offsets = np.zeros(len(x0))

    for i in range(len(x0)):
        if np.isfinite(lower[i]) and np.isfinite(upper[i]):
            ranges[i]  = upper[i] - lower[i]
            offsets[i] = lower[i]
        else:
            # no bounds: center on x0, use |x0| as scale
            ref = max(abs(x0[i]), 1.0)
            ranges[i]  = ref
            offsets[i] = x0[i] - ref / 2.0

    def scale(x):
        return (np.array(x) - offsets) / ranges

    def unscale(x):
        return np.array(x) * ranges + offsets

    return scale, unscale


def main():
    with open('x0.txt', 'r') as file:
        x0 = [float(p) for p in file.readline().strip().split()]

    model_indices   = list(range(22, 33))
    heights_indices = list(range(33, 44))
    integer_indices = model_indices

    lower_bound = [-np.inf] * len(x0)
    upper_bound = [ np.inf] * len(x0)
    for i in model_indices:
        lower_bound[i], upper_bound[i] = 0, 5
    for i in heights_indices:
        lower_bound[i] = 0

    scale, unscale = make_scalers(x0, lower_bound, upper_bound)

    x0_scaled = scale(x0)
    bounds_scaled = [(0, 1) if (np.isfinite(lower_bound[i]) and np.isfinite(upper_bound[i]))
                     else (None, None)
                     for i in range(len(x0))]

    result = minimize(
        f,
        x0_scaled,
        method='COBYLA',
        args=(integer_indices, unscale),
        constraints={'type': 'ineq', 'fun': constraints_fn, 'args': (integer_indices, unscale)},
        bounds=bounds_scaled,
        options={
            'maxiter': 500,
            'rhobeg': 0.1,
        }
    )

    xopt = unscale(result.x)
    print("\n--- RESULT ---")
    print("x* =", xopt)
    print("f* =", result.fun)
    print("message:", result.message)


if __name__ == '__main__':
    main()