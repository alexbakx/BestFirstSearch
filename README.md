# Best First Search
This projects implements a best first search to get from a starting point to an end point on a map. The implementation was done using Python. The starting point on the map is displayed by an **_S_**, while the end point is shown as a **_G_**. On the map, the **_X_** shows a wall that the algorithm can't go through. The five example maps provided demonstrate the algorithm at work, however any map in the same kind of format can be used by this algorithm. The algorithm implements a priority queue to store the nodes that it has yet to visit. 

## Methods
### open_Map
This method asks for a file name from the user to open a map, which it then adds to an array to store the map in. 

### find_coords
Finds the start and end nodes for any given map, by looking for the **_S_** and **_G_** in the array. 

### get_height
Simply returns the height of the map.

### get_width
Simply returns the width of the map.

### calc_heuristic
Calculates the heuristic value from one point to another using the euclidean distance. 

### find_neighbours
Takes the initial map, parent node, frontier, visited nodes, width, height, start and end of a map and finds all the surrounding nodes of that node. The initial map is simply the array holding the map. The parent is the node of which we want to find the neighbours. The frontier is all the nodes we have yet to explore, this is a priority queue. The visited queue holds all nodes that have already been visited. This method then checks if the neighbouring node is valid, if it's valid the node gets added to the frontier. Whether a neighbouring node is valid depends on several factors, such as if it's within bounds of the map, whether there is an **_X_** there etc.

### best_first
This method uses the best first algorithm to find a route between the start point and the end point. It checks whether there are more nodes to explore by seeing if the frontier is empty or not, then it pops of the node with the best heuristic value. The node then gets set as visited, and if the node is the goal node it exits out of the method. If not, the **_find_neighbours_** method gets called to find all neighbours of the node. 

### find_path
This method adds all nodes that are part of the path from the start point to the end point to an array, in order to display them on the map later. It does this by going backwards through the queue of visited nodes.

### print_map
This method takes the path from start point to end point, and displays it on top of the initial map to display the route that the algorihtm found. 

### main
Opens a new map, then executes the search algorithm to find the path and display in on the map.
