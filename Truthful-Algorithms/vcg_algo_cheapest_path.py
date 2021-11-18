import doctest
from copy import copy

import networkx as nx



def vcg_cheapest_path(graph, source, target):
    """
    The function finds  cheapest path from source to target,
    and calculates for each edge in the graph the cost, according the vcg algorithm.
    :param graph: a networkx weighted graph.
    :param source -the source node.
    :param target - the target node.
   >>> G = nx.Graph()
   >>> G.add_edge('a', 'b', weight=3)
   >>> G.add_edge('b', 'd', weight=4)
   >>> G.add_edge('c', 'd', weight=1)
   >>> G.add_edge('d', 'a', weight=10)
   >>> G.add_edge('a', 'c', weight=5)
   >>> G.add_edge('b', 'c', weight=1)
   >>> vcg_cheapest_path(G,'a','d')
   [('a', 'b', {'weight': 3}), ('a', 'd', {'weight': 10}), ('a', 'c', {'weight': 5}), ('b', 'd', {'weight': 4}), ('b', 'c', {'weight': 1}), ('d', 'c', {'weight': 1})]
   {'ab': 4, 'ad': 0, 'ac': 0, 'bd': 0, 'bc': 2, 'dc': 3}

   >>> G = nx.Graph()
   >>> G.add_edge('a', 'b', weight=3)
   >>> G.add_edge('b', 'd', weight=4)
   >>> G.add_edge('c', 'd', weight=1)
   >>> G.add_edge('a', 'c', weight=5)
   >>> vcg_cheapest_path(G,'b','c')
   [('a', 'b', {'weight': 3}), ('a', 'c', {'weight': 5}), ('b', 'd', {'weight': 4}), ('d', 'c', {'weight': 1})]
   {'ab': 0, 'ac': 0, 'bd': 7, 'dc': 4}
   """

    # Find the shortest path and length in the graph
    lenP, shortP = nx.single_source_dijkstra(graph, source, target)
    edges = graph.edges(data=True)
    print(edges)
    tempGraph = graph.copy()
    allCosts = {}
    for u, v, w in edges:
        edgeW = w.get('weight')
        tempGraph.remove_edge(u, v)
        # Find the new shortest path without the current edge
        newLen, newPath = nx.single_source_dijkstra(tempGraph, source, target)
        tempGraph.add_edge(u, v, weight=edgeW)

        # If the original shortest path goes through the current edge
        if shortP != newPath:
            # Calculate the new cost
            cost = newLen - (lenP - edgeW)
        # There is no change in the cost
        else:
            cost = 0

        allCosts[str(u+v)] = cost

    print(allCosts)


if __name__ == '__main__':
    (failures, tests) = doctest.testmod(report=True, verbose=True)
    print("{} failures, {} tests".format(failures, tests))
