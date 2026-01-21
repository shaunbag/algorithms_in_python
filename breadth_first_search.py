from collections import deque

# the breadth-first search algorithm, an algorithm used to answer two questions
# 1. is there a path from node A to node B
# 2. What is the shortest path from node A to node B
# first we need to create our graph (we'll use a hash table)
graph = {
    "you": ["alice", "bob", "claire"],
    "bob": ["anuj", "peggy"],
    "alice": ["peggy"],
    "claire": ["thom", "jonny"],
    "anuj": [],
    "peggy": [],
    "thom": [],
    "jonny": []
}


# create a method that checks if the persons name ends with an "m"
def persons_name_ends_with_m(name):
    return name[-1] == 'm'


# now create the algorithm, a while loop that continues while the search_queue isn't empty
def breadth_first():
    # next we will create a queue adding "you" items the "First Degree" connections
    search_queue = deque()
    search_queue += graph["you"]
    # create a set of people already checked to avoid loops if they are duplicated in the grapg
    searched = set()
    while search_queue:
        # remove the first person from the queue and store in variable
        person = search_queue.popleft()
        # check the person hasn't already been checked
        if person not in searched:
            # check if the persons name ends with an N
            if persons_name_ends_with_m(person):
                # print out the person found
                print(person + "'s name ends with an m")
                return True
            else:
                # otherwise we need to add any friends of that person to the queue, "second degree" connections
                search_queue += graph[person]
                searched.add(person)
    return False
