def biggest_descendent(graph, root, value):
    result = {}
    
    def dfs(node):
        max_value = value[node]
        
        for child in graph.successors(node):
            child_max = dfs(child)
            max_value = max(max_value, child_max)
        
        result[node] = max_value
        return max_value
    
    dfs(root)
    return result