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
    num_components = n

    def find(i):
        if parent[i] != i:
            parent[i] = find(parent[i])
        return parent[i]

    def union(i, j):
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            parent[root_i] = root_j
            return True
        return False

    for _, u, v in edges:
        if union(u, v):
            num_components -= 1
            if num_components == 1:
                x1 = points[u][0]
                x2 = points[v][0]
                print(x1 * x2)
                return

if __name__ == "__main__":
    solve()
