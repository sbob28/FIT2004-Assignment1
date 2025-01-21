import heapq

class TreeMap:
    def __init__(self, roads, solulus):
        """
        function description: TreeMap is initialised with a graph structure that records roads and solulus.
        This function constructs the graph as an adjacency li`st where each node represents a tree,
        and edges respresent the roads connecting each tree with their respective weights. 

        input:
        'roads': a list of tuples where each tuple (u, v, w) represents a directed road.
        - u is an integer. it is the started tree ID
        - v is an integer. it is the ending tree ID
        - w is an integer. it is the weight of the road.

        'solulus': a list of tuples where each tuple (x, y, z) represents a solulu tree.
        - x is an integer. it is the tree DI where the solulu tree is located 
        - y is an integer. it is the time required to destroy the solulu tree.
        - z is an integer. it is the tree ID to which you will be teleported to after destroying the solulu tree. 


        output: there is no return value so nothing but TreeMap is initialised with a 
        constructed graph of solulu events and roads. this setup prepares the instance for the next operations 
        in the next method.

        time complexity: time complexity is O(|R|) when each road is processed once after iterating thought the list of roads. 
        then the complexity is O(|S|) when it iterates over the solulu trees. where n is the total number of entries in 'roads' and 'solulus' together. 
        so the complexity is O(|R|+|S|), |R| is the number of roads and |S| is the number of solulu trees, 
        to find the number of trees from the max tree IDs in both roads and solulus. since |S| is less than |T| (max no. of trees), 
        it fits the time complexity required.

        space complexity: space complexity is O(|R|+|T|) where |T| is the max number of tree and 
        |R| is the number of roads. this is because space is allocated for the graph which is a list of adjacency lists.
        these lists are sized according to |T| because the solulus list has atmost |T| entries. this matches the requirement of space complexity in the 
        assignment brief.
        """

        #calculates the max no of trees, so ndodes.
        trees = 0
        for road in roads:
            trees = max(trees, road[0]+1, road[1]+1)
        for solulu in solulus:
            trees = max(trees, solulu[0]+1, solulu[2]+1)
        #seeing max indicies in roads and the sols lists
        #this takes into account all the possible tree in the graph
        #list of lists for the graph. each list is a tree node
        self.graph = [[] for _ in range(trees)]
        for u, v, w in roads:
            self.graph[u].append((v, w)) #addes an edge from one tree to another with corresponding weight

        self.solulus = [None]*trees #list (stores the solulu tree) is empty at the start 
        for x, y, z in solulus: #looped
            self.solulus[x] = (y, z)#stores the solulus at each tree index respecitvely

    def escape(self, start,exits):#to escape a route from strat to any exit
        """
        function description: this function's purpose is to calculate the least cost path for escaping
        from a tree to any of the exits. this is achieved by considering roads and the possibility of using a solulu. 
        it also uses a priority queue to always extend the least costly path available at the moment.

        input:
        'start': an integer that tells us the starting tree. so the tree ID where the escape begins. 
        'exits': a list of integers (tree IDs) that tell us whether the trees can be used as exits

        output/return/postconditions: the method returns a tuple containing:
        - minimum cost: which is the lowest cost to reach an exit from the starting tree.
        it considers both direct routes and use of solulus for teleportation.
        -path: which is a list of node indices that represent the sequence of trees visited from the 
        starting tree to the exit. this includes any teleportations using solulus. 
        -if no path to any exit is found then it return exit. 

        it also returns none if no viable path to any exit is found. 
        the method calculates the best route from the starting point to an exit based on the current graph.

        time complexity: the worst time complexity is O((|R|+|T|) log |T|). |R| is the number of edges in the graph and
        |T| is the number of trees int he graph. so the total number of vertices in the graph.
        We get this complexity because the code operates on each edge and each tree so that gives O(log|T|) complexity per operation that is done.
        So if the node is processed twice (once with and without solulu), this is the worst case scenario. 
        under the assumption that the number of edges is the key factor influencing the performance of the code, the complexity aligns with the one that 
        is required in the assignment brief.

        space complexity: O(|R|+|T|) where |T| is the number of trees and |R| is the number of edges (roads). the space complexity includes the space for the 
        priority queue, which can hold up to the max number of trees, and the 'visited' array that tracks the minimum cost to reach each tree in 2 scenarios 
        (once with and without solulu).
        """
    
        priority_q=[]
        heapq.heappush(priority_q, (0, start, [start], False))#adds the first state to the queue (no solulu used to start)
        #list to tack the min cost for each tree 
        #with and without a sol
        visited = [[float('inf'), float('inf')] for _ in range (len(self.graph))]

        #this finds and adds the tree with the lowest cost (current cost)
        #does this by checking index to see if sol is used or no
        while priority_q:
            cost_now, current_node, path, solulu_used = heapq.heappop(priority_q)
            solulu_index = 1 if solulu_used else 0
            if current_node in exits and solulu_used:#checks if current node or no is an exit and if sol has been used
                return (cost_now, path)#once exit is reached it returns the cost and path
            
            #for near by trees connext to the current tree
            for neighbour, travel_cost in self.graph[current_node]:
                next_cost = cost_now +travel_cost
                if visited[neighbour][solulu_index] > next_cost:#trying to visit the nighbour. it checks if the cost was cheaper before than now
                    visited[neighbour][solulu_index] = next_cost#updated the vistsed cost and also the state to the queue
                    heapq.heappush(priority_q, (next_cost, neighbour, path +[neighbour], solulu_used))
                #what if a solulu tree ahsnt been used yet? destroyyy
                if self.solulus[current_node] and not solulu_used:
                    destroy_time, teleport = self.solulus[current_node]
                    next_cost = cost_now + destroy_time#calculation for the cost too detsroy the tree and teleport
                    teleport_index =1#once teleported then it gets noted that that the destination wasvisited with a sol
                    if visited[teleport][teleport_index] > next_cost:
                        visited[teleport][teleport_index] = next_cost#updates the visited list for the destination (teleported) and push new state
                        more_path = path +[teleport] if teleport != current_node else path
                        heapq.heappush(priority_q, (next_cost, teleport, more_path, True))

        return None#in case no path is found or exit wasnt reach then none
    
roads = [(0,1,4), (1,2,2), (2,3,3), (3,4,1), (1,5,2),
(5,6,5), (6,3,2), (6,4,3), (1,7,4), (7,8,2),
(8,7,2), (7,3,2), (8,0,11), (4,3,1), (4,8,10)]

solulus = [(5,10,0), (6,1,6), (7,5,7), (0,5,2), (8,4,8)]  

myforest = TreeMap(roads, solulus)

print("example 1.1:", myforest.escape(1, [7, 2, 4]))
print("example 1.2:", myforest.escape(7, [8]))
print("example 1.3:", myforest.escape(1, [3, 4]))
print("example 1.4:", myforest.escape(1, [0, 4]))
print("example 1.5:", myforest.escape(3, [4]))
print("example 1.6:", myforest.escape(8, [2]))