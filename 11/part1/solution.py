import sys

sys.setrecursionlimit(100000)

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

def get_paths(node):
    if node == "out":
        return 1
    if node not in graph:
        return 0
    if node in memo:
        return memo[node]
    
    total = 0
    for neighbor in graph[node]:
        total += get_paths(neighbor)
    
    memo[node] = total
    return total

print(get_paths("you"))
