## Advent of Code 2022 --- Day 6: Tuning Trouble ---
#
from collections import deque

inputfile = open('input.txt','r')

for line in inputfile:
    queue = deque()
    uvalues = set() # maintain a set of unique values in the queue
                    # if uvalues == 4, then we have our preamble
    counter = 1
    for letter in line:
        if len(queue) < 4:
            queue.append(letter)
            uvalues.add(letter)
        else:
            toremove = queue.popleft()
            if toremove not in queue:
                uvalues.remove(toremove)
            queue.append(letter)
            uvalues.add(letter)
            if len(uvalues) == 4:
                break
        print('queue: ',queue,' uvalues: ',uvalues)
        counter = counter + 1
    print(uvalues,' ',counter)
                
inputfile.close()