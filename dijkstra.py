#Uses python3.10
'''
1 Computing the Minimum Cost of a Flight

Problem Introduction

Now, you are interested in minimizing not the number of segments, but the total cost of a flight. For this
you construct a weighted graph: the weight of an edge from one city to another one is the cost of the
corresponding flight.

Problem Description

Task. Given an directed graph with positive edge weights and with 𝑛 vertices and 𝑚 edges as well as two
vertices 𝑢 and 𝑣, compute the weight of a shortest path between 𝑢 and 𝑣 (that is, the minimum total
weight of a path from 𝑢 to 𝑣).
Input Format. A graph is given in the standard format. The next line contains two vertices 𝑢 and 𝑣.
Constraints. 1 ≤ 𝑛 ≤ 10^4, 0 ≤ 𝑚 ≤ 10^5, 𝑢 ̸= 𝑣, 1 ≤ 𝑢, 𝑣 ≤ 𝑛, edge weights are non-negative integers not exceeding 10^8.
Output Format. Output the minimum weight of a path from 𝑢 to 𝑣, or −1 if there is no path.
'''

import sys
import queue
import math

class Node:
    def __init__(self, index, distance):
        self.index = index
        self.distance = distance
    #you can use cmp function directly in python 3,so define the comparisons.
    def __lt__(self, other):
        return (self.distance < other.distance)

    def __gt__(self, other):
        return (self.distance > other.distance)

    def __eq__(self, other):
        return (self.distance == other.distance)

def distance(adj, cost, s, t):
    dist = [math.inf] * len(adj)
    dist[s] = 0
    h = queue.PriorityQueue()
    h.put(Node(s, dist[s]))
    while not h.empty():
         u = h.get()
         u_index = u.index
         for v in adj[u_index]:
             v_index = adj[u_index].index(v)
             if dist[v] > dist[u_index] + cost[u_index][v_index]:
                 dist[v] = dist[u_index] + cost[u_index][v_index]
                 h.put(Node(v, dist[v]))
    if dist[t] == math.inf:
        return -1
    else:
        return dist[t]


if __name__ == '__main__':
    n, m = map(int, input().split())
    lines = [[] for _ in range(m)]
    for i in range(m):
        lines[i] = list(map(int, input().strip().split()))
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for line in lines:
        l1 = line[0]
        l2 = line[1]
        w = line[2]
        adj[l1 - 1].append(l2 - 1)
        cost[l1 - 1].append(w)
    s, t = map(int, input().split())
    s, t = s - 1, t - 1
    print(distance(adj, cost, s, t))


