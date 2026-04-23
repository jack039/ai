import heapq

g = {'A':[('B',1),('C',3)],'B':[('D',1)],'C':[('D',1)],'D':[]}
h = {'A':3,'B':1,'C':1,'D':0}

def astar(start, goal):
    pq = [(h[start], 0, start, [])]
    while pq:
        f, cost, node, path = heapq.heappop(pq)
        if node == goal:
            return path + [node]
        for nei, w in g[node]:
            heapq.heappush(pq, (cost + w + h[nei], cost + w, nei, path + [node]))

print(astar('A','D'))
'''Experiment 4: Theory
Title:

Informed Search Method (A* Algorithm)

Theory:

Informed search algorithms use additional knowledge (heuristics) to find solutions more efficiently. The A* (A-star) algorithm is one of the most widely used informed search techniques.

A* selects the best path based on the evaluation function:

f(n)=g(n)+h(n)

f(n)=g(n)+h(n)

Where:

g(n): Cost from start node to current node
h(n): Heuristic estimate from current node to goal
f(n): Total estimated cost

A* always chooses the node with the lowest f(n) value, ensuring an optimal and efficient path to the goal.

Applications:
Pathfinding (maps, games)
Robotics navigation
Network routing
Conclusion:

A* algorithm improves search efficiency by combining actual cost and heuristic, making it faster and optimal.'''