

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



def test():
    result_1 = Result(1, [0, 1, 2])
    result_2 = Result(0.5, [0, 2, 1]) # Difference should be 1
    result_3 = Result(0.9, [2, 0, 1]) # Difference should be 2
    result_4 = Result(0.7, [2, 1, 0]) # Difference should be 3

    print(result_1.getDistance(result_1))
    print(result_1.getDistance(result_2))
    print(result_1.getDistance(result_3))
    print(result_1.getDistance(result_4))