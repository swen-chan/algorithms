Adding Exits to a Maze

Problem Introduction
Now you decide to make sure that there are no dead zones in a maze, that is, that at least one exit is
reachable from each cell. For this, you find connected components of the corresponding undirected graph
and ensure that each component contains an exit cell.

Problem Description
Task. Given an undirected graph with 𝑛 vertices and 𝑚 edges, compute the number of connected components
in it.
Input Format. A graph is given in the standard format.
Constraints. 1 ≤ 𝑛 ≤ 10^3, 0 ≤ 𝑚 ≤ 10^3.
Output Format. Output the number of connected components.

#Uses python3.10

def find(a, result):
    if visit[a] == 1:
        return result
    else:
        visit[a] = 1
        if len(adj[a]) != 0:
            for i in adj[a]:
                find(i, result)
        return result + 1


def number_of_components(adj):
    result = 0
    for i in range(n):
        result = find(i, result)
        #print(visit)
    return result


if __name__ == '__main__':
    n, m = map(int, input().split())
    lines = [[] for _ in range(m)]
    for i in range(m):
        lines[i] = list(map(int, input().strip().split()))
    adj = [[] for _ in range(n)]
    for line in lines:
        l1 = line[0]
        l2 = line[1]
        adj[l1 - 1].append(l2 - 1)
        adj[l2 - 1].append(l1 - 1)
    #print(adj)
    visit = [0 for i in range(n)]
    print(number_of_components(adj))
