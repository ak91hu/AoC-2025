import sys

sys.setrecursionlimit(200000)

lines = open("input.txt").read().strip().split("\n")
graph = {}

for line in lines:
    parts = line.split(":")
    node = parts[0].strip()
    if len(parts) > 1:
        neighbors = parts[1].strip().split()
    else:
        neighbors = []
    graph[node] = neighbors

memo = {}

def count_paths(start_node, end_node):
    if start_node == end_node:
        return 1
    if start_node not in graph:
        return 0
    
    key = (start_node, end_node)
    if key in memo:
        return memo[key]
    
    total = 0
    for neighbor in graph[start_node]:
        total += count_paths(neighbor, end_node)
    
    memo[key] = total
    return total

path1 = count_paths("svr", "dac") * count_paths("dac", "fft") * count_paths("fft", "out")
path2 = count_paths("svr", "fft") * count_paths("fft", "dac") * count_paths("dac", "out")

print(path1 + path2)
