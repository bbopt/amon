import subprocess


class Point:
    def __init__(self, index):
        self.index = index
    

# Results are stored as a list of integers, each corresponding to a point,
# The order of these integers represents which points have better objective function values for a specific fidelity
class Result:
    def __init__(self, fidelity, points):
        self.fidelity = fidelity
        self.points   = points # list of integers ([2, 8, 10, 25, ...])

        
    
    def getRank(self, target): # Here, the point is a value of the list, not an index
        for index, point in enumerate(self.points):
            if point == target:
                return index
        raise ValueError(f"Point {target} not in result's points: {self.points}")


    def distance(self, other_result):
        for point in range(len(self.points)):
            this_point_rank = 
