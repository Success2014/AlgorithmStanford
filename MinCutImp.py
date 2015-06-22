__author__ = 'Neo'

import random
import copy
import time


def CreateGraph(file):
    """
    :param file:
    :return: graph, a list of tuples
    """
    fhand = open(file)
    graph = []
    numOfNode = 0
    for line in fhand:
        numOfNode += 1
        tmp_lst = [int(s) for s in line.split()]
        for j in tmp_lst[1:]:
            if j > tmp_lst[0]:
                graph.append((tmp_lst[0] - 1, j - 1)) # Python index starts from 0
    return graph, numOfNode

def Karger(graph, numOfNode):
    """
    :param graph:
    :return: a list nodeRship, with nodeRship[i] = i-th node's grandparent
    """

    nodeRship = list(range(numOfNode)) # initially every node points to itself
    nodeSz = [1] * numOfNode # initially every node only has itself, has no offsprings
    graphToWork = copy.deepcopy(graph)
    random.shuffle(graphToWork) # shuffle edges

    # for itr in range(numOfNode - 2): # do contraction numofNode - 2 times, then you'll have only two nodes
    #     edgeToContract = random.choice(graphToWork) # randomly choose an edge, a tuple e.g. (3,4)
    #
    #     node0 = edgeToContract[0] # index of the first node
    #     node0Root = findRoot(nodeRship,node0)
    #     node1 = edgeToContract[1]
    #     node1Root = findRoot(nodeRship,node1)
    #     if nodeSz[node0Root] >= nodeSz[node1Root]: # if the size of the first node is greater than the second node
    #         nodeRship[node1Root] = node0Root
    #         nodeSz[node0Root] += nodeSz[node1Root]
    #     else:
    #         nodeRship[node0Root] = node1Root
    #         nodeSz[node1Root] += nodeSz[node0Root]
    #     while edgeToContract in graphToWork:
    #         graphToWork.remove(edgeToContract) # error here, needs to remove all the edge with the same root, time consuming

    itr = 0
    numContra = 0
    while numContra < (numOfNode - 2):
        edgeToContract = graphToWork[itr]
        node0 = edgeToContract[0] # index of the first node
        node0Root = findRoot(nodeRship,node0)
        node1 = edgeToContract[1]
        node1Root = findRoot(nodeRship,node1)
        if node0Root != node1Root:
            if nodeSz[node0Root] >= nodeSz[node1Root]: # if the size of the first node is greater than the second node
                nodeRship[node1Root] = nodeRship[node0Root]
                nodeSz[node0Root] += nodeSz[node1Root]
            else:
                nodeRship[node0Root] = nodeRship[node1Root]
                nodeSz[node1Root] += nodeSz[node0Root]
            numContra += 1
        itr += 1
    return nodeRship

def findRoot(nodeRship, node):
    """
    :param nodeRship:
    :param node: integer
    :return: the root of a node
    """
    while nodeRship[node] != node:
        node = nodeRship[node]
    return node

def countMinCut(graph, nodeRship):
    result = 0
    for edge in graph:
        if nodeRship[findRoot(nodeRship,edge[0])] != nodeRship[findRoot(nodeRship,edge[1])]:
            result += 1
    return result

def simulation(times, graph, numOfNode) :
    minCut = 100000000

    for i in range(times):
        #sim_graph = copy.deepcopy(graph)
        nodeRship = Karger(graph,numOfNode)
        num = countMinCut(graph, nodeRship)
        if num < minCut:
            minCut = num
    return minCut



start = time.time()
#graph,numOfNode = CreateGraph("E:/PrWS/Py/AlgI/test1.txt")
graph,numOfNode = CreateGraph("E:/PrWS/Py/AlgI/kargerMinCut.txt")
mincut = simulation(1000,graph, numOfNode)

print mincut

print 'TIME RUNNING: ',time.time() - start, 'SECONDS'








