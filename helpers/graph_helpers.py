
import io
from matplotlib import pyplot as plt
import networkx as nx


def visualize_topdown(G):
    pydot_graph = nx.drawing.nx_pydot.to_pydot(G)
    pydot_graph.set_rankdir("TB")
    pydot_graph.set("ordering", "out")
    png_data = pydot_graph.create_png()
    image = plt.imread(io.BytesIO(png_data), format="png")
    plt.figure(figsize=(10, 8))
    plt.imshow(image)
    plt.axis("off")
    plt.show()