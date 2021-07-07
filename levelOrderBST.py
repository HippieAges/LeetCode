class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = [] if root == None else [(root, 0)]
        nodes = []
        
        while len(queue) > 0:
            top_node, lvl = queue.pop(0)
            
            if top_node != None:
                queue.append((top_node.left, lvl + 1))
                queue.append((top_node.right, lvl + 1))
                
                len_nodes = len(nodes)
                if len_nodes == 0 or lvl >= len_nodes:
                    nodes.append([top_node.val])
                else:
                    nodes[lvl].append(top_node.val)
                                
        return nodes