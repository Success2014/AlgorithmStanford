__author__ = 'Neo'

import random
import copy
import time


def RandomEdge(graph):
    v1 = random.choice(graph.keys())
    v2 = random.choice(graph[v1])
    return v1, v2

def Karger(graph):
    numOfCrossEdges = []
    while len(graph) > 2:
        v1, v2 = RandomEdge(graph)
        for node in graph[v2]:
            if node != v1:
                graph[v1].append(node)
                graph[node].remove(v2)
                graph[node].append(v1)
        while v2 in graph[v1]:
            graph[v1].remove(v2)
        del graph[v2]
    for finalNode in graph.keys():
        numOfCrossEdges.append(len(graph[finalNode]))
    return numOfCrossEdges[0]

def CreateGraph(file):
    """
    :param file:
    :return: graph, a dictionary with key: node k, value: nodes connected to node k
    """
    fhand = open(file)
    graph = {}
    for line in fhand:
        tmp_lst = [int(s) for s in line.split()]
        graph[tmp_lst[0]] = tmp_lst[1:]
    return graph

def simulation(times, graph):
    minCut = 100000000
    for i in range(times):
        sim_graph = copy.deepcopy(graph)
        num = Karger(sim_graph)
        if num < minCut:
            minCut = num
    return minCut

#graph = CreateGraph('test1.txt')
start = time.time()
graph = CreateGraph('kargerMinCut.txt')
mincut = simulation(1600,graph)

print mincut


print time.time() - start








