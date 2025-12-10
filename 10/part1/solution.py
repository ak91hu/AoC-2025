import collections
import re
import sys

def main():
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    total_presses = 0

    for line in lines:
        if not line.strip():
            continue

        diagram_match = re.search(r'\[([.#]+)\]', line)
        if not diagram_match:
            continue
        
        diagram = diagram_match.group(1)
        target_mask = 0
        for i, char in enumerate(diagram):
            if char == '#':
                target_mask |= (1 << i)

        buttons = []
        for btn_str in re.findall(r'\(([\d,]+)\)', line):
            mask = 0
            for x in btn_str.split(','):
                mask |= (1 << int(x))
            buttons.append(mask)

        queue = collections.deque([(0, 0)])
        visited = {0}
        solved = False

        while queue:
            current_state, depth = queue.popleft()

            if current_state == target_mask:
                total_presses += depth
                solved = True
                break

            for btn_mask in buttons:
                next_state = current_state ^ btn_mask
                if next_state not in visited:
                    visited.add(next_state)
                    queue.append((next_state, depth + 1))
        
        if not solved:
            print(f"Could not solve line: {line.strip()}")

    print(total_presses)

if __name__ == '__main__':
    main()
