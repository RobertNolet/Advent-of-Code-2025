from collections import defaultdict

with open('input.txt') as file:
    data = file.read().split('\n')

beams = {data[0].index('S'): 1}

splits = 0
for line in data[1:]:
    newbeams = defaultdict(int)
    for beam, count in beams.items():
        if line[beam] == '.':
            newbeams[beam] += count
        elif line[beam] == '^':
            splits += 1
            newbeams[beam-1] += count
            newbeams[beam+1] += count
        else:
            print('Unexpected symbol!')
    beams = newbeams

print('Part 1:', splits)
print('Part 2:', sum(beams.values()))