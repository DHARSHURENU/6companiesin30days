# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        res=0
        def traverse(node):
            if node is None:
                return(0,0)
            left=traverse(node.left)
            right=traverse(node.right)
            tot=left[0]+right[0]+node.val
            cnt=left[1]+right[1]+1
            if tot//cnt == node.val:
                nonlocal res
                res+=1
            return (tot,cnt)
        traverse(root)
        return res
