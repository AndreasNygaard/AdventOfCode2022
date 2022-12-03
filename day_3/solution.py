### Puzzle 1 ###
lines = open('input.txt','r').read().strip().split('\n')
items = [list(set(line[:int(len(line)/2)]).intersection(line[int(len(line)/2):]))[0] for line in lines]
print(sum([(ord(item)-96)%58 for item in items]))

### Puzzle 2 ###
groups = [lines[3*i:3*i+3] for i in range(int(len(lines)/3))]
common_chars = [list(set(group[0]).intersection(group[1]).intersection(group[2]))[0] for group in groups]
print(sum([(ord(char)-96)%58 for char in common_chars]))
