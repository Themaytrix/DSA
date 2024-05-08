# represent graph in a hash table. each node should have a key of next neighbor and value of weight

graph = {}

graph['start'] = {'a':6, 'b':2}
graph['b'] = {'a':3, 'fin':5}
graph['a'] = {'fin':1}
graph['fin'] = {}

# need a hashtable to keep track of costs from destination
infinity = float('inf')
costs = {}
costs['a'] = 6
costs['b'] = 1
costs['fin'] = infinity

# need a hashtable to keep track of parents of nodes
parents ={}
parents['a'] = "start"
parents['b'] = 'start'
parents['fin'] = None

# an array to keep track of visited nodes or the shortest route
processed = []

def lowest_cost_node(costs):
    # initialize the lowest cost as infinity
    lowest_cost = infinity
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


node = lowest_cost_node(costs)
# while there is node to process
while node is not None:
    # cost of lowest node
    cost = costs[node]
    # we want to get the neighbors of the lowest cost node
    neighbors = graph[node]
    # for every node neighboring we want to compare the shortest path and update the cost
    for n in neighbors.keys():
        # we want to add the cost of traversal to the next node to see the smallest
        new_cost = cost + neighbors[n]
        # compare it to the original cost and update that cost if new_cost is smaller
        if costs[n] > new_cost:
            costs[n] = new_cost
            # update current node to be parent of preceding neighbors
            parents[n] = node
    processed.append(node)
    node = lowest_cost_node(costs)
        
print(processed)