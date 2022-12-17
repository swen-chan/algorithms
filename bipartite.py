#Uses python3

import sys
import queue

def bipartite(s, col):
    q = [s]
    while q:
        u = q.pop(0)
        for v in adj[u]:
            if col[v] == -1:
                col[v] = 1 - col[u]
                q.append(v)
            elif col[v] == col[u]:
                return False
    return True

def ispartite(adj):
    col = [-1] * len(adj)
    for i in range(len(adj)):
        if col[i] == -1:
            if not bipartite(i, col):
                return 0
    return 1

if __name__ == '__main__':
    n, m = map(int, input().split())
    lines = [[] for _ in range(m)]
    for i in range(m):
        lines[i] = list(map(int, input().strip().split()))
    adj = [[] for _ in range(n)]
    reach = [[] for _ in range(n)]
    for line in lines:
        l1 = line[0]
        l2 = line[1]
        adj[l1 - 1].append(l2 - 1)
        adj[l2 - 1].append(l1 - 1)
    print(ispartite(adj))
