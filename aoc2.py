
data = [r.split('-') for r in open('input.txt').readline().split(',')]

invalid1 = set()
invalid2 = set()
for a, b in data:
    va = int(a)
    vb = int(b)
    for r in range(2, len(b)+1):
        n = len(b)//r
        for x in range(10**(n-1), 10**n):
            v = sum(10**(n*i)*x for i in range(r))
            if v < va:
                continue
            if v > vb:
                break
            if r == 2:
                invalid1.add(v)
            invalid2.add(v)
                
print('Part 1:', sum(invalid1))
print('Part 2:', sum(invalid2))