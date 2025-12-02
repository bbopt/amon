# import sys
# import matplotlib.pyplot as plt
# from matplotlib.lines import Line2D

# def main():
#     with open('x_feasible.txt', 'r') as f:
#         feasible_x = [float(x.strip()) for x in f]
#     with open('x_infeasible.txt', 'r') as f:
#         infeasible_x = [float(x.strip()) for x in f]

#     with open('obj_feasible.txt', 'r') as f:
#         feasible_objs = []
#         for line in f:
#             feasible_objs.append([float(obj.strip()) for obj in line.strip().split()])

#     with open('obj_infeasible.txt', 'r') as f:
#         infeasible_objs = []
#         for line in f:
#             infeasible_objs.append([float(obj.strip()) for obj in line.strip().split()])

#     gap = sys.maxsize
#     for i in range(len(feasible_x)):
#         curr_gap = abs(feasible_x[i] - feasible_x[i-1])
#         if curr_gap < gap:
#             gap = curr_gap
#     for i in range(len(infeasible_x)):
#         curr_gap = abs(infeasible_x[i] - infeasible_x[i-1])
#         if curr_gap < gap:
#             gap = curr_gap


#     tmp_feasible_x = []
#     tmp_feasible_objs = []
#     for i in range(len(feasible_objs) - 1):
#         if feasible_x[i+1] - feasible_x[i] >= 2*gap:
#             for point, point_objs in zip(tmp_feasible_x, tmp_feasible_objs):
#                 for obj in point_objs:
#                     plt.scatter(point, obj, color='#32CD32')
#             tmp_feasible_x = []
#             tmp_feasible_objs = []
#         else:
#             tmp_feasible_x.append(feasible_x[i])
#             tmp_feasible_objs.append(feasible_objs[i])
#     plt.scatter(
#         [p for p, objs in zip(tmp_feasible_x, tmp_feasible_objs) for _ in objs],
#         [obj for _, objs in zip(tmp_feasible_x, tmp_feasible_objs) for obj in objs],
#         color='#32CD32'
#     )
#     # for point, point_objs in zip(tmp_feasible_x, tmp_feasible_objs):
#         # for obj in point_objs:
#             # plt.scatter(point, obj, color='#32CD32')

#     tmp_infeasible_x = []
#     tmp_infeasible_objs = []
#     for i in range(len(infeasible_objs) - 1):
#         if infeasible_x[i+1] - infeasible_x[i] >= 2*gap:
#             for point, point_objs in zip(tmp_infeasible_x, tmp_infeasible_objs):
#                 for obj in point_objs:
#                     plt.scatter(point, obj, color='#FF4C4C')
#             tmp_infeasible_x = []
#             tmp_infeasible_objs = []
#         else:
#             tmp_infeasible_x.append(infeasible_x[i])
#             tmp_infeasible_objs.append(infeasible_objs[i])
#     # for point, point_objs in zip(tmp_infeasible_x, tmp_infeasible_objs):
#     #     for obj in point_objs:
#     #         plt.scatter(point, obj, color='#FF4C4C')
#     plt.scatter(
#         [p for p, objs in zip(tmp_infeasible_x, tmp_infeasible_objs) for _ in objs],
#         [obj for _, objs in zip(tmp_infeasible_x, tmp_infeasible_objs) for obj in objs],
#         color='#FF4C4C'
#     )

#     # make legend manually
#     dummy_lines = [
#         Line2D([0], [0], color='#32CD32'),
#         Line2D([0], [0], color='#FF4C4C')
#     ]
#     plt.legend(dummy_lines, ['Feasible', 'Infeasible'])

#     plt.title('Objective function when changing one turbine\'s x position')
#     plt.grid()
#     plt.xlabel('x position')
#     plt.ylabel('Objective function')
#     plt.show()
#     plt.savefig('result_x_position.png')

# if __name__ == '__main__':
#     main()

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

def main():
    # Read x values
    with open('x_feasible.txt', 'r') as f:
        feasible_x = [float(x.strip()) for x in f]
    with open('x_infeasible.txt', 'r') as f:
        infeasible_x = [float(x.strip()) for x in f]

    # Read OBJ values
    with open('obj_feasible.txt', 'r') as f:
        feasible_objs = []
        for line in f:
            feasible_objs.append([float(obj.strip()) for obj in line.strip().split()])
    with open('obj_infeasible.txt', 'r') as f:
        infeasible_objs = []
        for line in f:
            infeasible_objs.append([float(obj.strip()) for obj in line.strip().split()])

    # Plot feasible points
    plt.scatter(
        [x for x, objs in zip(feasible_x, feasible_objs) for _ in objs],
        [obj for _, objs in zip(feasible_x, feasible_objs) for obj in objs],
        color='#32CD32',
        alpha=0.4,
        s=4
    )

    # Plot feasible points
    plt.scatter(
        [x for x, objs in zip(infeasible_x, infeasible_objs) for _ in objs],
        [obj for _, objs in zip(infeasible_x, infeasible_objs) for obj in objs],
        color='#FF4C4C',
        alpha=0.4,
        s=4
    )

    # Average curves
    avg_feasible = [sum(objs) / len(objs) for objs in feasible_objs]
    plt.plot(feasible_x, avg_feasible, color='blue')

    avg_infeasible = [sum(objs) / len(objs) for objs in infeasible_objs]
    plt.plot(infeasible_x, avg_infeasible, color='blue')


    dummy_lines = [
        Line2D([0], [0], color='#32CD32'),
        Line2D([0], [0], color='#FF4C4C'),
        Line2D([0], [0], color='blue')
    ]
    plt.legend(dummy_lines, ['Feasible', 'Infeasible', 'Average (250 eval)'])
    plt.title("Objective function when changing one turbine's x position")
    plt.grid()
    plt.xlabel('x position')
    plt.ylabel('Objective function')
    plt.savefig('result_x_position.png')
    plt.show()

if __name__ == '__main__':
    main()
