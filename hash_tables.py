# the hash tables data structure

# create the hash table
voted = {}


def check_voter(name):
    # the hash table contains the name and a boolean for if the name has registered to vote, check the name exists
    if name in voted:
        # if the name does exist then they have already voted
        print(name + " has already voted")
    else:
        # if not add the name and set the boolean to true
        voted[name] = True
        # inform the user that the new name has registered
        print(name + " has not yet voted but now has registered and voted")


