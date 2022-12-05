## Advent of Code 2022 -- Day 2: Rock Paper Scissors --
##
## Part 1

##
# player1 = A for Rock, B for Paper, and C for Scissors
# player2 = X for Rock, Y for Paper, and Z for Scissors
#
# The score for a single round is the score for the shape you selected 
# (1 for Rock, 2 for Paper, and 3 for Scissors) 
# plus the score for the outcome of the round 
# (0 if you lost, 3 if the round was a draw, and 6 if you won).

## Define Win/Loss Matrix
winloss = {
    'A': {
        'X': 4,
        'Y': 8,
        'Z': 3
    },
    'B': {
        'X': 1,
        'Y': 5,
        'Z': 9
    },
    'C': {
        'X': 7,
        'Y': 2,
        'Z': 6
    }
}

inputfile = open('input.txt','r')

score = 0
for line in inputfile:
    plays = line.strip().split(' ')
    score = score + winloss[plays[0]][plays[1]]

print('Your total score is: ',score)