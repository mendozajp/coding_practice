"""
https://neetcode.io/problems/same-binary-tree?list=blind75
This one is fast as can be and I actually ended up doing it pretty fast.
Lot of if statements but simple enough.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if None in (p, q):
            return False

        p_list = [p]
        q_list = [q]
        while p_list or q_list:
            p_tree = p_list.pop()
            q_tree = q_list.pop()
            if p_tree.val != q_tree.val:
                return False
            if p_tree.right:
                p_list.append(p_tree.right)
            if q_tree.right:
                q_list.append(q_tree.right)
            if len(p_list) != len(q_list):
                return False

            if p_tree.left:
                p_list.append(p_tree.left)
            if q_tree.left:
                q_list.append(q_tree.left)
            if len(p_list) != len(q_list):
                return False

        return True


"""
They had a recursive solution going. Cleaner, but recursion sucks so hey
"""


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False
