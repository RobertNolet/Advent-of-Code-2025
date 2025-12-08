from itertools import combinations
from collections import defaultdict
from math import prod

data = [tuple(map(int, line.split(','))) for line in open('input.txt')]
n = len(data)

def sqdist(p):
    return sum((x-y)**2 for x,y in zip(data[p[0]], data[p[1]]))

connections = sorted(combinations(range(n),2), key = sqdist)

# circuits[i] is the circuit that point i belongs to
# initially each point belongs to it's own circuit
circuits = {i:i for i in range(n)}

count = 0
m = 0
for i, j in connections:
    m += 1
    if circuits[i] != circuits[j]:
        # Merge circuits
        count += 1
        # Set the circuit of all point in circuit j
        # to circuit i, circuit j will cease to exist
        merge = (circuits[i], circuits[j])
        for k in circuits:
            if circuits[k] in merge:
                circuits[k] = min(merge)

    if m == 1000:
        counts = defaultdict(int)
        for i in circuits.values():
            counts[i] += 1
        print('Part 1:', prod(sorted(counts.values(), reverse=True)[:3]))
    if count == 999:
        print('Part 2:', data[i][0]*data[j][0])
        break