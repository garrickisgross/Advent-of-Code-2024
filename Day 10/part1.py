from math import sqrt

with open("Day 10/input.txt") as file:
    data = file.read().strip().splitlines()

data = [[int(j) for j in x] for x in data]

class Node:
    value: int
    x: int
    y: int

    def __init__(self, value = 0, x = 0, y = 0):
        self.value = value | 0
        self.x = x | 0
        self.y = y | 0

class Graph:
    nodes: list[Node]
    edges: dict[Node, list[Node]]

    def __init__(self, nodes: list[Node], edges: dict[int, list[int]]):
        self.nodes = nodes
        self.edges = edges
    
    def degree(self, node: Node) -> int:
        return len(self.edges[node])
    
    
    def find_all_paths(self, start_value: int, end_value: int) -> list[list[Node]]:
        def dfs(current_node: Node, end_value: int, path: list[Node], all_paths: list[list[Node]]):
            if current_node.value == end_value:
                all_paths.append(path[:])
                return
            for neighbor in self.edges[current_node]:
                if neighbor not in path:
                    path.append(neighbor)
                    dfs(neighbor, end_value, path, all_paths)
                    path.pop()
        
        start_nodes = [node for node in self.nodes if node.value == start_value]
        all_paths = []
        for start_node in start_nodes:
            dfs(start_node, end_value, [start_node], all_paths)
        
        return all_paths
    
def build_graph(data: list[list[int]]) -> Graph:
    nodes = []
    edges = {}
    for i, row in enumerate(data):
        for j, value in enumerate(row):
            node = Node()
            node.value = value
            node.x = i
            node.y = j
            nodes.append(node)
            edges[node] = []
    
    for i, node in enumerate(nodes):
        for j, other_node in enumerate(nodes):
            if i != j:
                distance = sqrt((node.x - other_node.x)**2 + (node.y - other_node.y)**2)
                is_diagonal = abs(node.x - other_node.x) == 1 and abs(node.y - other_node.y) == 1
                if distance <= 1 and  node.value == other_node.value - 1 and not is_diagonal:
                    edges[node].append(other_node)    
    
    return Graph(nodes, edges)

graph = build_graph(data)
paths = graph.find_all_paths(0, 9)

trailheads = {}
for path in paths:
    if path[0] not in trailheads:
        trailheads[path[0]] = [path[-1]]
    else:
        if path[-1] not in trailheads[path[0]]:
            trailheads[path[0]].append(path[-1])

rating = {}
for path in paths:
    if path[0] not in rating:
        rating[path[0]] = 1
    else:
        rating[path[0]] += 1

trailhead_count = 0
rating_count = 0
for key, value in trailheads.items():
    trailhead_count += len(value)

for key, value in rating.items():
    rating_count += value


print(trailhead_count)
print(rating_count)
    



    

        