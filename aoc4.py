dirs = {(dx,dy) for dx in [-1,0,1] for dy in [-1,0,1]} - {(0,0)}
data = [list(line.strip()) for line in open('input.txt')]

n = len(data)
m = len(data[0])

def valid(x,y):
    return (0 <= x < m) and (0 <= y < n)

def canremove(data, x, y):
    return sum(data[y+dy][x+dx] == '@' for (dx,dy) in dirs if valid(x+dx,y+dy)) < 4

nremove = []

done = False
while not done:
    rolls = [(x, y) for x in range(m) for y in range(n) if data[y][x] == '@' and canremove(data, x, y)]
    nremove.append(len(rolls))
    for (x,y) in rolls:
        data[y][x] = '.'
    done = len(rolls) == 0

print('Part 1', nremove[0])
print('Part 2:', sum(nremove))