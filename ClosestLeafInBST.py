# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
from collections import deque
class Solution:
    def findClosestLeaf(self, root: Optional[TreeNode], k: int) -> int:
    
        def traverseBST(root: Optional[TreeNode]) -> Tuple[int, str, List[Tuple[int, int, bool, str]]]:
            dist_from_root = 0
            dist_from_k = 0
            dist_to_k = 0
            k_direction = ""
            all_leaf_nodes = []
            k_seen = False
            queue = deque([(root, "", False)])
            
            while queue:
                curr_lvl = len(queue)
                
                for _ in range(curr_lvl):
                    curr_node, child_dir, k_child = queue.popleft()

                    if curr_node.val == k:
                        dist_to_k = dist_from_root
                        k_seen = True
                        k_direction = child_dir

                    if curr_node.left:
                        queue.append((curr_node.left, "left", False)) 

                        if child_dir == "right" or (root.right and curr_node.val == root.right.val):
                            queue[-1] = (curr_node.left, "right", False)

                        if curr_node.val == k or k_child:
                            queue[-1] = (curr_node.left, queue[-1][1], True)

                    if curr_node.right:
                        queue.append((curr_node.right, "right", False))

                        if child_dir == "left" or (root.left and curr_node.val == root.left.val):
                            queue[-1] = (curr_node.right, "left", False)
                    
                        if curr_node.val == k or k_child:
                            queue[-1] = (curr_node.right, queue[-1][1], True)
                    
                    # if we're not one of thr children of the k node and we're on a leaf node
                    if not k_child and not curr_node.left and not curr_node.right:
                        all_leaf_nodes.append((curr_node.val, dist_from_root, False, child_dir))

                    # if we're on the side of the k node and we're on a leaf node
                    if k_child and not curr_node.left and not curr_node.right:
                        all_leaf_nodes.append((curr_node.val, dist_from_k, True, ""))
                        
                if k_seen:
                    dist_from_k += 1
                
                dist_from_root += 1
            return dist_to_k, k_direction, all_leaf_nodes
        
        dist_to_k, k_direction, all_leaf_nodes = traverseBST(root)
        
        min_val = 0
        min_dist = float("inf")
        for val, dist, k_child, direction in all_leaf_nodes:
            if val == k: # if k is a leaf node, return it
                return k
            if not k_child:
                if direction != k_direction: # if we're on the opposite side of the tree from the k node
                    dist += dist_to_k
                else: # otherwise we're on the same root subtree
                    dist = abs(dist - dist_to_k + 2)
            if dist < min_dist:
                min_val = val
                min_dist = min(min_dist, dist)
        return min_val