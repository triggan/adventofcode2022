## Advent of Code 2022 --- Day 4: Camp Cleanup ---
#

# Part 1

inputfile = open('input.txt','r')

olatotal = 0

for line in inputfile:
    elves = line.strip().split(',')

    e1range = elves[0].split('-')
    e2range = elves[1].split('-')

    elf1 = []
    elf2 = []

    elf1.extend(range(int(e1range[0]),int(e1range[1])+1))
    elf2.extend(range(int(e2range[0]),int(e2range[1])+1))

    # Determine size of smallest set
    if len(elf1) > len(elf2):
        smallest = len(elf2)
    else:
        smallest = len(elf1)

    cross = list(set(elf1).intersection(set(elf2)))

    if len(cross) > 0:
        olatotal = olatotal + 1

inputfile.close()
print('Fully overlapping assignments: ',olatotal)