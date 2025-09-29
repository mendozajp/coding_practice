"""
First passthrough https://neetcode.io/problems/subtree-of-a-binary-tree?list=blind75
this doesnt work as there are duplicates in the tree. It says they are binary trees so I thought
there wouldn't be but binary tree doesnt mean there will be no dups. Binary search tree just
requires there are none. They are not the same thing.

Stopped after this, will come back with a solution later.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        main_root_stack = [root]
        while main_root_stack:
            main_node = main_root_stack.pop()
            if main_node.val == subRoot.val:
                # you'll want to break out of this loop and start the comparison loop
                main_root_stack = [main_node]
                break
            if main_node.right:
                main_root_stack.append(main_node.right)
            if main_node.left:
                main_root_stack.append(main_node.left)
            if not main_root_stack:
                return False

        sub_root_stack = [subRoot]
        while main_root_stack or sub_root_stack:
            main_node = main_root_stack.pop()
            sub_node = sub_root_stack.pop()
            # handle nones
            if None in (main_node, sub_node):
                if main_node == sub_node:
                    continue
                return False
            if main_node.val == sub_node.val:
                # add right to lists for both trees
                main_root_stack.append(main_node.right)
                sub_root_stack.append(sub_node.right)
                if len(main_root_stack) != len(sub_root_stack):
                    return False

                # add left to lists for both trees
                main_root_stack.append(main_node.left)
                sub_root_stack.append(sub_node.left)
                # confirm length of both lists
                if len(main_root_stack) != len(sub_root_stack):
                    return False

            else:
                return False
            if not main_root_stack and not sub_root_stack:
                return True
            if [] in [main_root_stack, sub_root_stack]:
                return False
            print(main_root_stack, sub_root_stack)

        return True


# since we can have duplicates the main idea here doesnt work, back to the drawing board.
