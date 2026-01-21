from binary_search import binary_search
from selection_sort import selection_sort
from quicksort import quick_sort
from hash_tables import check_voter
from breadth_first_search import breadth_first

my_list = [4, 2, 1, 65, 44, 100, 99, 75, 2]

numbers = [
    1, 2, 3, 4, 5, 6, 7, 8,
    9, 10, 11, 12, 13, 14, 15, 16,
    17, 18, 19, 20, 21, 22, 23, 24,
    25, 26, 27, 28, 29, 30, 31, 32,
    33, 34, 35, 36, 37, 38, 39, 40,
    41, 42, 43, 44, 45, 46, 47, 48,
    49, 50, 51, 52, 53, 54, 55, 56,
    57, 58, 59, 60, 61, 62, 63, 64,
    65, 66, 67, 68, 69, 70, 71, 72,
    73, 74, 75, 76, 77, 78, 79, 80,
    81, 82, 83, 84, 85, 86, 87, 88,
    89, 90, 91, 92, 93, 94, 95, 96,
    97, 98, 99, 100, 101, 102, 103, 104,
    105, 106, 107, 108, 109, 110, 111, 112,
    113, 114, 115, 116, 117, 118, 119, 120,
    121, 122, 123, 124, 125, 126, 127, 128,
    129, 130, 131, 132, 133, 134, 135, 136,
    137, 138, 139, 140, 141, 142, 143, 144,
    145, 146, 147, 148, 149, 150, 151, 152,
    153, 154, 155, 156, 157, 158, 159, 160,
    161, 162, 163, 164, 165, 166, 167, 168,
    169, 170, 171, 172, 173, 174, 175, 176,
    177, 178, 179, 180, 181, 182, 183, 184,
    185, 186, 187, 188, 189, 190, 191, 192,
    193, 194, 195, 196, 197, 198, 199, 200,
    201, 202, 203, 204, 205, 206, 207, 208,
    209, 210, 211, 212, 213, 214, 215, 216,
    217, 218, 219, 220, 221, 222, 223, 224,
    225, 226, 227, 228, 229, 230, 231, 232,
    233, 234, 235, 236, 237, 238, 239, 240,
    241, 242, 243, 244, 245, 246, 247, 248,
    249, 250, 251, 252, 253, 254, 255, 256,
]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("This is the Binary Search Algorithm using the array: " + str(numbers) + ", and the Item: " + str(1))
    answer = binary_search(numbers, 1)
    print(answer)

    print("This is the Selection Sort Algorithm using the array: " + str(my_list))
    answer = selection_sort(my_list)
    print(answer)

    print("This is the Quick Sort Algorithm using the array: " + str(my_list))
    answer = quick_sort(my_list)
    print(answer)

    # create the name variable on user input
    print("This is the hash tables data structure example")
    name = input("Enter a Voter Name")
    # simple loop to allow the user to enter multiple names adding to the hash table
    while name != "end":
        # run the check voter method from hash_tables
        check_voter(name)
        # allow user to try another name or the same to check the check_voter function, enter end as a name to finish
        name = input("Enter a Voter Name, enter end to finish this ")

    print("This is an example of the Breadth-first Search algorithm, finding the name ending with m from a graph")
    answer = breadth_first()
    print(answer)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
