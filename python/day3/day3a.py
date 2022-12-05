## Advent of Code 2022 --- Day 3: Rucksack Reorganization ---

## Part 1

# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.

# Offsets from ASCII values of letters to the priority values above.
LOWERADIFF = 96
UPPERADIFF = 38

inputfile = open('input.txt','r')

totalpri = 0

for line in inputfile:
    firstcomp = line[len(line.strip())//2:]
    secondcomp = line[:len(line.strip())//2]

    # use sets for intersection; returns a set with single value; use pop to get value
    commonitem = set(firstcomp).intersection(set(secondcomp)).pop()
    
    if commonitem.isupper():
        totalpri = totalpri + ( ord(commonitem) - UPPERADIFF )
    else:
        totalpri = totalpri + ( ord(commonitem) - LOWERADIFF )

inputfile.close()
print('Total of priorities is: ', totalpri)