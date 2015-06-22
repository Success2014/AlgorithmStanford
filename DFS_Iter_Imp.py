__author__ = 'Neo'
import time

def creategraph(filename, numofnode):
    """

    :param filename:
    :param numofnode:
    :return: graph and revgraph: dictionary of lists
    """
    fhand = open(filename)
    graph = {}
    revgraph = {}
    for i in xrange(numofnode):
        graph[i] = []
        revgraph[i] = []
    for line in fhand:
        tmp_list = [int(s) - 1 for s in line.split()]
        #graph[tmp_list[0]] = graph.get(tmp_list[0],[])
        #graph[tmp_list[0]] += tmp_list[1:]
        #revgraph[tmp_list[1]] += tmp_list[0:1]
        graph[tmp_list[0]].append(tmp_list[1])
        revgraph[tmp_list[1]].append(tmp_list[0])
    return graph, revgraph

def DFS_Loop(graph, numofnode):
    """

    :param graph:
    :param numofnode:
    :return:
    """
    global explored, state, leader, t, f
    t = 0
    # state = [0] * numofnode # 0-new, 1-started, 2-done
    # leader = [None] * numofnode
    # explored = [0] * numofnode # 0-unexplored, 1-explored
    # f = [0] * numofnode # finishing time of each node
    state = {}
    for i in xrange(numofnode):
        state[i] = 0
    leader = {}
    for i in xrange(numofnode):
        leader[i] = None
    explored ={}
    for i in xrange(numofnode):
        explored[i] = 0
    f = {}
    for i in xrange(numofnode):
        f[i] = 0



    for i in range(numofnode - 1, -1, -1):
        if explored[i] == 0:
            s = i
            DFS(graph, i, s)
    return f, leader


def DFS(graph, node, lead):
    global explored, state, leader, t, f
    stack  = []
    stack.append(node)
    while (not stack == []):
        v = stack.pop()
        if state[v] == 0:
            state[v] = 1
            explored[v] = 1
            leader[v] = lead
            stack.append(v)
            for edge in graph[v]:
                if explored[edge] == 0:
                    stack.append(edge)
        elif state[v] == 1:
            t += 1
            f[v] = t
            state[v] = 2
        #else:

    return leader,f

def DFS_Loop_S(graph, numofnode, finishingTime):
    """

    :param graph:
    :param numofnode:
    :param finishingTime:
    :return:
    """
    global explored, state, leader

    state = [0] * numofnode # 0-new, 1-started, 2-done
    leader = [None] * numofnode
    explored = [0] * numofnode # 0-unexplored, 1-explored

    finishingtime_rev = {}
    for key,value in finishingtime.items():
        finishingtime_rev[value] = key
    for i in range(numofnode, 0, -1):
        node = finishingtime_rev[i]
        if explored[node] == 0:
            currentLeader = node
            DFS_S(graph, node, currentLeader)
    return leader




def DFS_S(graph, node, lead):
    global explored, state, leader
    stack  = []
    stack.append(node)
    while (not stack == []):
        v = stack.pop()
        if state[v] == 0:
            state[v] = 1
            explored[v] = 1
            leader[v] = lead
            stack.append(v)
            for edge in graph[v]:
                if explored[edge] == 0:
                    stack.append(edge)
        elif state[v] == 1:
            state[v] = 2
        #else:

    return leader


start = time.time()
numofnode = 875714
#numofnode = 8
graph,revgraph = creategraph('SCC.txt',numofnode)
finishingtime,leader = DFS_Loop(revgraph,numofnode)
nodeLeader = DFS_Loop_S(graph,numofnode,finishingtime)
#print finishingtime
#print nodeLeader
SCC = {}
for j in range(numofnode):
    SCC[nodeLeader[j]] = SCC.get(nodeLeader[j],0)
    SCC[nodeLeader[j]] += 1
#print SCC
countSCC = SCC.values()
if len(countSCC) < 5:
    print countSCC
else:
    for i in range(5):
        print max(countSCC)
        countSCC.remove(max(countSCC))

print 'TIME RUNNING: ',time.time() - start, 'SECONDS'