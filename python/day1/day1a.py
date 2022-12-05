## Advent of Code - Day 1: Calorie Counting

inputfile = open('input.txt','r')

csum = 0
biggest = 0
for line in inputfile:
    if line != '\n':
       csum = csum + int(line)
    else:
        if csum > biggest:
            biggest = csum
        csum = 0

inputfile.close()
print('The largest calorie count is: ', biggest)