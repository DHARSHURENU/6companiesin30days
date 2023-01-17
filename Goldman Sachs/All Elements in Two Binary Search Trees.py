# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        res1 = []        
        self.inorder_traverse(root1, res1)
        res2 = []        
        self.inorder_traverse(root2, res2)
        res = []
        i = 0
        j = 0
        while i < len(res1) and j < len(res2):
            if res1[i] < res2[j]:
                res.append(res1[i])
                i += 1
            else:
                res.append(res2[j])
                j += 1
        while i < len(res1):
            res.append(res1[i])
            i += 1
        while j < len(res2):
            res.append(res2[j])
            j += 1
        return res
    def inorder_traverse(self, root, res):
        if not root:
            return
        self.inorder_traverse(root.left, res)
        res.append(root.val)
        self.inorder_traverse(root.right, res)
        
