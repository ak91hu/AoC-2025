import re
import tkinter as tk
from tkinter import filedialog

def solve_part_two():
    root = tk.Tk()
    root.withdraw()
    
    file_path = filedialog.askopenfilename(
        title="Select Puzzle Input (aoc1.txt)",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not file_path: return

    with open(file_path, 'r') as f:
        content = f.read()

    instructions = re.findall(r'[LR]\d+', content)
    
    current_pos = 50
    total_zeros = 0
    
    for instruction in instructions:
        direction = instruction[0]
        distance = int(instruction[1:])
        
        if direction == 'R':
            # Count how many multiples of 100 are in the range (current, current + distance]
            zeros = (current_pos + distance) // 100 - current_pos // 100
            total_zeros += zeros
            current_pos = (current_pos + distance) % 100
            
        elif direction == 'L':
            # Count how many multiples of 100 are in range [current - distance, current - 1]
            upper_bound = current_pos - 1
            lower_bound = current_pos - distance
            
            # Doing math to count multiples in a range [A, B]: floor(B/100) - floor((A-1)/100)
            zeros = upper_bound // 100 - (lower_bound - 1) // 100
            total_zeros += zeros
            current_pos = (current_pos - distance) % 100
            
    return total_zeros

if __name__ == "__main__":
    print(f"Part 2 Password: {solve_part_two()}")
