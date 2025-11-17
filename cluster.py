from collections import deque

def cluster(graph, weights, level):
    """
    Computes clusters of a weighted graph at a given level.

    Args:
        graph: An instance of dsc40graph.UndirectedGraph
        weights: A function returning the weight of edge (u, v)
        level: Threshold for edge weights

    Returns:
        frozenset of frozensets, where each inner frozenset is a cluster of nodes
    """
    visited = set()
    clusters = []

    for start in graph.nodes:
        if start in visited:
            continue

        component = set()
        queue = deque([start])
        visited.add(start)

        while queue:
            u = queue.popleft()
            component.add(u)

            for v in graph.neighbors(u):
                if v in visited:
                    continue
                if weights(u, v) >= level:
                    visited.add(v)
                    queue.append(v)

        clusters.append(frozenset(component))

    return frozenset(clusters)
