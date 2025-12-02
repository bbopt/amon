import matplotlib.pyplot as plt

def main():
    with open('results.txt', 'r') as file:
        fidelities = [float(fidelity) for fidelity in file.readline().strip().split()]
        time = [float(time) for time in file.readline().strip().split()]
    plt.bar(fidelities, time)
    for i, t in enumerate(time):
        plt.text(fidelities[i], t + 0.05, str(t), ha='center', va='bottom', fontsize=10)
    plt.title('Effect of fidelity on the execution time of instance 4\n(with server)')
    plt.grid(axis='y', linestyle='--', alpha=0.3)
    plt.xlabel('Fidelity')
    plt.ylabel('Average execution time [s]')
    plt.ylim([0, 4.2])
    plt.show()

if __name__ == '__main__':
    main()
