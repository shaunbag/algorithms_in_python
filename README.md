# Algorithms

A Python implementation of fundamental computer science algorithms including search, sorting, graph traversal, and data structures.

## 📋 Overview

This project contains clean, well-commented implementations of essential algorithms commonly used in computer science and software development. Each algorithm is implemented in its own module with clear documentation and examples.

## 🚀 Features

- **Binary Search**: Efficient search algorithm for sorted arrays
- **Selection Sort**: Simple sorting algorithm with O(n²) time complexity
- **Quick Sort**: Fast divide-and-conquer sorting algorithm with O(n log n) average time complexity
- **Hash Table Demo**: Minimal voter registry example showing constant-time lookups
- **Breadth-First Search (BFS)**: Graph traversal for reachability and shortest-path (unweighted) questions
- **Depth-First Search (DFS)**: Recursive tree/graph traversal demonstrated on directory structures
 - **Dijkstra's Algorithm**: Shortest-path algorithm for weighted graphs (non-negative weights)

## 📁 Project Structure

```
Algorithms/
├── binary_search.py      # Binary search implementation
├── breadth_first_search.py # Breadth-first search implementation
├── depth_first_search.py # Depth-first search implementation
├── selection_sort.py     # Selection sort implementation
├── quicksort.py          # Quick sort implementation
├── dijkstras_algorithm.py # Dijkstra's algorithm implementation
├── hash_tables.py        # Hash table (voter registry) example
└── main.py               # Example usage and demonstrations
```

## 🔧 Requirements

- Python 3.x

No external dependencies required - uses only Python standard library.

## 📖 Algorithms

### Binary Search

Searches for an item in a sorted array by repeatedly dividing the search interval in half.

**Time Complexity:**
- Best case: O(1)
- Average case: O(log n)
- Worst case: O(log n)

**Space Complexity:** O(1)

**Usage:**
```python
from binary_search import binary_search

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = binary_search(numbers, 5)
print(result)  # Returns the index and number of tries
```

### Selection Sort

Sorts an array by repeatedly finding the minimum element from the unsorted portion and placing it at the beginning.

**Time Complexity:**
- Best case: O(n²)
- Average case: O(n²)
- Worst case: O(n²)

**Space Complexity:** O(n)

**Usage:**
```python
from selection_sort import selection_sort

my_list = [4, 2, 1, 65, 44, 100, 99, 75, 2]
sorted_list = selection_sort(my_list)
print(sorted_list)  # Returns sorted array
```

### Quick Sort

Sorts an array using the divide-and-conquer approach by selecting a pivot and partitioning the array around it.

**Time Complexity:**
- Best case: O(n log n)
- Average case: O(n log n)
- Worst case: O(n²)

**Space Complexity:** O(log n) average, O(n) worst case

**Usage:**
```python
from quicksort import quick_sort

my_list = [4, 2, 1, 65, 44, 100, 99, 75, 2]
sorted_list = quick_sort(my_list)
print(sorted_list)  # Returns sorted array
```

### Hash Table (Voter Registry)

A minimal hash table example that tracks whether a name has already voted by storing names in a dictionary for O(1) average lookups and inserts.

**Time Complexity (average):**
- Insert: O(1)
- Lookup: O(1)

**Space Complexity:** O(n)

**Usage:**
```python
from hash_tables import check_voter

check_voter("alice")  # alice has not yet voted but now has registered and voted
check_voter("alice")  # alice has already voted
```

### Breadth-First Search (BFS)

Traverses a graph level-by-level using a queue. This implementation searches a small example graph for the first name ending with `"m"`.

**Time Complexity:** O(V + E)  
**Space Complexity:** O(V)

**Usage:**
```python
from breadth_first_search import breadth_first

found = breadth_first()  # Prints the matching name (if found) and returns True/False
print(found)
```

### Depth-First Search (DFS)

Recursively traverses a tree or graph by going as deep as possible before backtracking. This implementation demonstrates DFS by recursively traversing a directory structure and printing all file names.

**Time Complexity:** O(V + E)  
**Space Complexity:** O(V) (worst case for recursion stack)

**Usage:**
```python
from depth_first_search import print_names

print_names("/path/to/directory")  # Recursively prints all files in the directory tree
```

### Dijkstra's Algorithm

Dijkstra's algorithm finds the shortest path from a starting node to all other nodes in a weighted graph with non-negative edge weights. This repository includes a simple demonstration using dictionaries for the graph, cost table, and parent pointers.

**Time Complexity:** O(E + V log V) with a binary heap (priority queue) implementation; O(V^2) for a naive implementation

**Space Complexity:** O(V)

**Usage:**
```python
from dijkstras_algorithm import dijkstras_algorithm

dijkstras_algorithm()  # Runs the example graph and prints progress, costs, and parents
```


## 🏃 Running the Project

Run the main demonstration file:

```bash
python main.py
```

This will execute the algorithms with example data. The hash table demo is interactive and will prompt for voter names; type `end` to finish. The BFS demo runs automatically, and the DFS demo will prompt for a directory path.

## 📝 Example Output

```
This is the Binary Search Algorithm using the array: [1, 2, 3, ...], and the Item: 1
The index is 0, this took 1 tries

This is the Selection Sort Algorithm using the array: [4, 2, 1, 65, 44, 100, 99, 75, 2]
[1, 2, 2, 4, 44, 65, 75, 99, 100]

This is the Quick Sort Algorithm using the array: [4, 2, 1, 65, 44, 100, 99, 75, 2]
[1, 2, 2, 4, 44, 65, 75, 99, 100]

This is an example of the Breadth-first Search algorithm, finding the name ending with m from a graph
thom's name ends with an m
True

This is the depth-first algorithm, it will print the files in a given directory
Enter a directory path: /path/to/directory
file1.txt
file2.py
subdirectory_file.txt
...
```

## 🎯 Use Cases

- **Binary Search**: Ideal for searching in large sorted datasets (databases, search engines)
- **Selection Sort**: Educational purposes, small datasets where simplicity is preferred
- **Quick Sort**: General-purpose sorting for medium to large datasets, widely used in practice
- **Breadth-First Search**: Finding shortest paths in unweighted graphs, level-order tree traversal
- **Depth-First Search**: Tree/graph traversal, topological sorting, path finding, directory traversal

## 📚 Learning Resources

These implementations are designed to be educational and easy to understand, with inline comments explaining each step of the algorithm.
