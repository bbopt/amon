import matplotlib.pyplot as plt

def main():
    with open('results.txt', 'r') as file:
        fidelities = [float(fidelity) for fidelity in file.readline().strip().split()]
        time = [float(time) for time in file.readline().strip().split()]
    plt.plot(fidelities, time)
    plt.title('Effect of fidelity on execution time')
    plt.grid()
    plt.xlabel('Fidelity')
    plt.ylabel('Execution time [s]')
    plt.show()

if __name__ == '__main__':
    main()