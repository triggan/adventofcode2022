## Advent of Code 2022 --- Day 7: No Space Left On Device ---
#

# class Node:
#     def __init__(self, type, name, size=0):
#         self.parent = None
#         self.child = []
#         self.type = type
#         self.name = name
#         self.size = size

#     def getParent(self):
#         return self.parent

#     def createChild(self, type, name):
#         newChild = Node(type, name)
#         self.child.append(newChild)
#         return newChild

#     def getSize(self):
#         if self.type == 'directory':
#             return 0
#         else:
#             total = 0
#             for c in self.child:
#                 total = total + c.getSize()
#             return self.size + total

TOTALDISKCAP = 70000000
DISKCAPNEEDED = 30000000

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

# Get total capacity used
targetCapacityToReclaim = DISKCAPNEEDED- (TOTALDISKCAP - getDirSize('/'))
print(targetCapacityToReclaim)

# remove items below the threshold of targetCapacityToReclaim
filteredList = list(filter(lambda x: x[1] >= targetCapacityToReclaim, dirSizes))
sortedList = sorted(filteredList, key=lambda x: x[1], reverse=False)

print('Size of largest dir without exceeding threshold: ',sortedList[0])

inputfile.close()