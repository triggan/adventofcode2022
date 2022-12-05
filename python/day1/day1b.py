## Advent of Code - Day 1: Calorie Counting

inputfile = open('input.txt','r')

def topThree(cvalue, clist):
    toReturn = clist
    for index, x in enumerate(clist):
        if cvalue > x:
            bottomlist = clist[index:]
            if len(bottomlist) > 0:
                bottomlist.pop()
            toReturn = clist[:index] + [cvalue] + bottomlist
            break
    return toReturn

csum = 0
clist = [0,0,0]
for line in inputfile:
    if line != '\n':
       csum = csum + int(line)
    else:
        clist = topThree(csum,clist)
        csum = 0

inputfile.close()
print('The largest calorie counts are: ', clist)
print('Sum of calories: ', sum(clist))