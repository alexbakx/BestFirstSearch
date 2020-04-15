#A simple implementation of Priority Queue using Queue. 
class PriorityQueue(object): 
    def __init__(self): 
        self.queue = []
        self.heuristic = []
        self.parent = []
  
    def __str__(self): 
        return ' '.join([str(i) for i in self.queue]) 
  
    #For checking if the queue is empty 
    def isEmpty(self): 
        return len(self.queue) == [] 

    #For checking the length of the queue
    def length(self): 
        return len(self.queue)

    #For checking if a point exists in the queue
    def exists(self, point):
        return point in self.queue
  
    #For inserting an element in the queue 
    def insert(self, data, heuristic_value, node_parent): 
        self.queue.append(data)
        self.heuristic.append(heuristic_value)
        self.parent.append(node_parent)
  
    #For getting an element with the lowest priority 
    def getMin(self): 
        try: 
            min = 0
            for i in range(len(self.heuristic)): 
                if self.heuristic[i] < self.heuristic[min]: 
                    min = i 
            item = self.queue[min]
            item_parent = self.parent[min]
            del self.heuristic[min]
            del self.queue[min]
            del self.parent[min]
            return item, item_parent
        except IndexError: 
            print() 
            exit()

    #For getting the element with the highest priorty
    def getMax(self): 
        try: 
            max = 0
            for i in range(len(self.heuristic)): 
                if self.heuristic[i] >= self.heuristic[max]: 
                    max = i 
            item = self.queue[max]
            item_parent = self.parent[max]
            del self.heuristic[max]
            del self.queue[max]
            del self.parent[max]
            return item, item_parent
        except IndexError: 
            print() 
            exit()        