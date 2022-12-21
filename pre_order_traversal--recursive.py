from __future__ import annotations
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None):
        self.val: int = val
        self.left: TreeNode | None = left
        self.right: TreeNode | None = right


class Solution:
    def __init__(self):
        self.output: list[int] = []
    
    # dfs
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root != None:
            self.output.append(root.val)
            self.preorderTraversal(root.left)
            self.preorderTraversal(root.right)

        return self.output
