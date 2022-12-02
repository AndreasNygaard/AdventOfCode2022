### Puzzle 1 ###
games = [tuple(game.split(' ')) for game in open('input.txt', 'r').read().strip().split('\n')]
outcome_dict = {'A':1,'B':2,'C':3,'X':1,'Y':2,'Z':3}
print(sum([((outcome_dict[you] - outcome_dict[elf])%3 + 1)%3 * 3 + outcome_dict[you] for elf, you in games]))

### Puzzle 2 ###
print(sum([((outcome_dict[elf]+(outcome_dict[win]-2))%3 + 2)%3 + 1 + (outcome_dict[win]-1)*3 for elf, win in games]))
