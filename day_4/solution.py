### Puzzle 1 ###
ranges = [list(map(lambda x: int(x), line.replace('-',',').split(','))) for line in open('input.txt','r').read().strip().split('\n')]
print(sum([1 if (r[0] >= r[2] and r[1] <= r[3]) or (r[0] <= r[2] and r[1] >= r[3]) else 0 for r in ranges]))

### Puzzle 2 ###
print(sum([1 if r[0] <= r[3] and r[1] >= r[2] else 0 for r in ranges]))
