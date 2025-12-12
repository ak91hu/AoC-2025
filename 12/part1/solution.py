def count_hashes(shape_lines):
    count = 0
    for line in shape_lines:
        count += line.count('#')
    return count

def solve():
    shapes_area = {}
    current_id = None
    buffer = []
    
    with open('input.txt', 'r') as f:
        lines = [line.strip() for line in f if line.strip()]

    regions_lines = []
    for line in lines:
        if 'x' in line and ':' in line and not line.endswith(':'):
            if current_id is not None:
                shapes_area[current_id] = count_hashes(buffer)
                current_id = None
                buffer = []
            regions_lines.append(line)
        elif line.endswith(':'):
            if current_id is not None:
                shapes_area[current_id] = count_hashes(buffer)
                buffer = []
            current_id = int(line.replace(':', ''))
        else:
            buffer.append(line)

    if current_id is not None and buffer:
        shapes_area[current_id] = count_hashes(buffer)

    print("Shape areas:", shapes_area)

    success_count = 0
    
    for line in regions_lines:
        dims_part, counts_part = line.split(':')
        width_str, length_str = dims_part.split('x')
        
        region_area = int(width_str) * int(length_str)
        present_counts = list(map(int, counts_part.strip().split()))
        
        total_presents_area = 0
        for shape_id, quantity in enumerate(present_counts):
            total_presents_area += shapes_area[shape_id] * quantity
        if total_presents_area <= region_area:
            success_count += 1
        else:
            pass

    print(f"Total regions: {success_count}")

if __name__ == '__main__':
    solve()
