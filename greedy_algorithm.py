# Using the radio station analogy we will try to find the best stations to cover all the states


# define the function we can call in our main.py
def greedy_algorithm():
    # first we set up the set for the needed states to cover
    states_needed = {"mt", "wa", "or", "id", "nv", "ut", "ca", "az"}

    # next we set up the stations and their coverage
    stations = {"kone": {"id", "nv", "ut"}, "ktwo": {"wa", "id", "mt"}, "kthree": {"or", "nv", "ca"},
                "kfour": {"nv", "ut"},
                "kfive": {"ca", "az"}}

    # finally a set for the final_stations chosen
    final_stations = set()
    # now lets set up a loop to loop through the states_needed while the dictionary has items
    while states_needed:
        # create a reference for the best station
        best_station = None
        # create a set of the states covered
        states_covered = set()
        # loop through the stations and states
        for station, states in stations.items():
            # make a set intersection of states needed and states
            covered = states_needed & states
            # check if the length of covered is greater than states_covered
            if len(covered) > len(states_covered):
                # if so make best_station station
                best_station = station
                # and set states_covered to covered
                states_covered = covered
        # remove states_covered from states_needed
        states_needed -= states_covered
        # add best station to final_stations
        final_stations.add(best_station)

    print(final_stations)