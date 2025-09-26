"""https://neetcode.io/problems/depth-of-binary-tree?list=blind75
did this one a while ago. Not sure why I never uploaded it.
Pretty standard dfs expect the use of nonlocal which I learned during the question
Normally you would just return said variable instead of declaring it outside of the
scope but this was simplier to set up
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0

        def dfs(next_node, current_depth):
            if not next_node:
                return
            nonlocal max_depth
            if next_node.left:
                dfs(next_node.left, current_depth + 1)
            if next_node.right:
                dfs(next_node.right, current_depth + 1)
            max_depth = max(max_depth, current_depth)

        dfs(root, 1)
        return max_depth
