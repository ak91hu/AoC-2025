def solve():
    points = []
    with open('input.txt', 'r') as f:
        for line in f:
            if line.strip():
                points.append(tuple(map(int, line.strip().split(','))))

    edges = []
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            p1 = points[i]
            p2 = points[j]
            dist_sq = (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2
            edges.append((dist_sq, i, j))

    edges.sort(key=lambda x: x[0])

    parent = list(range(n))

    def find(i):
        if parent[i] != i:
            parent[i] = find(parent[i])
        return parent[i]

    def union(i, j):
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            parent[root_i] = root_j

    limit = 1000
    for k in range(limit):
        _, u, v = edges[k]
        union(u, v)

    groups = {}
    for i in range(n):
        root = find(i)
        groups[root] = groups.get(root, 0) + 1

    sizes = sorted(groups.values(), reverse=True)
    
    result = sizes[0] * sizes[1] * sizes[2]
    print(result)

if __name__ == "__main__":
    solve()
