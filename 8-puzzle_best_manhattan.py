from copy import deepcopy
import queue

def manhattan(current, goal):
    A = {}
    B = {}
    for i in range(len(current)):
        for j in range(len(current[i])):
            A[current[i][j]] = (i, j)
            B[goal[i][j]] = (i, j)
    s = 0
    for i in range(1, len(current)*len(current)):
        s += abs(A[i][0] - B[i][0]) + abs(A[i][1] - B[i][1])
    return s

def find_neighbours(index):
    neighbours = []
    if (index[0] - 1 >= 0):
        neighbours.append((index[0]-1,index[1]))
    if (index[0] + 1 < 3):
        neighbours.append((index[0]+1,index[1]))
    if (index[1] - 1 >= 0):
        neighbours.append((index[0],index[1]-1))
    if (index[1] + 1 < 3):
        neighbours.append((index[0],index[1]+1))
    return neighbours

def display(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print(matrix[i][j],end = ' ')
        print()
    print()

def shuffle(current,goal,none):
    global opened,closed
    closed.append(current)
    for pos in find_neighbours(none):
        temp = deepcopy(current)
        temp[pos[0]][pos[1]],temp[none[0]][none[1]] = temp[none[0]][none[1]],temp[pos[0]][pos[1]]
        hval = manhattan(temp,goal)
        if temp not in closed:
            opened.put((hval,temp,(pos[0],pos[1])))
    values = opened.get()
    return values[1],values[2],values[0]
        

current = [[2,0,3],[1,8,4],[7,6,5]]
goal = [[1,2,3],[8,0,4],[7,6,5]]
none = (0,1)
opened = queue.PriorityQueue()
opened.put((10,current))
closed = []

print("Current state :")
display(current)
print("Goal state :")
display(goal)

print("Procedure")
while not opened.empty() and current != goal :
    current,none,hval = shuffle(current,goal,none)
    print(f"Heurestic : {hval}")
    display(current)
