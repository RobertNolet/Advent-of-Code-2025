data = [[int(x) for x in line.strip()] for line in open('input.txt')]

scores = {1:0, 2:0}
for line in data:
    for part, l in [(1, 2), (2, 12)]:
        value = 0
        i = -1
        for digit in range(l):
            n = max(line[i+1:len(line)-(l-1-digit)])
            i += 1 + line[i+1:len(line)-(l-1-digit)].index(n)
            value = 10*value + n
        scores[part] += value

print('Part 1:', scores[1])
print('Part 2:', scores[2])