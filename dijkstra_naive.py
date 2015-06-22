import heapq
def creategraph(file):
    """

    :param file:
    :return:
    """
    fhand = open(file)
    graph = {}
    num_of_node = 0
    for line in fhand:
        tmp = line.split()
        num_of_node += 1
        graph[int(tmp[0]) - 1] = {}
        if len(tmp) > 1:
            for list_element in tmp[1:]:
                list_element_s = [int(x) for x in list_element.split(',')]
                graph[int(tmp[0]) - 1][list_element_s[0] - 1] = graph[int(tmp[0]) - 1].get(list_element_s[0] - 1,0)
                graph[int(tmp[0]) - 1][list_element_s[0] - 1] = list_element_s[1]
    return graph, num_of_node

def findCrossEdge(graph,processed_node_set):
    """
    find the crossing edges,tail is in pns, head is in upns
    :param graph:
    :param processed_node_set:
    :return: the crossing edges
    """
    edges_to_consider = []
    for pns in processed_node_set:
        [edges_to_consider.append((pns,node)) for node in graph[pns].keys() if ((pns, node) not in edges_to_consider) and ((node, pns) not in edges_to_consider) and (node not in processed_node_set)]
    return edges_to_consider # the first node must be in the processed_node_set

def buildHeap(graph, edges_to_consider, shortest_path):
    # size of the heap should be the number of nodes in unprocess node set, which have crossing edges
    current_heap = []
    length_edge_pair_dict = {} # key: node, value: minimun distance to nodes in process node set
    ###cross_edge_node = []
    for edge in edges_to_consider:
        ###cross_edge_node.append(edges_to_consider[1])
        tmp_length = graph[edge[0]][edge[1]] + shortest_path[edge[0]]
        heapq.heappush(current_heap, tmp_length)
        ###length_edge_pair_dict[(edge[0], edge[1])] = tmp_length
        length_edge_pair_dict[edge[1]] = tmp_length
    return current_heap, length_edge_pair_dict#, #cross_edge_node




def dijkstrashort(graph, num_of_node):
    # initialization
    processed_node_set = [0]
    unprocessed_node_set = range(1,num_of_node) # the set of nodes which haven't been processed
    shortest_path = [0] * num_of_node

    # find initial crossing edges and
    crossing_edges = findCrossEdge(graph, [0])
    current_heap, length_edge_pair_dict = buildHeap(graph, crossing_edges, shortest_path) # heap is the length of crossing edges

    while (not unprocessed_node_set == []):

        lengthof_node_to_addto_pns = heapq.heappop(current_heap) # pop out the length of the node, which would be added to the processed node set

        for node_add in length_edge_pair_dict.keys():
            if length_edge_pair_dict[node_add] == lengthof_node_to_addto_pns:
                node_to_addto_pns = node_add  # find the node to add to the processed node set
                break
        # delete this edge
        del length_edge_pair_dict[node_add] # already popped and deleted from heap
        # node_to_addto_pns = length_edge_pair_dict[lengthof_node_to_addto_pns][1] # find the node to add to the processed node set
        processed_node_set.append(node_to_addto_pns) # add the node to the processed node set
        unprocessed_node_set.remove(node_to_addto_pns) # remove the node from the unprocessed node set
        shortest_path[node_to_addto_pns] = lengthof_node_to_addto_pns # update the shortest path

        # no need to update the crossing edges
        # edges ending in this node must be removed, since they are no longer crossing edges
        # delete_list = []
        # for edge in crossing_edges:
        #     if edge[1] == node_to_addto_pns:
        #         delete_list.append(edge)
        # for edge_del in delete_list:
        #     crossing_edges.remove(edge_del)



        # add new crossing edges, edges incident to this node in unprocessed node set now become crossing edges
        for node in graph[node_to_addto_pns].keys():
            # if node is already in old heap, firstly delete it, then insert it again after update
            if node in unprocessed_node_set:
                tmp_length_2 = graph[node_to_addto_pns][node] + shortest_path[node_to_addto_pns]
                if node in length_edge_pair_dict.keys():
                    current_heap.remove(length_edge_pair_dict[node])
                    if tmp_length_2 < length_edge_pair_dict[node]:
                        length_edge_pair_dict[node] = tmp_length_2
                        # crossing_edges.append((node_to_addto_pns, node))
                else:
                    length_edge_pair_dict[node] = tmp_length_2
                    # crossing_edges.append((node_to_addto_pns, node))

                # update heap and length_edge_pair_dict

                heapq.heappush(current_heap, length_edge_pair_dict[node])
                heapq.heapify(current_heap)


    return shortest_path

graph, num_of_node = creategraph("dijkstraData.txt")
# print graph
# cross_edges = findCrossEdge(graph, [0,1])
# print cross_edges
# current_heap, len_ed_p = buildHeap(graph, cross_edges, [0,3,0,0])
# print current_heap
# print len_ed_p
shortest_path = dijkstrashort(graph,num_of_node)
# print shortest_path
print shortest_path[6],shortest_path[36], shortest_path[58], shortest_path[81], shortest_path[98], shortest_path[114], shortest_path[132], shortest_path[164], shortest_path[187], shortest_path[196]
# 7,37,59,82,99,115,133,165,188,197