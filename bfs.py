g = {'A':['B','C'],'B':['D'],'C':['E'],'D':[],'E':[]}

def bfs(s):
    q, v = [s], set()
    while q:
        n = q.pop(0)
        if n not in v:
            print(n,end=' ')
            v.add(n)
            q += g[n]

def dfs(s, v=set()):
    if s not in v:
        print(s,end=' ')
        v.add(s)
        for i in g[s]: dfs(i,v)

bfs('A'); print()
dfs('A')
'''Experiment 3: Theory (Very Short)

Breadth First Search (BFS) and Depth First Search (DFS) are uninformed search algorithms used to traverse or search in a graph or tree.

BFS explores nodes level by level using a queue (FIFO). It finds the shortest path in unweighted graphs.
DFS explores nodes deeply first using a stack/recursion (LIFO). It goes to the deepest node before backtracking.

Both algorithms are used to explore state spaces and find solutions in AI problems.'''