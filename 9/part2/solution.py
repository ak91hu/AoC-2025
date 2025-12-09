def solve_part_two():
    points = []
    try:
        with open('input.txt', 'r') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                x, y = map(int, line.split(','))
                points.append((x, y))
    except FileNotFoundError:
        print("Error: 'input.txt' not found. Please create the file with your puzzle input.")
        return

    n = len(points)
    
    def is_in_poly(x, y):
        inside = False
        for i in range(n):
            v1, v2 = points[i], points[(i + 1) % n]
            if v1[0] == v2[0] == x:
                if min(v1[1], v2[1]) <= y <= max(v1[1], v2[1]):
                    return True
            if v1[1] == v2[1] == y:
                if min(v1[0], v2[0]) <= x <= max(v1[0], v2[0]):
                    return True
            if (v1[1] > y) != (v2[1] > y):
                if v1[0] > x:
                    inside = not inside
                    
        return inside

    def is_valid_rect(p1, p2):
        x1, x2 = min(p1[0], p2[0]), max(p1[0], p2[0])
        y1, y2 = min(p1[1], p2[1]), max(p1[1], p2[1])
        
        if not is_in_poly(x1, y2): return False
        if not is_in_poly(x2, y1): return False
        
        cx, cy = (x1 + x2) / 2, (y1 + y2) / 2
        if not is_in_poly(cx, cy): return False
        
        for i in range(n):
            vx1, vy1 = points[i]
            vx2, vy2 = points[(i + 1) % n]

            if vx1 == vx2:
                if x1 < vx1 < x2:
                    ey_min, ey_max = min(vy1, vy2), max(vy1, vy2)
                    if max(y1, ey_min) < min(y2, ey_max):
                        return False
            else: 
                if y1 < vy1 < y2:
                    ex_min, ex_max = min(vx1, vx2), max(vx1, vx2)
                    if max(x1, ex_min) < min(x2, ex_max):
                        return False
                        
        return True
      
    candidates = []
    for i in range(n):
        for j in range(i + 1, n):
            p1 = points[i]
            p2 = points[j]
            # Calculate Area
            w = abs(p1[0] - p2[0]) + 1
            h = abs(p1[1] - p2[1]) + 1
            area = w * h
            candidates.append((area, p1, p2))
    candidates.sort(key=lambda x: x[0], reverse=True)
    
    print(f"Checking {len(candidates)} candidate rectangles...")

    for area, p1, p2 in candidates:
        if is_valid_rect(p1, p2):
            print("-" * 30)
            print(f"Largest Valid Area: {area}")
            print(f"Corners: {p1} and {p2}")
            return

if __name__ == "__main__":
    solve_part_two()
