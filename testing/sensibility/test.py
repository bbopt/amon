import numpy as np
import subprocess

def main():
    set_radius = 10
    points = []
    points += [(14850, -5804), (15617, -4860), (15926, -5731), (14977, -4538), (14251, -5472), (13737, -4935)]
    balls = []
    for point in points:
        balls.append(Boule(set_radius, point[0], point[1]))
    results = []
    for i in range(300):
        print(f"Iteration {i+1} of 300")
        current_point = []
        for ball in balls:
            random_point = ball.getRandomPoint()
            current_point.append(random_point[0])
            current_point.append(random_point[1])
        rest_of_point = [float(item) for item in '0 0 0 0 0 0 170 170 170 170 170 170 0 0 0 0 0 0'.split()]
        current_point += rest_of_point
        with open('x3.txt', 'w') as f:
            for elem in current_point:
                f.write(str(elem) + ' ')
        results.append(float(subprocess.run(['amon', 'run', '3', 'x3.txt', '-r', '--port', '8989'], capture_output=True, text=True).stdout.strip().split()[0]))

    with open("results.txt", 'w') as file:
        for result in results:
            file.write(f"{result}\n")
        
    

class Boule:
    def __init__(self, rayon, center_x, center_y):
        self.rayon_ = rayon
        self.center_x_ = center_x
        self.center_y_ = center_y
    def getRandomPoint(self):
        phase = np.random.uniform(0, 2 * np.pi)
        norme = np.random.uniform(0, self.rayon_)
        point_x = norme * np.cos(phase)
        point_y = norme * np.sin(phase)
        return (point_x, point_y)

if __name__ == "__main__":
    main()