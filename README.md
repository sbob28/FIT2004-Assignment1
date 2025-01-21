# Dynamic Programming and Graph-Based Problem Solving

## Overview

This project consists of two main tasks that demonstrate advanced techniques in dynamic programming and graph-based algorithms. Both tasks involve solving real-world-inspired problems with optimized solutions.

---

## Task 1: Max Cuteness Score Calculation for Fitmons

### Description
The `fuse` function calculates the maximum combined cuteness score achievable by fusing Fitmons. It uses dynamic programming to find the optimal combination of fusions, considering affinities between adjacent Fitmons.

### Input
A list of lists (`fitmons`), where each inner list represents a Fitmon and contains:
- **Affinity Left** (`float`): Affinity with the Fitmon to its left (range: 0.1-0.9; 0 for the leftmost Fitmon).
- **Affinity Right** (`float`): Affinity with the Fitmon to its right (range: 0.1-0.9; 0 for the rightmost Fitmon).
- **Cuteness Score** (`int`): Inherent cuteness score (>0).

### Output
The maximum cuteness score achievable by fusing all Fitmons.

### Complexity
- **Time Complexity:** O(n³)
- **Space Complexity:** O(n²)

### Example Usage
```python
print(fuse([[0, 29, 0.9], [0.9, 91, 0.8], [0.8, 48, 0]]))
```

---

## Task 2: Escape Route Optimization with TreeMap

### Description
The `TreeMap` class models a forest of trees connected by roads and enriched with teleportation options via Solulu trees. The `escape` method finds the least-cost path from a starting tree to any exit, considering road weights and teleportation options.

### Input
1. **Roads**: A list of tuples `(u, v, w)` representing directed roads:
   - `u` (int): Starting tree ID.
   - `v` (int): Ending tree ID.
   - `w` (int): Weight (cost) of the road.
2. **Solulus**: A list of tuples `(x, y, z)` representing Solulu trees:
   - `x` (int): Tree ID with a Solulu tree.
   - `y` (int): Time required to destroy the Solulu tree.
   - `z` (int): Destination tree ID after teleportation.
3. **Start** (int): Starting tree ID.
4. **Exits** (list of int): Tree IDs that can serve as exits.

### Output
A tuple:
- **Minimum Cost**: Lowest cost to reach an exit.
- **Path**: List of tree IDs representing the sequence of trees visited.
- `None` if no path is found.

### Complexity
- **Time Complexity:** O((|R|+|T|) log |T|)
- **Space Complexity:** O(|R|+|T|)

### Example Usage
```python
roads = [(0,1,4), (1,2,2), (2,3,3), (3,4,1)]
solulus = [(5,10,0), (6,1,6)]
myforest = TreeMap(roads, solulus)
print(myforest.escape(1, [7, 2, 4]))
```

---

## Files
- **`task1.py`**: Contains the `fuse` function.
- **`task2.py`**: Contains the `TreeMap` class and `escape` method.

## How to Run
1. Clone the repository.
2. Execute `task1.py` and `task2.py` independently to see example outputs.
3. Modify the input data as needed to test different scenarios.
