import re
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds

def solve_machine_joltage(line):
    target_match = re.search(r'\{([\d,]+)\}', line)
    if not target_match:
        return 0
    
    targets = np.array([int(x) for x in target_match.group(1).split(',')], dtype=float)
    num_counters = len(targets)
    
    button_matches = re.findall(r'\(([\d,]+)\)', line)
    
    num_buttons = len(button_matches)
    A = np.zeros((num_counters, num_buttons))
    
    for col_idx, btn_str in enumerate(button_matches):
        indices = [int(x) for x in btn_str.split(',')]
        for row_idx in indices:
            if row_idx < num_counters:
                A[row_idx, col_idx] = 1
                
    c = np.ones(num_buttons)
    
    constraints = LinearConstraint(A, lb=targets, ub=targets)
    variable_bounds = Bounds(0, np.inf)
    
    res = milp(c=c, constraints=constraints, integrality=np.ones(num_buttons), bounds=variable_bounds)
    
    if res.success:
        return int(np.round(res.fun))
    else:
        return 0

def main():
    total_presses = 0
    
    try:
        with open('input.txt', 'r') as f:
            lines = f.readlines()
            
        for line in lines:
            if line.strip():
                total_presses += solve_machine_joltage(line)
                
        print(f"Total Minimum Presses: {total_presses}")
        
    except FileNotFoundError:
        print("Error: 'input.txt' not found.")

if __name__ == '__main__':
    main()
