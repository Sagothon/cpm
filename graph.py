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
            if G.node[successor]['t1'] == 0:
            	G.node[successor]['t1'] = sum_of_times
            	G.node[successor]['from'] = node
            elif G.node[successor]['t1'] < sum_of_times:  # przypisuję najgorszą drogę
                G.node[successor]['t1'] = sum_of_times
                G.node[successor]['from'] = node  # zaznaczam z którego wierzchołka była najgorsza droga, potrzebne do ścieżki krytycznej
        if G.out_degree() == 0:
        	gjfdg
        unvisited.remove(unvisited[0])

    # ========================================= znajduję koniec grafu ================================
    # czyli node z najwiekszym t1
    max = 0
    last_node = G.node['0']
    for node in G.nodes_iter():
        if G.node[node]['t1'] > max:
            max = G.node[node]['t1']
            last_node = G.node[node]

        # ======================================== idę od końca i buduję ścieżkę krytyczną ==========================
    sciezka_krytyczna = []
    #print(last_node)
    #sciezka_krytyczna.append(last_node)
    while 1:
        sciezka_krytyczna.append(last_node['from'])
        last_node = G.node[last_node['from']]
        if last_node['from'] == 0:
            break
    sciezka_krytyczna.reverse()
    print(sciezka_krytyczna)
    # ====================================== rysowanko grafu ============================================
    pos = nx.spring_layout(G)

    nx.draw_networkx(G, pos, with_labels=True, label='dfdd')

    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, labels=edge_labels)
    nx.draw_networkx_nodes(G, pos, nodelist=sciezka_krytyczna, node_color='b', node_size=1600)

    #for key, value in pos.items():
    #    value[0] += 0.02
    #node_labels = nx.get_node_attributes(G, 't2')
    #nx.draw_networkx_labels(G, pos, labels=node_labels)

    #for key, value in pos.items():
    #    value[0] -= 0.04
    #node_labels = nx.get_node_attributes(G, 't1')
    #nx.draw_networkx_labels(G, pos, labels=node_labels)

    #for key, value in pos.items():
    #    value[0] += 0.02
    #    value[1] += 0.02
    #node_labels = nx.get_node_attributes(G, 'luz')
    #nx.draw_networkx_labels(G, pos, labels=node_labels)


    plt.title(sciezka_krytyczna)
    plt.show()
