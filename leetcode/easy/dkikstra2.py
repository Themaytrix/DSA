from heapq import heapify,heappop,heappush

graph = {
    "A": {"B": 3, "C": 3},
    "B": {"A": 3, "D": 3.5, "E": 2.8},
    "C": {"A": 3, "E": 2.8, "F": 3.5},
    "D": {"B": 3.5, "E": 3.1, "G": 10},
    "E": {"B": 2.8, "C": 2.8, "D": 3.1, "G": 7},
    "F": {"G": 2.5, "C": 3.5},
    "G": {"F": 2.5, "E": 7, "D": 10},
}

# helper function

def shortest_distance(source,graph):
    
    # build hashmap containing nodes and distances
    # set initial distances to infinity since we do not know the sources
    distance = {}
    for node in graph:
        distance[node] = float('inf')
    
    # set source distance to 0
    distance[source] = 0
    
    #   priority queue
    pq = [(0,source)]
    heapify(pq)
    
    visited = []
    
    # while we have element in our queue
    while pq:
        # get the priority element
        current_distance, current_node = heappop(pq)
        
        # check if the node has been visited.
        if current_node not in visited:
            visited.append(current_node)
            
        # go through node and neighbours
        
        for neighbor,weight in graph[current_node].items():
            new_distance = current_distance + weight
            
            if new_distance < distance[neighbor]:
                distance[neighbor] = new_distance
                heappush(pq,(new_distance,neighbor))
                print(distance)
                