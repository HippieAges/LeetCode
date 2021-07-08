class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = [] if root == None else [(root, 0)]
        mirrored_queue = queue.copy()
        nodes = []
        
        while len(queue) > 0:
            back_node, _ = mirrored_queue.pop()
            top_node, lvl = queue.pop(0)
            
            if lvl % 2 != 0:
                if back_node.left != None:
                    queue.append((back_node.left, lvl + 1))
                if back_node.right != None:
                    queue.append((back_node.right, lvl + 1))
            else:
                if back_node.right != None:
                    queue.append((back_node.right, lvl + 1))
                if back_node.left != None:
                    queue.append((back_node.left, lvl + 1))
                
            if lvl == 0 or len(mirrored_queue) == 0:
                mirrored_queue = queue.copy()
                
            len_nodes = len(nodes)
            if len_nodes == 0 or lvl >= len_nodes:
                nodes.append([top_node.val])
            else:
                nodes[lvl].append(top_node.val)
                
                                
        return nodes