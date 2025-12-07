import os
from collections import defaultdict

def solve_quantum_tachyon_puzzle(filename):
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
      
    active_timelines = defaultdict(int)
    
    start_row = grid[0]
    if 'S' in start_row:
        active_timelines[start_row.index('S')] = 1
    else:
        print("Error: Start 'S' not found in the first row.")
        return

    for row_idx, row_str in enumerate(grid):
        next_timelines = defaultdict(int)
        for col, count in active_timelines.items():
            if 0 <= col < len(row_str):
                char = row_str[col]
            else:
                char = '.'
            if char == '^':
                next_timelines[col - 1] += count
                next_timelines[col + 1] += count
            else:
                next_timelines[col] += count
        
        active_timelines = next_timelines
        
        if not active_timelines:
            break

    total_timelines = sum(active_timelines.values())
    print(f"Total Active Timelines: {total_timelines}")

if __name__ == "__main__":
    solve_quantum_tachyon_puzzle('input.txt')
