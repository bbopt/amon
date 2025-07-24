import subprocess


def main():
    for var_index in range(30):


def changeVariable(index, value, point_file):
    with open(point_file, 'r') as source_file:
        point = source_file.readline().strip().split()
    try:
        point[index] = value
    except IndexError as e:
        print(f'No index {index}: {e}')
    with open('x0.txt', 'w') as target_file:
        for var in point:
            target_file.write(f'{var} ')

