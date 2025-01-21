import heapq

class TreeMap:
    def __init__(self, roads, solulus):
        # Calculate the maximum number of trees (nodes)
        tree_count = 0
        for road in roads:
            tree_count = max(tree_count, road[0]+1, road[1]+1)
        for solulu in solulus:
            tree_count = max(tree_count, solulu[0]+1, solulu[2]+1)

        self.graph = [[] for _ in range(tree_count)]
        for tree1, tree2, weight in roads:
            self.graph[tree1].append((tree2, weight))

        self.solulus = [None] * tree_count
        for tree_index, destroy_time, teleport_destination in solulus:
            self.solulus[tree_index] = (destroy_time, teleport_destination)

    def escape(self, start, exits):
        pq = []
        heapq.heappush(pq, (0, start, [start], False))

        # Initialize visited list to store (node, solulu_used) with their min cost
        visited = [[float('inf'), float('inf')] for _ in range(len(self.graph))]

        while pq:
            current_cost, current_node, path, solulu_used = heapq.heappop(pq)
            solulu_idx = 1 if solulu_used else 0

            if current_node in exits and solulu_used:
                return (current_cost, path)

            # Explore neighbors
            for neighbor, travel_cost in self.graph[current_node]:
                next_cost = current_cost + travel_cost

                # Normal movement without Solulu tree interaction
                if visited[neighbor][solulu_idx] > next_cost:
                    visited[neighbor][solulu_idx] = next_cost
                    heapq.heappush(pq, (next_cost, neighbor, path + [neighbor], solulu_used))

                # Check if current node is a Solulu tree
                if self.solulus[current_node] and not solulu_used:
                    destroy_time, teleport = self.solulus[current_node]
                    next_cost = current_cost + destroy_time
                    teleport_idx = 1
                    if visited[teleport][teleport_idx] > next_cost:
                        visited[teleport][teleport_idx] = next_cost
                        extended_path = path + [teleport] if teleport != current_node else path
                        heapq.heappush(pq, (next_cost, teleport, extended_path, True))

        return None  # No route found


# Usage example
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
