## Advent of Code 2022 --- Day 3: Rucksack Reorganization ---

## Part 2

# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.

# Offsets from ASCII values of letters to the priority values above.
LOWERADIFF = 96
UPPERADIFF = 38

inputfile = open('input.txt','r')

totalpri = 0

while True:

    pack1 = inputfile.readline().strip()
    pack2 = inputfile.readline().strip()
    pack3 = inputfile.readline().strip()

    if (pack1 == '') or (pack2 == '')  or (pack3 == ''):
        break

    # use sets for intersection; returns a set with single value; use pop to get value
    commonitem = set(pack1).intersection(set(pack2)).intersection(set(pack3)).pop()
    
    if commonitem.isupper():
        totalpri = totalpri + ( ord(commonitem) - UPPERADIFF )
    else:
        totalpri = totalpri + ( ord(commonitem) - LOWERADIFF )

inputfile.close()
print('Total of priorities is: ', totalpri)