import heapq
class TreeMap:
    def __init__(self, roads, solulus):
        #calculates the max no. of trees (nodes)
        tree_count = 0
        for road in roads:
            tree_count = max(tree_count, road[0]+1, road[1]+1)
        for solulu in solulus:
            tree_count = max(tree_count, solulu[0]+1, solulu[2]+1)
        #does this by seeing max indicies in roads and sols lists
        #this takes into account all the possible tree nodes in graph
        self.graph = [[] for _ in range(tree_count)] #list of lists for the graph. each list is a tree node
        for tree1, tree2, weight in roads:
            self.graph[tree1].append((tree2, weight)) #adds an edge from one tree to another with a weight

        self.solulus = [None] * tree_count #initially list storing the solulu tree is none
        for tree_index, destroy_time, teleport_destination in solulus: #each tuple in solulus is looped
            self.solulus[tree_index] = (destroy_time, teleport_destination) #stores the solulus at each tree index respectively

    def escape(self, start, exits): #method to escape a route is defined
        #from a start to any of the exit

        # Priority queue for modified Dijkstra's algorithm
        priority_q = []
        # Format: (current_cost, current_node, path, solulu_used)
        heapq.heappush(priority_q, (0, start, [start], False))

        # Keep track of visited states
        visited = {(start, False): 0}

        while priority_q:
            current_cost, current_node, path, solulu_used = heapq.heappop(priority_q)

            # If reached an exit and Solulu tree has been destroyed
            if current_node in exits and solulu_used:
                return (current_cost, path)

            # Explore neighbors
            for neighbor, travel_cost in self.graph[current_node]:
                next_cost = current_cost + travel_cost
                next_state = (neighbor, solulu_used)

                # Normal movement without Solulu tree interaction
                if next_state not in visited or visited[next_state] > next_cost:
                    visited[next_state] = next_cost
                    heapq.heappush(priority_q, (next_cost, neighbor, path + [neighbor], solulu_used))

                # Check if current node is a Solulu tree
                if self.solulus[current_node] and not solulu_used:
                    destroy_time, teleport = self.solulus[current_node]
                    next_cost = current_cost + destroy_time
                    if teleport != current_node:
                        next_state = (teleport, True)
                        extended_path = path + [teleport]
                    else:
                        next_state = (current_node, True)
                        extended_path = path
                    if next_state not in visited or visited[next_state] > next_cost:
                        visited[next_state] = next_cost
                        heapq.heappush(priority_q, (next_cost, teleport, extended_path, True))

        return None  # No route found


roads = [(0, 1, 4), (1, 2, 2), (2, 3, 3), (3, 4, 1), (1, 5, 2),
        (5, 6, 5), (6, 3, 2), (6, 4, 3), (1, 7, 4), (7, 8, 2),
        (8, 7, 2), (7, 3, 2), (8, 0, 11), (4, 3, 1), (4, 8, 10)]

solulus = [(5, 10, 0), (6, 1, 6), (7, 5, 7), (0, 5, 2), (8, 4, 8)]

myforest = TreeMap(roads, solulus)

print("Example 1.1:", myforest.escape(1, [7, 2, 4]))  
print("Example 1.2:", myforest.escape(7, [8]))        
print("Example 1.3:", myforest.escape(1, [3, 4]))     
print("Example 1.4:", myforest.escape(1, [0, 4]))     
print("Example 1.5:", myforest.escape(3, [4]))        
print("Example 1.6:", myforest.escape(8, [2]))        

