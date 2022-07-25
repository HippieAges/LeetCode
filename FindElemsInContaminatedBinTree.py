# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:
    
    # O(V) time complexity since we visit each node once
    # O(V) space complexity since we store each node once
    def __init__(self, root: Optional[TreeNode]):
        self.node_vals = {}
        self._uncontaminate(root, 0)
    
    # O(1) time complexity since hashMap search is constant
    # O(1) space complexity since we don't allocate additional memory
    def find(self, target: int) -> bool:
        return self.node_vals.get(target, None) != None
        
    def _uncontaminate(self, root: Optional[TreeNode], root_val: int) -> None:
        if not root:
            return
        
        self.node_vals[root_val] = root_val
        
        self._uncontaminate(root.left, 2 * root_val + 1)
        self._uncontaminate(root.right, 2 * root_val + 2)

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)