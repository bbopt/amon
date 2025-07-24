import matplotlib.pyplot as plt

def main():
    with open('results.txt', 'r') as file:
        fidelities = [float(fidelity) for fidelity in file.readline().strip().split(':')[1].split()]
        objectives = [float(objective) for objective in file.readline().strip().split(':')[1].split()]

    truth = objectives[-1]
    errors = []
    for objective in objectives:
        errors.append(abs(truth - objective)/truth)

    plt.plot(fidelities, errors)
    plt.title('Error with increasing fidelity')
    plt.grid()
    plt.xlabel('Fidelity')
    plt.ylabel('Error [%]')
    plt.show()



if __name__ == '__main__':
    main()

