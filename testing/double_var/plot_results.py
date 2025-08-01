import csv
import numpy as np
import matplotlib.pyplot as plt

def main():
    results = []
    with open("results.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            x = float(row["x"].strip())
            y = float(row["y"].strip())
            obj = float(row["obj"].strip())
            is_feasible = row["is_feasible"].strip() == "True"
            results.append((x, y, obj if is_feasible else np.nan))

    xs = sorted(set(r[0] for r in results))
    ys = sorted(set(r[1] for r in results))

    x_to_idx = {val: idx for idx, val in enumerate(xs)}
    y_to_idx = {val: idx for idx, val in enumerate(ys)}

    matrix = np.full((len(ys), len(xs)), np.nan)
    for x, y, val in results:
        i = y_to_idx[y]
        j = x_to_idx[x]
        matrix[i, j] = val

    plt.imshow(matrix, cmap="viridis", origin="lower",
            extent=[min(xs), max(xs), min(ys), max(ys)],
            aspect="auto")
    plt.colorbar(label="Objective Value")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Feasible Objective Heatmap")
    plt.show()

if __name__ == '__main__':
    main()
