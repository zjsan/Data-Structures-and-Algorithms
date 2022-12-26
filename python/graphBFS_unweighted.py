#creating the graph using dictionary
graph1 = {

    "A": [("B"),("F")],
    "B": [("C"),("E"),("F")],
    "C": [("D"),('E')],
    "D": [("G")],
    "E": [("D"),("G")],
    "F": [("E"),("H")],
    "H": [()],
    "G": [()],
}

#unweighted optimal path
def shortestPath(graph,start,end):

    search_queue = []#list to add nodes in the graph
    search_queue.append(start)#adding starting node in the queue
    visited = []#list for marked nodes during the traversal

    #while the queue is not empty
    #continue traversing 
    #until queue is empty
    while search_queue: 
        node = search_queue.pop(0)#getting first element in the queue
        lastNode = node[-1]#will use to search a path from a node to last node
        nextNodes = graph[lastNode]#appending lastnode for nextnode
        
        #traversing a path from current node to goal node
        #adding possible paths to the queue
        for nextNode in nextNodes:
            path = list(node)#list to contain possible paths
            path.append(nextNode)
            search_queue.append(path)#appending goal path in the queue
            #checking if node is goal
            #if goal has reached
            #get out of the loop
            if nextNode == end:
                print("The optimal path is --> ",*path, end = " ")#displaying the path
                return True
        #traversing all neighbor nodes if goal is not yet reached
        visited.append(node)#marking the node as visited
    return False 

shortestPath(graph1,"A","G")
