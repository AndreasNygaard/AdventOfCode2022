### Puzzle 1 ###
lines = open('input.txt','r').read()
cal = [eval(group.replace('\n','+')) for group in lines[:-2].split('\n\n')]
print(max(cal))
### Puzzle 2 ###
print(sum(sorted(cal)[-3:]))
