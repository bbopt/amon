import sys
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

def main():
    with open('results_feasible.txt', 'r') as f:
        feasible_yaw = [float(y) for y in f.readline().strip().split()]
        feasible_objs = [float(obj) for obj in f.readline().strip().split()]
    with open('results_infeasible.txt', 'r') as f:
        infeasible_yaw = [float(y) for y in f.readline().strip().split()]
        infeasible_objs = [float(obj) for obj in f.readline().strip().split()]

    gap = sys.maxsize
    for i in range(len(feasible_yaw)):
        curr_gap = abs(feasible_yaw[i] - feasible_yaw[i-1])
        if curr_gap < gap:
            gap = curr_gap
    for i in range(len(infeasible_yaw)):
        curr_gap = abs(infeasible_yaw[i] - infeasible_yaw[i-1])
        if curr_gap < gap:
            gap = curr_gap


    tmp_feasible_yaw = []
    tmp_feasible_objs = []
    for i in range(len(feasible_objs) - 1):
        if feasible_yaw[i+1] - feasible_yaw[i] >= 2*gap:
            plt.plot(tmp_feasible_yaw, tmp_feasible_objs, color='#32CD32')
            tmp_feasible_yaw = []
            tmp_feasible_objs = []
        else:
            tmp_feasible_yaw.append(feasible_yaw[i])
            tmp_feasible_objs.append(feasible_objs[i])
    plt.plot(tmp_feasible_yaw, tmp_feasible_objs, color='#32CD32')

    tmp_infeasible_yaw = []
    tmp_infeasible_objs = []
    for i in range(len(infeasible_objs) - 1):
        if infeasible_yaw[i+1] - infeasible_yaw[i] >= 2*gap:
            plt.plot(tmp_infeasible_yaw, tmp_infeasible_objs, color='#FF4C4C')
            tmp_infeasible_yaw = []
            tmp_infeasible_objs = []
        else:
            tmp_infeasible_yaw.append(infeasible_yaw[i])
            tmp_infeasible_objs.append(infeasible_objs[i])
    plt.plot(tmp_infeasible_yaw, tmp_infeasible_objs, color='#FF4C4C')

    # make legend manually
    dummy_lines = [
        Line2D([0], [0], color='#32CD32'),
        Line2D([0], [0], color='#FF4C4C')
    ]
    plt.legend(dummy_lines, ['Feasible', 'Unfeasible'])

    plt.title('Objective function when changing one turbine\'s relative yaw angle')
    plt.grid()
    plt.xlabel('yaw angle')
    plt.ylabel('Objective function')
    plt.show()
    plt.savefig('result_yaw.png')

if __name__ == '__main__':
    main()