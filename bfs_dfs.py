# BFS and DFS using Adjacency List

from collections import deque   # deque means double ended queue used in BFS

# Create graph from user
graph = {}   # graph dictionary stores vertex and its neighbours

n = int(input("Enter number of vertices: "))  
# takes total number of vertices from user

for i in range(n):

    node = input("Enter vertex: ")  
    # takes vertex name

    neighbours = input("Enter neighbours separated by space: ").split()
    # takes neighbours in one line and split them into list

    graph[node] = neighbours  
    # store vertex and neighbours in graph dictionary


# DFS Function
def dfs(node, visited):

    visited.add(node)  
    # add current node into visited set

    print(node, end=" ")  
    # print current node

    for neighbour in graph[node]:  
        # check all neighbours of current node

        if neighbour not in visited:  
            # if neighbour not visited

            dfs(neighbour, visited)  
            # recursive call for neighbour


# BFS Function
def bfs(start):

    visited = set()  
    # set stores visited nodes

    queue = deque([start])  
    # create queue and insert starting node

    visited.add(start)  
    # mark start node as visited

    while queue:  
        # loop runs until queue becomes empty

        node = queue.popleft()  
        # remove first element from queue

        print(node, end=" ")  
        # print current node

        for neighbour in graph[node]:  
            # check all neighbours

            if neighbour not in visited:  
                # if neighbour not visited

                visited.add(neighbour)  
                # mark neighbour as visited

                queue.append(neighbour)  
                # insert neighbour into queue


# Main Program
start = input("Enter starting vertex: ")  
# takes starting node from user

print("\nDFS Traversal:")
dfs(start, set())  
# call DFS function with empty visited set

print("\nBFS Traversal:")
bfs(start)  
# call BFS function



viva
Important Points
DFS (Depth First Search)
Goes deep into graph first using recursion.
BFS (Breadth First Search)
Visits level by level using queue.
Adjacency List
Graph representation where each node stores list of neighbours.
Queue
FIFO structure used in BFS.
Visited Set
Prevents revisiting same node again.

29. What are real life applications of BFS?

Applications of BFS:

Social networking
GPS shortest path
Web crawling
Broadcasting systems
30. What are real life applications of DFS?

Applications of DFS:

Maze solving
Topological sorting
Cycle detection
Path finding
31. Why is graph called non-linear data structure?

Because nodes are not stored sequentially like arrays or linked lists.

Each node can connect to multiple nodes.
