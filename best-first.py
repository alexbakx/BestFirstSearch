import math
from PriorityQueue import PriorityQueue

#Opens a map from a given file name
def open_map():
    input_map = []
    filename = input('Enter a filename: ')
    f = open(filename, 'r')
    for x in f:
        input_map.append([x.rstrip()])
    return input_map

#Finds the start and end nodes for any given map
def find_coords(search_map, map_width, map_height):
    for i in range(map_width):
        for j in range(map_height):
            if search_map[j][0][i] == 'S':
                start = [i, j]
            if search_map[j][0][i] == 'G':
                end = [i, j]
    return start, end

#Calculates the height of a map
def get_height(search_map):
    return len(search_map)

#Calculates the width of a map
def get_width(search_map):
    return len(search_map[0][0])

#Calculates the heuristic value from one point to another using the euclidean distance
def calc_heuristic(pointA, pointB, initial_map, width, height, start, end, visited_queue):
    x1 = pointA[0]
    y1 = pointA[1]
    x2 = pointB[0]
    y2 = pointB[1]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


def find_neighbours(initial_map, parent, frontier, visited_queue, width, height, start, end):
    x = parent[0]
    y = parent[1]
    #For all surrounding nodes
    for i in range (x - 1, x + 2):
        for j in range (y - 1, y + 2):
            #Check if the neighbouring node is valid, i.e. can only go up, down, left, right
            #Can't be X, G, S, -, | and can't be outside of the map boundaries
            if i > 0 and j > 0 and i <= width and j <= height and [i, j] != [x, y] and [i, j] != [x - 1, y - 1] and [i, j] != [x + 1, y - 1] and [i, j] != [x + 1, y + 1] and [i, j] != [x - 1, y + 1] and initial_map[j][0][i] != 'X' and initial_map[j][0][i] != '-' and initial_map[j][0][i] != '|' and not frontier.exists([i, j]) and not visited_queue.exists([i, j]):
                frontier.insert([i, j], calc_heuristic([i, j], end, initial_map, width, height, start, end, visited_queue), parent)   

#While there are more nodes to explore
def best_first(frontier, initial_map, visited_queue, width, height, start, end):
    while not frontier.isEmpty():
        #Pop node off with the best heuristic value
        current = frontier.getMin()
        parent = current[1]
        current = current[0]
        #Set the current node as visited
        visited_queue.insert(current, 0, parent)
        #If the current node is the goal node
        if current == end:
            break
        else:
            #If not the goal node, find all it's neighbours and add them to the priority queue
            find_neighbours(initial_map, current, frontier, visited_queue, width, height, start, end)

#Print initial map
def print_map(initial_map):
    for i in range(height):
        for j in range(width):
            print(initial_map[i][0][j], '', end='')
        print()

def find_path(visited_queue, initial_map, width, height, start, end):
    path = []
    #Create array and variable to check whether it's the first node
    first = True
    #Remove first node, as this is the end node and not part of the path
    visited_queue.getMax()

    #Add nodes that are part of the path to array
    while visited_queue.length() > 0:
        #If first node, manually set it as the current node and the next node
        if first:
            current_node = visited_queue.getMax()
            next_node = visited_queue.getMax()
            first = False
        #If the current node's parent is the next node
        if current_node[1] == next_node[0]:
            #Add it to the path
            path.append(current_node[0])
            #Set current node to the next node, i.e. its child
            current_node = next_node
            #Set next node to the node after that node
            next_node = visited_queue.getMax()
        #If the current node's parent is not the next node, it is not part of the path and needs to be skipped
        else:
            next_node = visited_queue.getMax()
    
    #Outside of loop to get the last node
    if current_node[1] == next_node[0]:
        path.append(current_node[0])

    return path

def print_map(initial_map, path, width, height, start, end):
    #Print map with shortest path
    for i in range(height):
        for j in range(width):
            #If current point is part of the path, display it as a decimal
            if [j, i] in path and [j, i] != start and [j, i] != end:
                print('. ', end='')
            else:
                print(initial_map[i][0][j], '', end='')
        print() 

def main():
    initial_map = open_map()

    #Calculate width and height of map
    width = get_width(initial_map)
    height = get_height(initial_map)
    #Find start and end nodes
    start, end = find_coords(initial_map, width, height)
    frontier = PriorityQueue()
    #Add the start node to the priority queue, with a heuristic value of 0, and no parent
    frontier.insert(start, 0, None)
    visited_queue = PriorityQueue()

    #Execute the search algorithm
    best_first(frontier, initial_map, visited_queue, width, height, start, end)

    #Find the path
    path = find_path(visited_queue, initial_map, width, height, start, end)

    #Print the path on the map
    print_map(initial_map, path, width, height, start, end)

if __name__ == '__main__': main()