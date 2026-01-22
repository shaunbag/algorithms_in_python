# the depth first search algorithm
# demonstrated here on a file direct
from os import listdir
from os.path import isfile, join

# define the function that takes a directory as a parameter


def print_names(directory):
    # loop through the files in the directory
    for file in sorted(listdir(directory)):
        # obtain the full path of the file
        fullpath = join(directory, file)
        # check if the fullpath is a file
        if isfile(fullpath):
            # print the file if its a file
            print(file)
        else:
            # call the print_names function recursively if the fullpath isn't a file
            print_names(fullpath)
