import networkx as nx
import matplotlib.pyplot as plt

# ================================= algorytm przechodzenia grafu po najdłuższych ścieżkach ======================================
# po drodze uzupełniam wartości 't1'

def CPM(G):
    unvisited = nx.topological_sort(G) # lista wierzchołków do odwiedzenia
    while unvisited:  # pętla dopóki jest coś nieodwiedzonego
        node = unvisited[0]  # biorę kolejne nieodwiedzone wierchołki
        for successor in G.successors_iter(node):  # iteracja po sąsiadach noda
            time = G.node[successor]['time']  # waga krawedzi miedzy wierzchołkami
            full_time = G.node[node]['t1']  # droga od początku grafu do wierzchołka który jest rozpatrywany
            sum_of_times = time + full_time
            if G.node[successor]['t1'] < sum_of_times:  # przypisuję najgorszą drogę
                G.node[successor]['t1'] = sum_of_times
                G.node[successor]['from'] = node  # zaznaczam z którego wierzchołka była najgorsza droga, potrzebne do ścieżki krytycznej
        if G.out_degree(node) == 0:
            for predecessor in G.predecessors(node):
                time = G.node[node]['time']
                full_time = G.node[predecessor]['t1']
                sum_of_times = time + full_time
                if G.node[node]['t1'] < sum_of_times:
                    G.node[node]['t1'] = sum_of_times
                    G.node[node]['t2'] = sum_of_times
                    G.node[node]['from'] = predecessor
        unvisited.remove(unvisited[0])
#================================================================================
    unvisited = nx.topological_sort(G).reverse()
    while unvisited:
        node = unvisited[0]

    # ========================================= znajduję koniec grafu ================================
    # czyli node z najwiekszym t1
    max = 0
    last_node = nx.nodes(G)[0]
    for node in G.nodes_iter():
        if G.node[node]['t1'] > max:
            max = G.node[node]['t1']
            last_node = node

        # ======================================== idę od końca i buduję ścieżkę krytyczną ==========================
    sciezka_krytyczna = []
    sciezka_krytyczna.append(last_node)
    while 1:
        sciezka_krytyczna.append(G.node[last_node]['from'])
        last_node = G.node[last_node]['from']
        if G.node[last_node]['from'] == 0:
            break
    sciezka_krytyczna.reverse()
    # ====================================== rysowanko grafu ============================================
    pos = nx.spring_layout(G)

    nx.draw_networkx(G, pos, with_labels=True, node_size=1600)

    nx.draw_networkx_nodes(G, pos, nodelist=sciezka_krytyczna, node_color='y', node_size=2000)

    for key, value in pos.items():
        value[0] += 0.03
    node_labels = nx.get_node_attributes(G, 't2')
    nx.draw_networkx_labels(G, pos, labels=node_labels)

    for key, value in pos.items():
        value[0] -= 0.06
    node_labels = nx.get_node_attributes(G, 't1')
    nx.draw_networkx_labels(G, pos, labels=node_labels)

    for key, value in pos.items():
        value[0] += 0.03
        value[1] += 0.03
    node_labels = nx.get_node_attributes(G, 'luz')
    nx.draw_networkx_labels(G, pos, labels=node_labels)


    plt.title(sciezka_krytyczna)
    plt.show()
