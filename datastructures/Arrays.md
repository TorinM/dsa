# Dynamic and Static Arrays

The most used data structure

Forms a fundamental data bedrock for all other data structures

## Time Complexity

| Function  | Static Array | Dynamic Array |
| :-------- | :----------: | -----------:  |
| Access    | $O(1)$       | $O(1)$        |
| Search    | $O(n)$       | $O(n)$        |
| Insertion | N/A          | $O(n)$        |
| Appending | N/A          | $O(1)$        |
| Deletion  | N/A          | $O(n)$        |

* Note: Appending an element to the dynamic array is constant because the need to resize to a larger array is done so infrequently.
  * "Resizing" a dynamic array is analogous to creating a new static array of, most likely double, larger size and copying elements over to the new one.

## Static Array

___Fixed size___ container

__Indexable__ = Referenceable slots of memory by a number

Usages (pretty much everywhere):

1. Storing and accessing ___sequential___ data
2. Temporarily storing objects
3. Used by IO routines as __buffers__
    * Read small chunks of a data source (file) that is too large to fit in memory into the buffer one at a time.
4. Lookup tables and inverse lookup tables
5. Used to return multiple values from a function
    * "Hack" way to get around language specific limitations of only a single return value
6. Used in dynamic programming to cache answer to sub-problems
    * Shows in Knapsack or coin change DP problems

### Indexes

Basically each element adds 1 to the address of the 0 index.

## Dynamic Arrays

One way to implement is with a static array:

1. Create static array with initial capacity
2. Add elements and keep track of the number adding
3. If adding would exceed the size of the array, create a new static array double the size and copy all elements to that new array, then add the value

## Source Code Implementation

Implemented dynamic array in python [here](/datastructures/src/DynamicArray.py)
