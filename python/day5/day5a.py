## Advent of Code 2022 --- Day 5: Supply Stacks ---
#

#             [M] [S] [S]            
#         [M] [N] [L] [T] [Q]        
# [G]     [P] [C] [F] [G] [T]        
# [B]     [J] [D] [P] [V] [F] [F]    
# [D]     [D] [G] [C] [Z] [H] [B] [G]
# [C] [G] [Q] [L] [N] [D] [M] [D] [Q]
# [P] [V] [S] [S] [B] [B] [Z] [M] [C]
# [R] [H] [N] [P] [J] [Q] [B] [C] [F]
#  1   2   3   4   5   6   7   8   9 

stacks = [[]]*10
stacks[1] = ['R','P','C','D','B','G']
stacks[2] = ['H','V','G']
stacks[3] = ['N','S','Q','D','J','P','M']
stacks[4] = ['P','S','L','G','D','C','N','M']
stacks[5] = ['J','B','N','C','P','F','L','S']
stacks[6] = ['Q','B','D','Z','V','G','T','S']
stacks[7] = ['B','Z','M','H','F','T','Q']
stacks[8] = ['C','M','D','B','F']
stacks[9] = ['F','C','Q','G']

inputfile = open('input.txt','r')

def moveStack(src,dst,allstacks):

    obj2move = allstacks[src].pop()
    allstacks[dst].append(obj2move)

while True:

    line = inputfile.readline()

    if not line:
        break

    if 'move' in line:

        moves = line.strip().split(' ')

        for x in range(int(moves[1])):
            moveStack(int(moves[3]),int(moves[5]),stacks)

result = ''
for stack in stacks:

    if len(stack) > 0:
        result = result + stack.pop()

inputfile.close()
print(result)
