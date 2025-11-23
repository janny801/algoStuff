
# Topological sort for a DAG (Kahn's algorithm)
def topo_sort(n, graph, indegree):
    from collections import deque
    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)

    return order

# determine if a dag is semi connected
def isSemiConnected(n, graph, indegree):
    order = topo_sort(n, graph, indegree) #external func; order topologically 

    # check if there exists any direct path from u-> v
        #iterative dfs (no rec)
    def reach(u, v):
        stack = [u]
        visited = set([u])
        while stack:
            x = stack.pop()
            if x == v:
                return True
            for nxt in graph[x]:
                if nxt not in visited:
                    visited.add(nxt)
                    stack.append(nxt)
        return False

    # condition for dag to be semi connected
    for i in range(len(order) - 1):
        u = order[i]
        v = order[i + 1]
        if not reach(u, v):#one pair fails-> graph is not semi connected
            return False

    return True


if __name__ == "__main__":
    n = int(input().strip())

    graph = [[] for _ in range(n+1)]
    indegree = [0] * (n+1)

    for _ in range(n):
        parts = list(map(int, input().split()))
        u = parts[0]
        k = parts[1]
        for v in parts[2:2+k]:
            graph[u].append(v)
            indegree[v] += 1

    print(isSemiConnected(n, graph, indegree))
