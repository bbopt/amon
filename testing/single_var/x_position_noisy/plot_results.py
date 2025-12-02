import sys
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

def main():
    with open('results_feasible.txt', 'r') as f:
        feasible_x = [float(x) for x in f.readline().strip().split()]
        feasible_objs = [float(obj) for obj in f.readline().strip().split()]
    with open('results_infeasible.txt', 'r') as f:
        infeasible_x = [float(x) for x in f.readline().strip().split()]
        infeasible_objs = [float(obj) for obj in f.readline().strip().split()]

    gap = sys.maxsize
    for i in range(len(feasible_x)):
        curr_gap = abs(feasible_x[i] - feasible_x[i-1])
        if curr_gap < gap:
            gap = curr_gap
    for i in range(len(infeasible_x)):
        curr_gap = abs(infeasible_x[i] - infeasible_x[i-1])
        if curr_gap < gap:
            gap = curr_gap


    tmp_feasible_x = []
    tmp_feasible_objs = []
    for i in range(len(feasible_objs) - 1):
        if feasible_x[i+1] - feasible_x[i] >= 2*gap:
            plt.plot(tmp_feasible_x, tmp_feasible_objs, color='#32CD32')
            tmp_feasible_x = []
            tmp_feasible_objs = []
        else:
            tmp_feasible_x.append(feasible_x[i])
            tmp_feasible_objs.append(feasible_objs[i])
    plt.plot(tmp_feasible_x, tmp_feasible_objs, color='#32CD32')

    tmp_infeasible_x = []
    tmp_infeasible_objs = []
    for i in range(len(infeasible_objs) - 1):
        if infeasible_x[i+1] - infeasible_x[i] >= 2*gap:
            plt.plot(tmp_infeasible_x, tmp_infeasible_objs, color='#FF4C4C')
            tmp_infeasible_x = []
            tmp_infeasible_objs = []
        else:
            tmp_infeasible_x.append(infeasible_x[i])
            tmp_infeasible_objs.append(infeasible_objs[i])
    plt.plot(tmp_infeasible_x, tmp_infeasible_objs, color='#FF4C4C')

    # make legend manually
    dummy_lines = [
        Line2D([0], [0], color='#32CD32'),
        Line2D([0], [0], color='#FF4C4C')
    ]
    plt.legend(dummy_lines, ['Feasible', 'Infeasible'])

    plt.title('Objective function when changing one turbine\'s x position')
    plt.grid()
    plt.xlabel('x position')
    plt.ylabel('Objective function')
    plt.show()
    plt.savefig('result_x_position.png')

if __name__ == '__main__':
    main()