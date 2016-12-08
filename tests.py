import networkx as nx
import matplotlib.pyplot as plt
import graph


def testing():
    G = nx.DiGraph()
    G.add_node('0', time=0)
    G.add_node('a', time=5)
    G.add_node('b', time=3)
    G.add_node('c', time=4)
    G.add_node('d', time=6)
    G.add_node('e', time=4)
    G.add_node('f', time=3)
    G.add_edge('0', 'a')
    G.add_edge('a', 'b')
    G.add_edge('0', 'c')
    G.add_edge('a', 'd')
    G.add_edge('e', 'd')
    G.add_edge('b', 'f')
    G.add_edge('c', 'f')
    G.add_edge('d', 'f')

    nx.set_node_attributes(G, 't1', 0)
    nx.set_node_attributes(G, 't2', 0)
    nx.set_node_attributes(G, 'luz', 0)
    nx.set_node_attributes(G, 'from', 0)
    #graph.CPM(G)
    pos = nx.spring_layout(G, k=5)

    nx.draw_networkx(G, pos, with_labels=True)

    edge_labels = nx.get_edge_attributes(G, 'weight')
    print(edge_labels)
    nx.draw_networkx_edge_labels(G, pos, labels=edge_labels)
    #nx.draw_networkx_nodes(G, pos, nodelist=sciezka_krytyczna, node_color='b', node_size=1600)

    plt.show()

if __name__ == '__main__':
    testing()