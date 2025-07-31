import subprocess

for fidelity in range(6):
    print(f'Fidelity = {fidelity}')
    print('---------------')
    results = {}
    for i in range(100):
        print(f'{i+1}th iteration')
        results[i] = float(subprocess.run(['amon', 'run', 'params.txt', f'x{i}.txt', '-s', '1', '-f', f'{fidelity}'], capture_output=True, text=True).stdout.strip().split()[0])
    results = dict(sorted(results.items(), key=lambda item: item[1]))
    print('Writing...')
    with open("order.txt", 'a') as f:
        f.write(f'\nFidelity = {fidelity:.2f}\n')
        f.write('---------------\n')
        for point, obj in results.items():
            f.write(f'Point {point:2} : obj = {obj}\n')
    with open("quick_comparison.txt", 'a') as f:
        f.write(f'Fidelity = {fidelity:1.2f}: [ ')
        for point in results:
            f.write(f'{point:2} ')
        f.write(']\n')
