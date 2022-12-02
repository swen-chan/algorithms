Finding an Exit from a Maze

Problem Introduction:
A maze is a rectangular grid of cells with walls between some of adjacent cells.
You would like to check whether there is a path from a given cell to a given
exit from a maze where an exit is also a cell that lies on the border of the maze
(in the example shown to the right there are two exits: one on the left border
and one on the right border). For this, you represent the maze as an undirected
graph: vertices of the graph are cells of the maze, two vertices are connected by
an undirected edge if they are adjacent and there is no wall between them. Then,
to check whether there is a path between two given cells in the maze, it suffices to
check that there is a path between the corresponding two vertices in the graph.
Problem Description

Task. Given an undirected graph and two distinct vertices 𝑢 and 𝑣, check if there is a path between 𝑢 and 𝑣.
Input Format. An undirected graph with 𝑛 vertices and 𝑚 edges. The next line contains two vertices 𝑢
and 𝑣 of the graph.

Constraints. 2 ≤ 𝑛 ≤ 10^3; 1 ≤ 𝑚 ≤ 10^3; 1 ≤ 𝑢, 𝑣 ≤ 𝑛; 𝑢 ̸= 𝑣.

Output Format. Output 1 if there is a path between 𝑢 and 𝑣 and 0 otherwise.

#python 3.10

visit = []
def reach(adj, x, y):
    #write your code here
    for i in adj[x]:
        if i not in visit:
            visit.append(i)
            reach(adj, i, y)
    if y in visit:
        return 1
    else:
        return 0

if __name__ == '__main__':
    n, m = map(int, input().split())
    lines = [[] for _ in range(m)]
    for i in range(m):
        lines[i] = list(map(int, input().strip().split()))
    a, b = map(int, input().split())
    adj = [[] for _ in range(n)]
    for line in lines:
        l1 = line[0]
        l2 = line[1]
        adj[l1-1].append(l2-1)
        adj[l2-1].append(l1-1)
    print(reach(adj, a-1, b-1))
