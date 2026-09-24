class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # This is just cycle detection
        # I can assume nodes have unique values, or IDs from 0 to n-1.
        from collections import defaultdict
        # if not edges:
        #     return True
        
        adj_map = defaultdict(set)
        for a, b in edges:
            # This works, but you can also make it more clear
            # by doing for edge in edges, and a=edge[0], b=edge[1] and such.
            adj_map[a].add(b)
            adj_map[b].add(a)
        
            
        visited = set()
        def dfs(node, parent):
            
            visited.add(node)
            for nxt in adj_map[node]:
                if nxt == parent:
                    continue
                if nxt in visited:
                    return False
                if dfs(nxt, node) == False:
                    return False
            return True
            
        if not dfs(0, -1):
            return False
        return len(visited) == n
