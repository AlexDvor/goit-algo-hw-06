import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

edges = [
    ("A", "B", 2),
    ("A", "C", 5),
    ("B", "C", 1),
    ("B", "D", 3),
    ("C", "D", 2),
    ("C", "E", 3),
    ("D", "E", 1),
]

G.add_weighted_edges_from(edges)

pos = nx.spring_layout(G)
edge_labels = nx.get_edge_attributes(G, "weight")

nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=700)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title("Граф з вагами")
plt.show()

source_node = "A"

distances = nx.single_source_dijkstra_path_length(G, source_node)

paths = nx.single_source_dijkstra_path(G, source_node)

print(f"\nНайкоротші відстані від {source_node}:")
for target, distance in distances.items():
    print(f"{source_node} → {target}: {distance} (шлях: {paths[target]})")


"""
Ми використовуємо add_weighted_edges_from, щоб додати ребра з вагами.

nx.single_source_dijkstra_path_length — повертає відстані від початкової вершини до всіх інших.

nx.single_source_dijkstra_path — повертає самі найкоротші шляхи.


Алгоритм Дейкстри дозволяє ефективно знайти найкоротші шляхи у 
графах з невід’ємними вагами. Це ідеально підходить для задач таких як:

планування маршрутів,

аналіз мереж (транспортних, комп’ютерних),

пошук оптимальних шляхів.
"""
