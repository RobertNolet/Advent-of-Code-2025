
with open('input.txt') as file:
    data1, data2 = file.read().split('\n\n')

ranges = {tuple(map(int, line.split('-'))) for line in data1.split('\n')}
items = set(map(int, data2.split('\n')))

print('Part 1:', sum(any((a <= x <= b) for a, b in ranges) for x in items))

def overlap(a1, b1, a2, b2):
    return max(b1,b2) - min(a1,a2) < (b1-a1) + (b2-a2) + 1

newranges = set()
for r1 in ranges:
    overlaps = {r2 for r2 in newranges if overlap(*r1, *r2)}
    if overlaps:
        newranges -= overlaps
        a = min(a for a, b in overlaps | {r1})
        b = max(b for a, b in overlaps | {r1})
        newranges.add((a,b))
    else:
        newranges.add(r1)

print('Part 2:', sum((b-a+1) for (a,b) in newranges))