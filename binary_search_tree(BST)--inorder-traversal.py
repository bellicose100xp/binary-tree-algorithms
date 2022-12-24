# Inorder traversal of binary search tree (BST) happends from smallest node value to largest node value

from __future__ import annotations
from typing import List, Optional  # type: ignore
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None):
        self.val: int = val
        self.left: TreeNode | None = left
        self.right: TreeNode | None = right

class BinaryTree:
    def buildTreeLeetCode(self, arr: list[int | None]) -> TreeNode | None:
        node_arr: list[TreeNode | None] = []

        # convert all values to TreeNode(s)
        for val in arr:
            if val:
                node_arr.append(TreeNode(val))
            else:
                node_arr.append(None)
        
        n = len(node_arr)
        for idx, node in enumerate(node_arr):
            if node is None:
                continue

            next_left_idx = idx*2 + 1  # next left idx for current node
            if next_left_idx < n:  # if next left index is greater then or equal to array length then break as we've reached the end of array
                if node_arr[next_left_idx]:
                    node.left = node_arr[next_left_idx]
            else:
                break

            next_right_idx = idx*2 + 2  # next right idx for current node
            if next_right_idx < n:  # if next right index is greater then or equal to array length then break as we've reached the end of array
                if node_arr[next_right_idx]:
                    node.right = node_arr[next_right_idx]
            else:
                break

        return node_arr[0]

# utility functions
def printTree(root: TreeNode | None) -> None:
    tree: str = ''
    queue: deque[TreeNode | None] = deque([root])

    while True:
        node = queue.pop()
        val = f'{node.val}' if node else 'None'
        tree += f'{val}'

        if node:
            queue.appendleft(node.left)
            queue.appendleft(node.right)

        if not queue or not any(queue):
            break
        else:
            tree += ' -> '

    print(tree)

# create sorted array using inorder traversal of binary search tree
def inorder(root: TreeNode | None) -> list[int]:
    if not root:
        return []
    
    return inorder(root.left) + [root.val] + inorder(root.right)

tree = BinaryTree()
leet: list[int | None] = [5,3,6,2,4,None,None,1] # BST
root = tree.buildTreeLeetCode(leet)
# printTree(root)
print(inorder(root))