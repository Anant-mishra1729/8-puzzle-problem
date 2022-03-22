from copy import deepcopy

def find_heurestic(current,goal):
    hval = 0
    for i in range(len(current)):
        for j in range(len(current)):
            if current[i][j]!= 0 and current[i][j] != goal[i][j]:
                hval += 1
    return hval

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
    min_hval = 10
    for pos in find_neighbours(none):
        temp = deepcopy(current)
        temp[pos[0]][pos[1]],temp[none[0]][none[1]] = temp[none[0]][none[1]],temp[pos[0]][pos[1]]
        hval = find_heurestic(temp,goal)
        if hval < min_hval: 
            min_hval = hval
            beststate = temp
            new_none = (pos[0],pos[1])
    return beststate,new_none,min_hval

current = [[2,0,3],[1,8,4],[7,6,5]]
goal = [[1,2,3],[8,0,4],[7,6,5]]
none = (0,1)

print("Current state :")
display(current)
print("Goal state :")
display(goal)

print("Procedure")
while(current != goal):
    current,none,hval = shuffle(current,goal,none)
    print(f"Heurestic : {hval}")
    display(current)
