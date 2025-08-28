"""
https://neetcode.io/problems/invert-a-binary-tree?list=blind75
Full disclosure I remember basically nothing about trees from school.
Went back and read on it a bit, understood the traversal methods but when I saw
this problem I froze up and didn't really know what to do. After seeing the solution was
apparently with DFS, swapping left and right nodes (didnt see the code solution just the second 
hint) I tried it again with the preorder traversal method in hand and got it without issue. 
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def reverse_children(tree):
    if tree:
        reverse_children(tree.left)
        reverse_children(tree.right)
        temp = tree.left
        tree.left = tree.right
        tree.right = temp

        
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        reverse_children(root)
        return root


"""
Just thought well we need to get to the bottom and swap left and right, just like the hint said,
so if recursivley we get there just like preorder travel, then swap left and right. 
The last nodes will just swap None and None which shouldn't cause any issues. 
Searched it up, this is actually depth-first search, or at least, its depth first traversal, 
just going as deep as you can go and backing up as you cant go any more. 
Solution is just the same but without the seperate function and tightened up.
"""

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
    
"""
The BFS and DFS iterative solution are both very similar. I'll throw the BFS sol here for ref.
"""

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        queue = deque([root])                               # double ended queue for left pop and append, does this convert it to a list?
        while queue:                                        # expect dequeue to be mt eventually
            node = queue.popleft()                          # so og list was root. At this moment, queue is mt
            node.left, node.right = node.right, node.left   # children of popped node, appending is how we get the next layer.
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root