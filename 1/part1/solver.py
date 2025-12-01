import re
import tkinter as tk
from tkinter import filedialog

def solve_safe_password():
    root = tk.Tk()
    root.withdraw()

    print("Please select your 'aoc1.txt' file from the window...")
    
    file_path = filedialog.askopenfilename(
        title="Select Puzzle Input",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if not file_path:
        print("No file selected.")
        return
      
    with open(file_path, 'r') as f:
        content = f.read()

    instructions = re.findall(r'[LR]\d+', content)
    print(f"Processing {len(instructions)} rotations...")

    current_pos = 50  # Dial starts at 50
    password_count = 0
    
    for instruction in instructions:
        direction = instruction[0]      # First letter (L or R)
        distance = int(instruction[1:]) # The number following it
        
        if direction == 'R':
            # Add distance, wrap around 100
            current_pos = (current_pos + distance) % 100
        elif direction == 'L':
            # Subtract distance, wrap around 100
            current_pos = (current_pos - distance) % 100
            
        # Did we land on 0?
        if current_pos == 0:
            password_count += 1
            
    return password_count

if __name__ == "__main__":
    answer = solve_safe_password()
    if answer is not None:
        print("\n" + "="*30)
        print(f"ACCESS CODE: {answer}")
        print("="*30 + "\n")
