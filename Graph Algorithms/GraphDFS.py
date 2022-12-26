#testing stack implementation
def stack():
    
    stack = ['A','B','C','D','E']

    print("Initial list",stack)

    while stack:
        for x in stack:
            y = stack.pop()
            print("Elements pop from the stack --> ",y)
    print("After popping elements --> ",stack)

    
#dfs traversal
def maze(graph,start,end):
    
    search_stack = []#creating an empty stack for the traversal
    search_stack.append(start)
    visited = []#list for visited rooms
    

    #continue traversing all rooms
    #until the stack is empty
    while search_stack:

        currentRoom = search_stack.pop()#popping recently added element --> LIFO RULE
        goalRoom = currentRoom[-1]#will use to search a path from current room to goalroom
        nextRooms = graph[goalRoom]

        #traversing all rooms
        #adding possible paths
        for nextRoom in nextRooms:
            if nextRoom not in visited:
                path = list(currentRoom)#creating a list of possbile path and appending rooms that leads to goal room
                path.append(nextRoom)
                search_stack.append(path)#appending path in the stack
                visited.append(nextRoom)#marking down visited rooms

                #checking if currentRoom is the goalRoom
                #if goal room is found break loop
                if nextRoom == end:
                    print("The optimal path for the maze is --> ", *path, end = " ")
#creating the graph using dictionary
graph = {
        'A' : ['B','J'],
        'B' : ['C'],
        'C' : ['D'],
        'D' : [],
        'E' : ['F', 'G'],
        'F' : [],
        'G' : [],
        'H' : [],
        'I' : ['H'],
        'J' : ['I', 'P'],
        'K' : ['E', 'L'],
        'L' : ['M'],
        'M' : [],
        'N' : [],
        'O' : ['P'],
        'P' : ['K', 'O']
}
maze(graph,'A','G')



