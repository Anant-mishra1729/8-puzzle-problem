from copy import deepcopy

def manhattan(current, goal):
    # A will contain coordinates of current state
    # B will contain coordinates of goal state
    A = {}
    B = {}
    for i in range(len(current)):
        for j in range(len(current[i])):
            A[current[i][j]] = (i, j)
            B[goal[i][j]] = (i, j)

    # Calculating manhattan distance
    s = 0
    for i in range(1, len(current)*len(current)):
        s += abs(A[i][0] - B[i][0]) + abs(A[i][1] - B[i][1])
    return s

# For finding coordinates of points with which blank can be swapped
def find_neighbours(index):
    neighbours = []
    if (index[0] - 1 >= 0):
        neighbours.append((index[0]-1, index[1]))
    if (index[0] + 1 < 3):
        neighbours.append((index[0]+1, index[1]))
    if (index[1] - 1 >= 0):
        neighbours.append((index[0], index[1]-1))
    if (index[1] + 1 < 3):
        neighbours.append((index[0], index[1]+1))
    return neighbours


def display(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print(matrix[i][j], end=' ')
        print()
    print()

# Generating different states of board


def shuffle(current, goal, none):
    min_hval = 10
    for pos in find_neighbours(none):
        # Deepcopy is used as by doing temp = current any change in temp will also reflect in current
        temp = deepcopy(current)

        # Swapping with coordinates
        temp[pos[0]][pos[1]], temp[none[0]][none[1]] = temp[none[0]][none[1]], temp[pos[0]][pos[1]]

        # Calculating manhattan distance
        hval = manhattan(temp, goal)
        if hval < min_hval:
            min_hval = hval
            beststate = temp
            new_none = (pos[0], pos[1])
    return beststate, new_none, min_hval


current = [ [ 1, 2, 3 ],
            [ 5, 6, 0 ],
            [ 7, 8, 4 ] ]
goal = [ [ 1, 2, 3 ],
          [ 5, 8, 6 ],
          [ 0, 7, 4 ] ]
none = (1, 2)

print("Current state :")
display(current)
print("Goal state :")
display(goal)

print("Procedure")
while(current != goal):
    current, none, hval = shuffle(current, goal, none)
    print(f"Heurestic : {hval}")
    display(current)
