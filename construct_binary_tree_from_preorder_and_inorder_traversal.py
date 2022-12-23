# first value in pre-order traversal is always root
# preorder = [3,9,20,15,7]  inorder = [9,3,15,20,7]
# ouput = [3,9,20,null,null,15,7]

from __future__ import annotations
from collections import deque


class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None):
        self.val: int = val
        self.left: TreeNode | None = left
        self.right: TreeNode | None = right


class BinaryTree:
    def buildTreePreOrderAndInOrder(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        if not preorder and not inorder:
            return None

        root_val = preorder[0]
        root = TreeNode(root_val)
        mid = inorder.index(root_val)

        root.left = self.buildTreePreOrderAndInOrder(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTreePreOrderAndInOrder(preorder[mid+1:], inorder[mid+1:])

        return root

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


tree = BinaryTree()
root = tree.buildTreePreOrderAndInOrder(preorder=[3, 9, 20, 15, 7], inorder=[9, 3, 15, 20, 7])
printTree(root)
