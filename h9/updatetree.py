def build_tree_adj(n, tree_edges):
    # build adjacency list for MST
    adj = [[] for _ in range(n)]
    for u, v, w in tree_edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    return adj

def find_heaviest_on_path(adj, start, end):
    # DFS to find heaviest edge on path
    stack = [(start, -1, None, -1)]
    visited = set()
    while stack:
        node, parent, heavy_edge, heavy_weight = stack.pop()
        if node == end:
            return heavy_edge
        visited.add(node)
        for nxt, w in adj[node]:
            if nxt == parent:
                continue
            if nxt in visited:
                continue
            if w > heavy_weight:
                new_edge = (node, nxt, w)
                new_w = w
            else:
                new_edge = heavy_edge
                new_w = heavy_weight
            stack.append((nxt, node, new_edge, new_w))
    return None

def udpatetree(n, tree_edges, u, v, new_w):
    # build adjacency of current MST
    adj = build_tree_adj(n, tree_edges)
    # case 1; updated edge (u,v) already part of the mst 
    for i, (a, b, w) in enumerate(tree_edges):
        if (a == u and b == v) or (a == v and b == u):
            tree_edges[i] = (a, b, new_w)
            return tree_edges     
    #case 2; edge (u,v) is not in the mst 
    # find heaviest edge on the path between u and v 
    heavy = find_heaviest_on_path(adj, u, v)
    if heavy is None: #if none found just return unchanged 
        return tree_edges
    hx, hy, hw = heavy
    # if new weight not improving
    if new_w >= hw:
        return tree_edges
    # replace heavy with new edge
    new_tree = []
    removed = False
    for a, b, w in tree_edges:
        #remove only the correct heavy edge once
        if not removed and ((a == hx and b == hy and w == hw) or (a == hy and b == hx and w == hw)):
            removed = True
            continue
        new_tree.append((a, b, w))
    new_tree.append((u, v, new_w))
    return new_tree

if __name__ == "__main__":
    # input: n, m edges of mst, then update edge and new weight
    import sys
    data = sys.stdin.read().strip().split()
    idx = 0

    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1

    tree_edges = []
    for _ in range(m):
        a = int(data[idx]); b = int(data[idx+1]); w = int(data[idx+2])
        idx += 3
        tree_edges.append((a, b, w))

    u = int(data[idx]); v = int(data[idx+1]); new_w = int(data[idx+2])

    updated = udpatetree(n, tree_edges, u, v, new_w)

    for e in updated:
        print(e[0], e[1], e[2])
