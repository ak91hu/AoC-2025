def solve():
    points = []
    
    with open('input.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            x, y = map(int, line.split(','))
            points.append((x, y))

    max_area = 0
    n = len(points)

    for i in range(n):
        for j in range(i + 1, n):
            p1 = points[i]
            p2 = points[j]

            width = abs(p1[0] - p2[0]) + 1
            height = abs(p1[1] - p2[1]) + 1
            area = width * height
            
            if area > max_area:
                max_area = area

    print(f"Largest area: {max_area}")

if __name__ == "__main__":
    solve()
