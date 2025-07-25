import sys
import numpy as np
import matplotlib.pyplot as plt


class Result:
    def __init__(self, fidelity, points):
        self.fidelity = fidelity
        self.points   = points

    def getRank(self, target):
        for index, point in enumerate(self.points):
            if point == target:
                return index
        raise ValueError(f'Point {target} not in {self.points} for fidelity = {self.fidelity}')

    def getHierarchy(self, target): # Returns list of bools. Ex: [True, True, False] means the provided point is better or equal to point 1 and 2, but worse than 3. 3 Is not the index, it is the actual point.
        hierarchy = [None] * len(self.points)
        rank = self.getRank(target)
        for i, point in enumerate(self.points):
            if i < rank:
                hierarchy[point] = False
            else:
                hierarchy[point] = True
        return hierarchy

    def getDistance(self, other_result):
        distance = 0
        for i in range(len(self.points)):
            this_hierarchy  = self.getHierarchy(i)
            other_hierarchy = other_result.getHierarchy(i)
            for j in range(len(this_hierarchy)):
                if this_hierarchy[j] is None or other_hierarchy[j] is None:
                    raise ValueError("Results not fully filled")
                if this_hierarchy[j] != other_hierarchy[j]:
                    distance += 1
        distance *= 0.5
        return distance


def main():
    results = []
    with open('quick_comparison.txt', 'r') as file:
        for line in file:
            fidelity, points = line.split(':')
            fidelity = float(fidelity.split('=')[1].strip())
            points = [int(x) for x in points.strip('[] \n').split()]

            results.append(Result(fidelity, points))

    for result in results:
        if result.fidelity == 1:
            truth = result
    results.append(Result(-1, truth.points[::-1]))
    
    distances = {}
    for result in results:
        distances[result.fidelity] = truth.getDistance(result)
    print('Fid  : dist')
    print('-----------')
    for fid, dist in distances.items():
        print(f'{fid:.2f} :  {int(dist)}')
    
    worst = distances[-1]
    similarity = {}
    for fid, distance in distances.items():
        similarity[fid] = 1 - distance / worst

    x, y = zip(*similarity.items())
    print(x)
    print(y)
    plt.step(x[:-1], y[:-1], where='post')
    plt.title('Similarity in order of feasible points with fidelity')
    plt.grid()
    plt.xlabel('Fidelity')
    plt.xticks(np.arange(0, 1.05, 0.05))
    plt.ylabel('Similarity')
    plt.show()


def test():
    result_1 = Result(1, [0, 1, 2])
    result_2 = Result(0.5, [0, 2, 1]) # Distance should be 1
    result_3 = Result(0.9, [2, 0, 1]) # Distance should be 2
    result_4 = Result(0.7, [2, 1, 0]) # Distance should be 3

    print(result_1.getDistance(result_1))
    print(result_1.getDistance(result_2))
    print(result_1.getDistance(result_3))
    print(result_1.getDistance(result_4))

if __name__ == '__main__':
    if sys.argv[1] == 'test':
        test()
    elif sys.argv[1] == 'main':
        main()