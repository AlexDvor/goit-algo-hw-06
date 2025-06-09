import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_nodes_from(["A", "B", "C", "D", "E"])

G.add_edges_from([("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("D", "E")])

plt.figure(figsize=(6, 4))
nx.draw(
    G,
    with_labels=True,
    node_color="lightblue",
    edge_color="gray",
    node_size=1500,
    font_size=14,
)
plt.title("Транспортна мережа міста")
plt.show()

print(f"Кількість районів (вузлів): {G.number_of_nodes()}")
print(f"Кількість доріг (ребер): {G.number_of_edges()}")

print("\nСтупінь кожного вузла:")
for node, degree in G.degree():
    print(f"{node}: {degree}")
