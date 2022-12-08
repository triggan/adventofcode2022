## Advent of Code 2022 --- Day 7: No Space Left On Device ---
#

nodes = {} 
currentNode = None
dirSizes = []

inputfile = open('input.txt','r')

def createNode(nodetype,size=0,parent=None):
    newnode = {}
    newnode['type'] = nodetype
    newnode['size'] = size
    newnode['children'] = []
    newnode['parent'] = parent
    return newnode

def getDirSize(startNode):
    total = 0
    for child in nodes[startNode]['children']:
        total = total + getDirSize(child)
    return nodes[startNode]['size'] + total

# Create a list of nodes, with each having a parent and list of children
for line in inputfile:
    commands = line.strip().split(' ')
    if commands[0] == '$':
        # handle cd
        if commands[1] == 'cd':

            if commands[2] == '/':
                nodes[commands[2]] = createNode('directory')
                currentNode = commands[2]

            elif commands[2] == '..':
                currentNode = nodes[currentNode]['parent']

            else:
                currentNode = currentNode + commands[2]

        elif commands[1] == 'ls':
            continue

    elif commands[0] == 'dir':
        nodes[currentNode]['children'].append(currentNode + commands[1])
        if commands[1] in nodes:
            raise Exception('Found duplicate file/dir name.')
        nodes[currentNode + commands[1]] = createNode('directory',parent=currentNode)

    else:  #only thing that remains are files
        nodes[currentNode]['children'].append(currentNode + commands[1])
        if commands[1] in nodes:
            raise Exception('Found duplicate file/dir name.')
        nodes[currentNode + commands[1]] = createNode('file',int(commands[0]),currentNode)

# Traverse the nodes and total up the size of files beneath each node
for path in nodes:
    if nodes[path]['type'] == 'directory':
        dirSizes.append([path,getDirSize(path)])

# remove items below the threshold of 100,000
filteredList = list(filter(lambda x: x[1] <= 100000, dirSizes))

total = 0
for item in filteredList:
    total = total + item[1]

print(filteredList)
print(total)

inputfile.close()