from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:        
        nodes = defaultdict(list)
        counter = set()

        for node1, node2 in edges:
            # print(node1, node2)
            counter |= {node1, node2}
            nodes[node1].append(node2)
        
        visited = set()
        print(nodes)
        connectedComps = 0
        
        def dfs(edges: List[int], nodes: Dict[int, int], n: int) -> int:
            # print(edge)
            if edges in visited:
                return 0
            elif n == 0 or (type(edges) != list and edges not in nodes):
                visited.add(edges)
                return 1
            
            newComponent = 0
            for edge in nodes[edges]:
                print(edge)
                newComponent |= dfs(edge, nodes, n - 1)
                visited.add(edges)
                # print(visited, edge)
            return newComponent
                        
        for edges in nodes:
            connectedComps += dfs(edges, nodes, n - 1)
        # print(connectedComps)
        connectedComps += (n - len(counter))
        print(counter)
        return connectedComps    