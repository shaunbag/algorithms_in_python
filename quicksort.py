# the quicksort algorithm
# define the quicksort method
def quick_sort(arr):
    # check if the array passed in has a length of 1 or 0
    if len(arr) < 2:
        # if so return the array
        return arr
    # if not then perform the following
    else:
        # define the pivot value as the first item in the array
        pivot = arr[0]
        # make another array of all the values lower than the pivot
        less = [i for i in arr[1:] if i <= pivot]
        # make another array of all the values higher
        greater = [i for i in arr[1:] if i > pivot]
        # the return calls quicksort recursively on the lesser and greater arrays to sort them then all values are
        # combined lower values + the pivot value + greater values
        return quick_sort(less) + [pivot] + quick_sort(greater)
