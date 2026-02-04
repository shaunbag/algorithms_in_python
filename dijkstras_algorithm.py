# first setup the graphs
import math
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}

# Hash tables to store the current costs for each node
infinity = math.inf
costs = {"a": 6, "b": 2, "fin": infinity}

parents = {"a": "start", "b": "start", "fin": "none"}
processed = set()


# set out the function to find the lowest cost node
def find_the_lowest_cost_node(costs_to_process):
    # set lowest cost initially to infinity
    lowest_cost = math.inf
    # and lowest cost node to none
    lowest_cost_node = None
    # then loop through the passed in costs to process
    for node_to_process in costs_to_process:
        # grab the cost from the graph
        cost_to_process = costs_to_process[node_to_process]
        # check if the cost is less than the current lowest cost and hasn't already been processed
        if cost_to_process < lowest_cost and node_to_process not in processed:
            # now set the lowest cost to the cost we are processing
            lowest_cost = cost_to_process
            # and set the lowest cost node to the node we are processing
            lowest_cost_node = node_to_process
    # finally return the lowest cost node
    return lowest_cost_node


# the algorithm
def dijkstras_algorithm():
    # set node to the initial lowest cost node
    node = find_the_lowest_cost_node(costs)
    # loop while the node isn't None
    while node is not None:
        # set costs as the node in the costs hash table
        cost = costs[node]
        # and set neighbors as the node in the graph
        neighbors = graph[node]
        # now loop through the keys in neighbours
        for n in neighbors.keys():
            # set the new cost as the current cost plus the node in neighbours
            new_cost = cost + neighbors[n]
            # check if the node in costs is greater than the new cost
            if costs[n] > new_cost:
                # if it is then set it as new cost
                costs[n] = new_cost
                # and set the node in parents as the node
                parents[n] = node
        # add this node to processed
        processed.add(node)
        # call find the lowest node again and continue the loop
        print("Processed: " + str(processed))
        print("Costs: " + str(costs))
        print("Parents: " + str(parents))
        node = find_the_lowest_cost_node(costs)



