# The Selection Sort algorithm

# create a find smallest element in an array function

def find_smallest(arr):
    # initialise smallest with the first item in the array
    smallest = arr[0]
    # initialise the smallest index with 0
    smallest_index = 0
    # loop through the array
    for i in range(1, len(arr)):
        # if the item in the current iteration is smaller than the smallest item, initially item 0
        if arr[i] < smallest:
            # make smallest the current index in the array
            smallest = arr[i]
            # and set the smallest index as this index ready for the next iteration
            smallest_index = i
    # finally return the smallest index
    return smallest_index

# now using this function make the selection sort


def selection_sort(arr):
    # initialise an empty array
    new_arr = []
    # make a copy of the array passed into the function so we can mutate it
    copied_arr = list(arr)
    # loop through the copied array
    for i in range(len(copied_arr)):
        # use the find_smallest function to find the smallest item in the array
        smallest = find_smallest(copied_arr)
        # add the smallest item to the new array
        new_arr.append(copied_arr.pop(smallest))
    # finally return the array
    return new_arr
