import matplotlib.pyplot as plt

def main():
    evaluations = range(1, 1001)

    results = []
    with open('results.txt', 'r') as f:
        for elem in f.readline().strip().split():
            results.append(float(elem.strip()))

    averages = []
    sum = 0
    for i, result in enumerate(results):
        sum += result
        avg = (sum)/(i+1)
        averages.append(avg)

    plt.scatter(evaluations, results, label='Objective')
    plt.plot(evaluations, averages, label='Average', color='red')
    plt.grid(True)
    plt.title('Repeated evaluations of a single point')
    plt.xlabel('Evaluation')
    plt.ylabel('Objective function')
    plt.savefig('hello.png')

if __name__ == '__main__':
    main()


