## Advent of Code 2022 --- Day 6: Tuning Trouble ---
#
from collections import deque

inputfile = open('testinput.txt','r')

for line in inputfile:
    queue = deque()
    uvalues = set() # maintain a set of unique values in the queue
                    # if uvalues == 4, then we have our preamble
    for letter in line:
        if len(queue) < 4:
            queue.append(letter)
            uvalues.add(letter)
        else:
            uvalues.remove(queue.popleft())
            queue.append(letter)
            uvalues.add(letter)
            if len(uvalues) == 4:
                break
    print(uvalues)
                
inputfile.close()