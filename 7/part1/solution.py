import os

def solve_tachyon_puzzle(filename):
    if not os.path.exists(filename):
        print(f"Error: {filename} not found.")
        return

    try:
        with open(filename, 'r') as f:
            grid = [line.rstrip('\n') for line in f if line.strip()]
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return

    if not grid:
        print("Error: The input file is empty.")
        return

    active_beams = set()
    first_row = grid[0]
    if 'S' in first_row:
        active_beams.add(first_row.index('S'))
    else:
        print("Error: Starting point 'S' not found in the first row.")
        return

    total_splits = 0

    for row_str in grid:
        next_beams = set()
        
        for x in active_beams:
            if x < 0 or x >= len(row_str):
                continue
                
            char = row_str[x]
            
            if char == 'S' or char == '.':
                next_beams.add(x)
                
            elif char == '^':
                total_splits += 1
                next_beams.add(x - 1)
                next_beams.add(x + 1)
        active_beams = next_beams

        if not active_beams:
            break

    print(f"File processed: {filename}")
    print(f"Total split count: {total_splits}")

if __name__ == "__main__":
    solve_tachyon_puzzle('input.txt')
