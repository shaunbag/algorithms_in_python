# the binary algorithm

# define the function taking the array to be searched and the item we are searching for
def binary_search(arr, item):
    # the lowest index
    low = 0
    # the highest index
    high = len(arr) - 1
    # create the while loop
    tries = 0
    while low <= high:
        tries = tries + 1
        # create the mid value
        mid = (low + high) // 2
        # create the guess mid (index) in the arr
        guess = arr[mid]
        # check the guess is it equal to the item
        if guess == item:
            return "The index is " + str(mid) + ", this took " + str(tries) + " tries"
        # is the guess greater than the item, if it is take 1 from the mid
        elif guess > item:
            high = mid - 1
        else:
            # otherwise add one to the mid
            low = mid + 1
    return None

