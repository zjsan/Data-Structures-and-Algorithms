from queue import PriorityQueue

#creating a dictionary for the graph

start = "Home"#initializing start
goal = "Home"#initializing end/goal
graph = {
    "Home": [("Church", 45), ("Market", 12), ("Office", 25)],
    "Church": [("Fields", 15), ("Home", 45), ("Market", 30)],
    "Market": [("Church", 30), ("Fields", 45), ("Home", 12), ("Office", 10), ("Pier", 12)],
    "Office": [("Home", 25), ("Market", 10), ("Pier", 20)],
    "Fields": [("Church", 15), ("Market", 45), ("Pier", 50)],
    "Pier": [("Fields", 50), ("Market", 12), ("Office", 20)]
}

frontier = PriorityQueue()#queue for the traversal
frontier.put([0, {start}, [start]])#appending the starting node

min_path = []#list for the optimal path
min_cost = -1

#traversing the graph
#while queue is not empty
while (not frontier.empty()):

    cur_n = frontier.get()#getting first element
    cost = cur_n[0]#getting cosst
    visited = cur_n[1].copy()#marking down the node
    path = cur_n[2].copy()#getting initial cost
    node = path[-1]#use to get the recently added node
    neighbors = graph[node]#will use for the traversal
    
    if len(path) == len(graph):
        neighbors = {n[0]: n[1] for n in neighbors}#getting neighbours of the node
        #checking if start is in neighbours
        #adding initial cost of the current node to the cost of the start node
        #as by the UCS rule
        if start in neighbors.keys():
            path.append(start)
            cost += neighbors[start]#cost counter
            min_path = path
            min_cost = cost
            break

    #appending neighbour nodes in the search queue    
    else:
        neighbors = graph[node]

        #getting neighbors and their cost
        for neighbor, n_cost in neighbors:
            #checking if the node is not yet visited
            #if not put them on the search queue together with their cost
            #as well as adding the possible optimal path
            if neighbor not in visited:
                new_v = visited.copy()
                new_v.add(neighbor)
                new_p = path.copy()
                new_p.append(neighbor)
                new_cost = cost
                new_cost += n_cost
                frontier.put([new_cost, new_v, new_p])

#printing optimal path
print("The optimal path that the salesman can go through is --> ",min_path)
print("Total cost for the salesman to pay for this path: ",min_cost)
