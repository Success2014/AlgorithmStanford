import sys

sys.setrecursionlimit(1000000)

def creategraph(filename, numofnode):
    """

    :param filename:
    :param numofnode:
    :return: a graph dictionary of lists
    """
    fhand = open(filename)
    graph =  {}
    for i in range(numofnode):
        graph[i] = []
    for line in fhand:
        tmp_list = [int(s) - 1 for s in line.split()]
        #graph[tmp_list[0]] = graph.get(tmp_list[0],[])
        graph[tmp_list[0]] += tmp_list[1:]
    return graph

def DFS_F(graph, node, leader):
    """

    :param graph:
    :param node:
    :param leader:
    :return:
    """
    global nodeExplored, nodeLeader, finishingTime, t, finishingTime
    if nodeExplored[node] == 0:
        nodeExplored[node] = 1
    #nodeLeader[node] = leader

    for edge in graph[node]:
        if nodeExplored[edge] == 0:
            DFS_F(graph, edge, node)

    t += 1
    finishingTime[node] = t
    return

def DFS_S(graph, node, currentLeader):
    """

    :param graph:
    :param node:
    :param leader:
    :return:
    """
    global nodeExplored, nodeLeader, finishingTime, t, finishingTime
    if nodeExplored[node] == 0:
        nodeExplored[node] = 1
    nodeLeader[node] = currentLeader

    for edge in graph[node]:
        if nodeExplored[edge] == 0:
            DFS_S(graph, edge, currentLeader)

    return

def DFSLoop_F(graph, numofnode, nodeExplored):
    """

    :param graph:
    :return:
    """
    for i in range(numofnode - 1, -1, -1):
        if nodeExplored[i] == 0:
            DFS_F(graph, i, i)

def DFSLoop_S(graph, numofnode, nodeExplored, finishingTime):
    """

    :param graph:
    :param numofnode:
    :param nodeExplored:
    :param finishingTime:
    :return:
    """
    while sum(nodeExplored) < numofnode:
        node = finishingTime.index(max(finishingTime))
        finishingTime[node] = 0
        if nodeExplored[node] == 0:
            currentLeader = node
            DFS_S(graph, node, currentLeader)

def createrevgraph(graph, numofnode):
    """

    :param graph:
    :return: return a reverse graph
    """
    revgraph = {}
    for i in range(numofnode):
        revgraph[i] = []
    for key, item in graph.items():
        for eachitem in item:
            revgraph[eachitem].append(key)
    return revgraph


numofnode = 8
graph = creategraph('test1.txt',numofnode)
revgraph = createrevgraph(graph, numofnode)
#print graph
#print revgraph


nodeExplored = [0] * numofnode
nodeLeader  = [0] * numofnode
t = 0 # global time counter
finishingTime = [0] * numofnode

DFSLoop_F(revgraph,numofnode,nodeExplored)
#print finishingTime


nodeExplored = [0] * numofnode
nodeLeader = [0] * numofnode
DFSLoop_S(graph,numofnode,nodeExplored,finishingTime)
print nodeLeader

SCC = {}
for j in range(numofnode):
    SCC[nodeLeader[j]] = SCC.get(nodeLeader[j],0)
    SCC[nodeLeader[j]] += 1
print SCC
