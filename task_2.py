import networkx as nx
from collections import deque

G = nx.Graph()

G.add_nodes_from(["A", "B", "C", "D", "E"])

G.add_edges_from([("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("D", "E")])


def dfs_path(graph, start, goal, path=None, visited=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(start)
    path = path + [start]

    if start == goal:
        return path

    for neighbor in graph.neighbors(start):
        if neighbor not in visited:
            new_path = dfs_path(graph, neighbor, goal, path, visited)
            if new_path:
                return new_path
    return None


def bfs_path(graph, start, goal):
    visited = set()
    queue = deque([[start]])

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            for neighbor in graph.neighbors(node):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
            visited.add(node)
    return None


start_node = "A"
end_node = "E"

dfs_result = dfs_path(G, start_node, end_node)
bfs_result = bfs_path(G, start_node, end_node)

print(f"\nDFS шлях від {start_node} до {end_node}: {dfs_result}")
print(f"BFS шлях від {start_node} до {end_node}: {bfs_result}")


"""
DFS занурюється вглиб, може знайти шлях не найкоротший.

BFS перевіряє по колу — завжди знаходить найкоротший шлях у графі без ваги.

DFS шлях: A → C → D → E
BFS шлях: A → B → D → E 
"""
