
# Python program for implementation
# of Ford Fulkerson algorithm
from collections import defaultdict
 
# This class represents a directed graph
# using adjacency matrix representation
class Graph:
 
    def __init__(self, graph):
        self.graph = graph  # residual graph
        self. ROW = len(graph)
        # self.COL = len(gr[0])
 
    '''Returns true if there is a path from source 's' to sink 't' in
    residual graph. Also fills parent[] to store the path '''
 
    def BFS(self, s, t, parent):
 
        # Mark all the vertices as not visited
        visited = [False]*(self.ROW)
 
        # Create a queue for BFS
        queue = []
 
        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True
 
         # Standard BFS Loop
        while queue:
 
            # Dequeue a vertex from queue and print it
            u = queue.pop(0)
 
            # Get all adjacent vertices of the dequeued vertex u
            # If a adjacent has not been visited, then mark it
            # visited and enqueue it
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                      # If we find a connection to the sink node,
                    # then there is no point in BFS anymore
                    # We just have to set its parent and can return true
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
                    if ind == t:
                        return True
 
        # We didn't reach sink in BFS starting
        # from source, so return false
        return False
             
     
    # Returns the maximum flow from s to t in the given graph
    def FordFulkerson(self, source, sink):
 
        # This array is filled by BFS and to store path
        parent = [-1]*(self.ROW)
 
        max_flow = 0 # There is no flow initially
 
        # Augment the flow while there is path from source to sink
        while self.BFS(source, sink, parent) :
 
            # Find minimum residual capacity of the edges along the
            # path filled by BFS. Or we can say find the maximum flow
            # through the path found.
            path_flow = float("Inf")
            s = sink
            while(s !=  source):
                path_flow = min (path_flow, self.graph[parent[s]][s])
                s = parent[s]
 
            # Add path flow to overall flow
            max_flow +=  path_flow
 
            # update residual capacities of the edges and reverse edges
            # along the path
            v = sink
            while(v !=  source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
 
        return max_flow


# The code above was taken from GeeksForGeeks
# https://www.geeksforgeeks.org/ford-fulkerson-algorithm-for-maximum-flow-problem/


def solution(entr, exits, path):
    for i in range(len(path)):
        path[i] = [0] + path[i] + [0]

    path.insert(0, [0] * len(path[0]))
    path.append([0] * len(path[0]))

    for e in entr:
        path[0][e+1] = sum(path[e+1])

    for e in exits:
        path[e+1][-1] = 2000000
        #path[e+1][-1] = sum([path[f][e+1] for f in range(len(path))])

    return Graph(path).FordFulkerson(0, len(path) - 1)


 
# path = [
#     [0, 10, 7, 0, 0, 0, 0, 0],
#     [0, 0, 0, 4, 6, 0, 0, 0],  # Room 0: Bunnies
#     [0, 0, 0, 5, 2, 0, 0, 0],  # Room 1: Bunnies
#     [0, 0, 0, 0, 0, 4, 4, 0],  # Room 2: Intermediate room
#     [0, 0, 0, 0, 0, 6, 6, 0],  # Room 3: Intermediate room
#     [0, 0, 0, 0, 0, 0, 0, 10],  # Room 4: Escape pods
#     [0, 0, 0, 0, 0, 0, 0, 10],  # Room 5: Escape pods
#     [0, 0, 0, 0, 0, 0, 0, 0]
# ]

# graph2 = [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]]
 
# g = Graph(path)
 
# source = 0; sink = 7

entrances = [0, 1]
exits = [4, 5]
path = [
  [0, 0, 4, 6, 0, 0],  # Room 0: Bunnies
  [0, 0, 5, 2, 0, 0],  # Room 1: Bunnies
  [0, 0, 0, 0, 4, 4],  # Room 2: Intermediate room
  [0, 0, 0, 0, 6, 6],  # Room 3: Intermediate room
  [0, 0, 0, 0, 0, 0],  # Room 4: Escape pods
  [0, 0, 0, 0, 0, 0],  # Room 5: Escape pods
]
  
print(solution(entrances, exits, path))