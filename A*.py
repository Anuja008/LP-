# A* Algorithm for 8 Puzzle Problem

# Enter Goal State
print("Enter Goal State:")

goal = []   # empty list to store goal puzzle

for i in range(3):

    row = input().split()
    # take one row input and split values

    goal.append(row)
    # add row into goal state


# Heuristic Function
def h(state):

    count = 0
    # count stores number of misplaced tiles

    for i in range(3):
        for j in range(3):

            # check if tile is misplaced and not blank
            if state[i][j] != goal[i][j] and state[i][j] != '_':

                count += 1
                # increase count if tile is misplaced

    return count
    # return heuristic value


# Display Puzzle Function
def display(state):

    for row in state:

        print(" ".join(row))
        # print each row properly

    print()
    # blank line for formatting


# Generate Child States
def generate(state):

    # find blank space position
    for i in range(3):
        for j in range(3):

            if state[i][j] == '_':

                x, y = i, j
                # store blank tile position

    # possible moves
    moves = [[0,1],[0,-1],[1,0],[-1,0]]
    # right, left, down, up

    children = []
    # list to store child states

    for dx, dy in moves:

        nx = x + dx
        ny = y + dy
        # calculate new position

        # check boundaries
        if nx >= 0 and nx < 3 and ny >= 0 and ny < 3:

            # create copy of current state
            temp = [row[:] for row in state]

            # swap blank with adjacent tile
            temp[x][y], temp[nx][ny] = temp[nx][ny], temp[x][y]

            children.append(temp)
            # add new state into children list

    return children
    # return all child states


# Enter Initial State
print("Enter Initial State:")

start = []   # empty list for initial state

for i in range(3):

    row = input().split()
    # take row input

    start.append(row)
    # add row into start state


# Open List
open_list = [start]
# stores states to be explored

# Visited List
visited = []
# stores already visited states


# Main Loop
while open_list:

    # remove first state
    current = open_list.pop(0)

    print("Current State:")
    display(current)
    # display current puzzle

    # Goal Check
    if h(current) == 0:

        print("Goal State Reached")
        break
        # stop if goal reached

    visited.append(current)
    # add current state into visited list

    # generate child states
    children = generate(current)

    # sort children using heuristic value
    children.sort(key=h)

    # add child states into open list
    for child in children:

        if child not in visited:

            open_list.append(child)
            # add unexplored child

-----------------------------------

What is the formula of A* Algorithm?

A* uses:

f(n)=g(n)+h(n)

Where:

g(n) = actual cost from start node
h(n) = heuristic estimated cost
f(n) = total estimated cost

. What are real life applications of A* Algorithm?

Applications:

GPS Navigation
Robot path planning
Video games
Network routing
Maze solving
