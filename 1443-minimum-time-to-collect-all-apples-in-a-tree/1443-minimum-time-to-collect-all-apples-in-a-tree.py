from collections import defaultdict

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        
        adjacency_list = defaultdict(list)
        
        for src_node, dst_node in edges:
            adjacency_list[src_node].append(dst_node)
            adjacency_list[dst_node].append(src_node)
        visited = set()
        
        def cld(cur_node):
            
            visited.add(cur_node)
            
            cost_of_collect = 0
            
            for child_node in adjacency_list[cur_node]:
                
                if child_node in visited:
                    continue
                cost_from_child = cld(child_node)
                
                if cost_from_child or hasApple[child_node]:

                    cost_of_collect += cost_from_child + 2
            
            return cost_of_collect
        

        rni = 0
        return cld(cur_node=rni)