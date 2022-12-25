#Uses python3
'''
Detecting Anomalies in Currency Exchange Rates

Problem Introduction

You are given a list of currencies 𝑐1, 𝑐2, . . . , 𝑐𝑛 together with a list of exchange
rates: 𝑟𝑖𝑗 is the number of units of currency 𝑐𝑗 that one gets for one unit of 𝑐𝑖. You 
would like to check whether it is possible to start with one unit of some currency, 
perform a sequence of exchanges, and get more than one unit of the same currency. 
In other words, you would like to find currencies 𝑐𝑖1, 𝑐𝑖2, . . . , 𝑐𝑖𝑘 such that
𝑟𝑖1,𝑖2· 𝑟𝑖2,𝑖3· 𝑟𝑖𝑘−1,𝑖𝑘, 𝑟𝑖𝑘,𝑖1 > 1. For this, you construct the following graph: 
vertices are currencies 𝑐1, 𝑐2, . . . , 𝑐𝑛, the weight of an edge from 𝑐𝑖 to 𝑐𝑗 is equal to − log 𝑟𝑖𝑗 . 
There it suffices to check whether is a negative cycle in this graph. Indeed, 
assume that a cycle 𝑐𝑖 → 𝑐𝑗 → 𝑐𝑘 → 𝑐𝑖 has negative weight. This means that −(log 𝑐𝑖𝑗 + log 𝑐𝑗𝑘 + log 𝑐𝑘𝑖) < 0
and hence log 𝑐𝑖𝑗 + log 𝑐𝑗𝑘 + log 𝑐𝑘𝑖 > 0. This, in turn, means that 𝑟𝑖𝑗*𝑟𝑗𝑘*𝑟𝑘𝑖 = 2^log𝑐𝑖𝑗 * 2^log𝑐𝑗𝑘 * 2^log𝑐𝑘𝑖 
= 2^(log𝑐𝑖𝑗+log𝑐𝑗𝑘+log𝑐𝑘𝑖） > 1 .

Problem Description

Task. Given an directed graph with possibly negative edge weights and with 𝑛 vertices and 𝑚 edges, check
whether it contains a cycle of negative weight.
Input Format. A graph is given in the standard format.
Constraints. 1 ≤ 𝑛 ≤ 10^3, 0 ≤ 𝑚 ≤ 10^4, edge weights are integers of absolute value at most 10^3.
Output Format. Output 1 if the graph contains a cycle of negative weight and 0 otherwise.
'''
import sys

def negative_cycle(adj, cost):
    #can't use inf for initialization,because the inf is not mathematically strict infinite,but a constant,so it will meet problem at line 37
    dist = [1001] * len(adj)
    dist[0] = 0
    for i in range(len(adj)):
        for u in range(len(adj)):
            for v in adj[u]:
                v_index = adj[u].index(v)
                if  dist[v] > dist[u] + cost[u][v_index]:
                    dist[v] = dist[u] + cost[u][v_index]
                    # if it's the last iliteration
                    if i == len(adj) - 1:
                        return 1
    return 0

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
    print(negative_cycle(adj, cost))
