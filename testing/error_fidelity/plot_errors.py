import matplotlib.pyplot as plt

def main():
    with open('results.txt', 'r') as file:
        fidelities = [float(fidelity) for fidelity in file.readline().strip().split(':')[1].split()]
        differences = [float(difference) * 100 for difference in file.readline().strip().split(':')[1].split()]

    plt.bar(fidelities, differences)
    plt.title('Error with increasing fidelity')
    plt.grid(axis='y', linestyle='--', alpha=0.3)
    plt.xlabel('Fidelity')
    plt.ylabel('Error [%]')
    plt.show()



if __name__ == '__main__':
    main()

