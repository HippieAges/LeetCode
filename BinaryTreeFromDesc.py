# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(V) time complexity
# O(V) space complexity
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        
        # add every parent-child into a hash table
        nodes = {}
        children = {}
        for parent, child, isLeft in descriptions:
            if nodes.get(parent):
                if isLeft:
                    nodes[parent].insert(0, (child, isLeft))
                else:
                    nodes[parent].append((child, isLeft))
            else:
                nodes[parent] = [(child, isLeft)]
            children[child] = [parent]
        
        # find the root node to begin dfs
        root = None
        for parent in nodes:
            if not children.get(parent):
                root = parent
                break
        
        def dfs(root: int) -> Optional[TreeNode]:
            if not nodes.get(root):
                return TreeNode(root)

            root_node = TreeNode(root)
            nodes_len = len(nodes[root])
            if nodes_len == 1:
                if nodes[root][0][1] == 1:
                    root_node.left = dfs(nodes[root][0][0])
                else:
                    root_node.right = dfs(nodes[root][0][0])
            elif nodes_len == 2:
                root_node.left = dfs(nodes[root][0][0])
                root_node.right = dfs(nodes[root][1][0])
            return root_node
                
        return dfs(root)