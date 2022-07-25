# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(nlogn) time complexity due to the sorted method using Timsort
# O(1) space complexity if not considering the solution, otherwise O(n + m) where n and m represent the two respective binary trees 
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def getAllElementsFromBST(root: TreeNode) -> List[int]:
            if not root:
                return []
            
            left = getAllElementsFromBST(root.left)
            right = getAllElementsFromBST(root.right)

            return left + [root.val] + right
        
        return sorted(getAllElementsFromBST(root1) + getAllElementsFromBST(root2))