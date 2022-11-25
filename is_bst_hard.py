'''
Problem Description

Task. You are given a binary tree with integers as its keys. You need to test whether it is a correct binary
search tree. Note that there can be duplicate integers in the tree, and this is allowed. The definition of
the binary search tree in such case is the following: for any node of the tree, if its key is 𝑥, then for any
node in its left subtree its key must be strictly less than 𝑥, and for any node in its right subtree its key
must be greater than or equal to 𝑥. In other words, smaller elements are to the left, bigger elements
are to the right, and duplicates are always to the right. You need to check whether the given binary
tree structure satisfies this condition. You are guaranteed that the input contains a valid binary tree.
That is, it is a tree, and each node has at most two children.

Input Format. The first line contains the number of vertices 𝑛. The vertices of the tree are numbered
from 0 to 𝑛 − 1. Vertex 0 is the root.
The next 𝑛 lines contain information about vertices 0, 1, ..., 𝑛−1 in order. Each of these lines contains
three integers 𝑘𝑒𝑦𝑖, 𝑙𝑒𝑓 𝑡𝑖 and 𝑟𝑖𝑔ℎ𝑡𝑖 — 𝑘𝑒𝑦𝑖 is the key of the 𝑖-th vertex, 𝑙𝑒𝑓 𝑡𝑖 is the index of the left
child of the 𝑖-th vertex, and 𝑟𝑖𝑔ℎ𝑡𝑖 is the index of the right child of the 𝑖-th vertex. If 𝑖 doesn’t have
left or right child (or both), the corresponding 𝑙𝑒𝑓 𝑡𝑖 or 𝑟𝑖𝑔ℎ𝑡𝑖 (or both) will be equal to −1.

Constraints. 0 ≤ 𝑛 ≤ 10^5; −2^31 ≤ 𝑘𝑒𝑦𝑖 ≤ 2^31 − 1; −1 ≤ 𝑙𝑒𝑓 𝑡𝑖, 𝑟𝑖𝑔ℎ𝑡𝑖 ≤ 𝑛 − 1. It is guaranteed that the
input represents a valid binary tree. In particular, if 𝑙𝑒𝑓 𝑡𝑖 ̸= −1 and 𝑟𝑖𝑔ℎ𝑡𝑖 ̸= −1, then 𝑙𝑒𝑓 𝑡𝑖 ̸= 𝑟𝑖𝑔ℎ𝑡𝑖.
Also, a vertex cannot be a child of two different vertices. Also, each vertex is a descendant of the root
vertex. Note that the minimum and the maximum possible values of the 32-bit integer type are allowed
to be keys in the tree — beware of integer overflow!

Output Format. If the given binary tree is a correct binary search tree (see the definition in the problem
description), output one word “CORRECT” (without quotes). Otherwise, output one word “INCORRECT” (without quotes).
'''

#NOTICE:The difference between this question and question in is_bst.py is that 'for any node in its right subtree its key
#must be greater than or equal to 𝑥. '

import sys, threading

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size
mini = -(2 ** 64)
maxi = 2 ** 64


def isbit(i, mini, maxi):
    if i == -1:
        return True
    le = left[i]
    ri = right[i]
    if node[i] > maxi or node[i] < mini :
        return False
    return (isbit(le, mini, node[i]-1) and
            isbit(ri, node[i], maxi))

def isbinarysearchtree(i):
    # Implement correct algorithm here

    return isbit(i, mini, maxi)

def leftbiggerroot(root):
    if root == -1:
        return True
    no = node[root]
    if no > node[0] :
        return False
    return (leftbiggerroot(right[root]) and
            leftbiggerroot(left[root]))

def rightsmallerroot(root):
    if root == -1:
        return True
    no = node[root]
    if no < node[0]:
        return False
    return (rightsmallerroot(left[root]) and
            rightsmallerroot(right[root]))

def main():
    nodes = int(sys.stdin.readline().strip())
    if nodes == 0:
        print("CORRECT")
        return 0
    global node
    node = [0] * nodes
    global left
    left = [0] * nodes
    global right
    right = [0] * nodes

    for i in range(nodes):
        line = sys.stdin.readline().strip().split()
        node[i] = int(line[0])
        left[i] = int(line[1])
        right[i] = int(line[2])
        # node[i] = number[0]
        # left[i] = number[1]
        # right[i] = number[2]

    if (isbinarysearchtree(0) and leftbiggerroot(left[0]) and rightsmallerroot(right[0])):
        print("CORRECT")
    else:
        print("INCORRECT")


threading.Thread(target=main).start()
