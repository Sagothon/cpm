import networkx as nx
import matplotlib.pyplot as plt

# ===================== GRAF ==============================
def createGraph(G):
    nx.set_node_attributes(G, 't1', 0)
    nx.set_node_attributes(G, 't2', 0)
    nx.set_node_attributes(G, 'luz', 0)
    nx.set_node_attributes(G, 'from', 0)


def add_Edge(G, fro, to, weigh):
    G.add_edge(fro, to, weight=weigh)
    print(fro, to, weigh)


# ================================= algorytm przechodzenia grafu po najdłuższych ścieżkach ======================================
# po drodze uzupełniam wartości 't1'

def PERT(G):
    visited = []  # lista odwiedzonych wierzchołków  
    unvisited = nx.topological_sort(G) # lista wierzchołków do odwiedzenia
    while unvisited:  # pętla dopóki jest coś nieodwiedzonego
        node = unvisited[0]  # biorę kolejne nieodwiedzone wierchołki
        for successor in G.successors_iter(node):  # iteracja po sąsiadach noda
            waga = G.edge[node][successor]['weight']  # waga krawedzi miedzy wierzchołkami
            droga = G.node[node]['t1']  # droga od początku grafu do wierzchołka który jest rozpatrywany
            suma_droga_waga = droga + waga
            if G.node[successor]['t1'] < suma_droga_waga:  # przypisuję najgorszą drogę
                G.node[successor]['t1'] = suma_droga_waga
                G.node[successor][
                    'from'] = node  # zaznaczam z którego wierzchołka była najgorsza droga, potrzebne do ścieżki krytycznej

        visited.append(unvisited[0])  # przerzucam odwiedzone wierzchołki
        unvisited.remove(unvisited[0])

    # ========================================= znajduję koniec grafu ================================
    # czyli node z najwiekszym t1
    max = 0
    last_node = G.node[1]
    for node in G.nodes_iter():
        if G.node[node]['t1'] > max:
            max = G.node[node]['t1']
            last_node = G.node[node]

        # ======================================== idę od końca i buduję ścieżkę krytyczną ==========================
    sciezka_krytyczna = []
    while 1:
        sciezka_krytyczna.append(last_node['from'])
        last_node = G.node[last_node['from']]
        if last_node['from'] == 0:
            break
    sciezka_krytyczna.reverse()
    print(sciezka_krytyczna)

    # ====================================== rysowanko grafu ============================================
    pos = nx.spring_layout(G)

    nx.draw(G, pos, with_labels=True)
    # node_labels = nx.get_node_attributes(G,'t1')
    # nx.draw_networkx_labels(G, pos, labels = node_labels)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, labels=edge_labels)
    nx.draw_networkx_nodes(G, pos,
                           nodelist=sciezka_krytyczna,
                           node_color='b',
                           node_size=500,
                           alpha=0.8)

    plt.show()
