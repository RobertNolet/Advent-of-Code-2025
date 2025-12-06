import numpy as np

with open('input.txt') as file:
    lines = file.read().split('\n')

numbers = np.array([[int(x) for x in line.split()] for line in lines[:-1]])
ops = [np.sum if c == '+' else np.prod for c in lines[-1].split()]
n = len(ops)

print('Part 1:', sum(ops[i](numbers[:,i]) for i in range(n)))

result = 0
data = np.array([list(line) for line in lines[:-1]])
i = 0
for op in ops:
    values = []
    while i < data.shape[1] and np.any(data[:,i] != ' '):
        values.append(int(''.join(data[:,i]))) 
        i += 1
    i += 1
    result += op(values, dtype=int)
print('Part 2:', result)