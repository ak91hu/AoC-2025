import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import LogNorm
import numpy as np
import os

def visualize_tachyon_manifold(filename):
    if not os.path.exists(filename):
        print(f"Error: {filename} not found.")
        return

    with open(filename, 'r') as f:
        raw_lines = [line.rstrip('\n') for line in f if line.strip()]

    if not raw_lines:
        return

    width = max(len(line) for line in raw_lines)
    height = len(raw_lines)
    
    grid_lines = [line.ljust(width, '.') for line in raw_lines]

    simulation_grid = np.zeros((height, width), dtype=np.float64)

    found_start = False
    for c in range(width):
        if grid_lines[0][c] == 'S':
            simulation_grid[0, c] = 1.0
            found_start = True
            break
    
    if not found_start:
        return

    for r in range(height - 1):
        for c in range(width):
            val = simulation_grid[r, c]
            
            if val == 0:
                continue

            char = grid_lines[r][c]
            
            if char == '^':
                if c - 1 >= 0:
                    simulation_grid[r+1, c-1] += val
                if c + 1 < width:
                    simulation_grid[r+1, c+1] += val
            else:
                simulation_grid[r+1, c] += val

    fig, ax = plt.subplots(figsize=(10, 12), facecolor='#1e1e1e')
    ax.set_facecolor('#1e1e1e')
    ax.set_title("Quantum Tachyon Distribution", color='white', fontsize=14, pad=20)
    ax.axis('off')

    max_val = np.max(simulation_grid)
    cmap = plt.get_cmap('magma')
    
    im = ax.imshow(
        np.zeros((height, width)), 
        cmap=cmap, 
        norm=LogNorm(vmin=0.1, vmax=max_val if max_val > 0 else 1)
    )

    status_text = ax.text(0.02, 0.97, '', transform=ax.transAxes, color='#00ffcc', fontsize=12, fontweight='bold', fontfamily='monospace')

    def update(frame):
        current_view = np.copy(simulation_grid)
        if frame < height - 1:
            current_view[frame+1:, :] = 0
            
        im.set_data(current_view)
        
        active_now = np.sum(simulation_grid[frame, :])
        status_text.set_text(f"Active Timelines: {int(active_now):,}")
        return [im, status_text]

    ani = animation.FuncAnimation(
        fig, 
        update, 
        frames=range(height), 
        interval=40,
        blit=True, 
        repeat=False
    )

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    visualize_tachyon_manifold('input.txt')
