# Algorithms

A Python implementation of fundamental computer science algorithms including search and sorting algorithms.

## 📋 Overview

This project contains clean, well-commented implementations of essential algorithms commonly used in computer science and software development. Each algorithm is implemented in its own module with clear documentation and examples.

## 🚀 Features

- **Binary Search**: Efficient search algorithm for sorted arrays
- **Selection Sort**: Simple sorting algorithm with O(n²) time complexity
- **Quick Sort**: Fast divide-and-conquer sorting algorithm with O(n log n) average time complexity

## 📁 Project Structure

```
Algorithms/
├── binary_search.py      # Binary search implementation
├── selection_sort.py     # Selection sort implementation
├── quicksort.py          # Quick sort implementation
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

## 🏃 Running the Project

Run the main demonstration file:

```bash
python main.py
```

This will execute all three algorithms with example data and display the results.

## 📝 Example Output

```
This is the Binary Search Algorithm using the array: [1, 2, 3, ...], and the Item: 1
The index is 0, this took 1 tries

This is the Selection Sort Algorithm using the array: [4, 2, 1, 65, 44, 100, 99, 75, 2]
[1, 2, 2, 4, 44, 65, 75, 99, 100]

This is the Quick Sort Algorithm using the array: [4, 2, 1, 65, 44, 100, 99, 75, 2]
[1, 2, 2, 4, 44, 65, 75, 99, 100]
```

## 🎯 Use Cases

- **Binary Search**: Ideal for searching in large sorted datasets (databases, search engines)
- **Selection Sort**: Educational purposes, small datasets where simplicity is preferred
- **Quick Sort**: General-purpose sorting for medium to large datasets, widely used in practice

## 📚 Learning Resources

These implementations are designed to be educational and easy to understand, with inline comments explaining each step of the algorithm.
