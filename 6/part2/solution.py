import math
from pathlib import Path

def solve_vertical_equations(file_path: str) -> int:
    input_path = Path(file_path)
    if not input_path.exists():
        print(f"Error: File {file_path} not found.")
        return 0

    with input_path.open("r") as f:
        grid = [list(line.rstrip('\n')) for line in f]

    total_result = 0
    current_numbers = []
    current_operator = "+"
    columns = list(zip(*grid))

    for col in columns:
        bottom_char = col[-1]
        if not bottom_char.isspace():
            current_operator = bottom_char

        col_content = "".join(col).strip("*+ ")

        if col_content:
            current_numbers.append(int(col_content))

        if not col_content and current_numbers:
            total_result += perform_calculation(current_numbers, current_operator)
            current_numbers.clear()

    if current_numbers:
        total_result += perform_calculation(current_numbers, current_operator)

    return total_result

def perform_calculation(numbers: list[int], operator: str) -> int:
    """Helper to dispatch math operations."""
    if operator == "+":
        return sum(numbers)
    elif operator == "*":
        return math.prod(numbers)
    return 0

if __name__ == "__main__":
    answer = solve_vertical_equations("input/day06.txt")
    print(f"Part two answer: {answer}")
