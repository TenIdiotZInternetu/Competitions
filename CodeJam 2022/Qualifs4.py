from queue import Queue

class Tree:
    def __init__(self, nodes):
        self.nodes = []
        self.initiators = []

        for i in range(nodes):
            self.nodes.append(Node(i))


class Node:
    def __init__(self, i):
        self.index = i
        self.parents= []
        self.child = None
        self.fun = 0

        self.visited = False
        self.unvisited = Queue()
        self.is_initiator = False


def create_tree(F, P):
    tree = Tree(len(F) + 1)

    for i in range(1, len(F) + 1):
        tree.nodes[i].index = i
        tree.nodes[i].fun = F[i - 1]
        tree.nodes[i].child = tree.nodes[P[i - 1]]
        tree.nodes[i].child.parents.append(tree.nodes[i])
        tree.nodes[i].child.unvisited.put(tree.nodes[i])
        

    for node in tree.nodes:
        if not node.parents:
            node.is_initiator = True
            tree.initiators.append(node)

    return tree


# def get_max_fun(node):
#     if not node.parents:
#         node.max_fun = node.fun
#         return node.max_fun

#     maxes = [node.fun]

#     for parent in node.parents:
#         maxes.append(get_max_fun(parent))
        
#     node.max_fun = max(maxes)

#     return node.max_fun


def get_max_fun(tree):
    stack = []
    stack.append(tree.nodes[0])

    while stack:
        cur = stack.pop()

        if not cur.unvisited.empty():
            stack.append(cur)
            stack.append(cur.unvisited.get())
            continue

        if cur.is_initiator:
            cur.max_fun = cur.fun
            continue

        maxes = [cur.fun]

        for p in cur.parents:
            maxes.append(p.max_fun)

        cur.max_fun = max(maxes)


def DFS(tree):
    out = 0
    subtrees = Queue()
    subtrees.put(tree.nodes[0])

    while not subtrees.empty():
        q = Queue()
        q.put(subtrees.get())
        sub_funs = []

        while not q.empty():
            cur = q.get()

            sub_funs.append(cur.fun)
            if cur.is_initiator: continue

            maxes = {}

            for p in cur.parents:
                maxes[p] = p.max_fun

            maxes_vals = list(maxes.values())
            maxes_keys = list(maxes.keys())
            next = maxes_keys[maxes_vals.index(min(maxes_vals))]

            for p in cur.parents:
                if p != next: subtrees.put(p)

            q.put(next)
            

        out += max(sub_funs)

    return out

    



T = int(input())

for t in range(T):
    N = int(input())
    F = input().split()
    P = input().split()
    
    for n in range(N):
        F[n] = int(F[n])
        P[n] = int(P[n])

    tree = create_tree(F, P)
    get_max_fun(tree)
    print("Case #" + str(t + 1) + ":", DFS(tree))
    

