# Big-O Notation

___THIS IS ALL TIME COMPLEXITY___

Measurement of time and space complexity of a data structure, algorithm, program, etc.

Gives an ___upper bound___ in the worst case

## Complexities

$n$ = The size of the input

| Time              | Big-O           |
| :---------------- | --------------: |
| Constant          | $O(1)$          |
| Logarithmic       | $O(log(n))$     |
| Linear            | $O(n)$          |
| Linearithmic      | $O(nlog(n))$    |
| Quadratic         | $O(n^2)$        |
| Cubic             | $O(n^3)$        |
| Exponential       | $O(b^n)$, $b>1$ |
| Factorial         | $O(n!)$         |

* These are just the main ones, any mathematical notation can be considered for $n$

Remember we only really care about the worst case scenario and what happens when $n$ -> $\infty$

* So given an algorithm function that describes the running time: $f(n) = 7log(n)^3 + 15n^2 + 2n^3 + 8$
* We reduce $O(f(n)) = O(n^3)$ as this term will be the largest contributor as $n$ -> $\infty$
  * This is all theoretical, if you have a huge constant in the real world, it will matter

## Examples

### Constant time

Algorithms that ___do not depend on $n$ at all___

```python
i = 1 # assigning is in constant time
while i < 11:
    print(i)
    i += 1
```

### Linear Time

Respects the input size $n$, do constant amount of work $n$ times.

```python
i = 1
while i < n:
    print(i)
    i += 3 # makes f(n) 1/3, cut time in third
```

* $f(n) = n/3$
* $O(f(n)) = O(n)$

### Quadratic Time

$n$ work done $n$ times = $O(n^2)$

```python
for i in range(n):
    for j in range(n):
        print(i, ":", j)
```

* $f(n) = n * n = n^2$
* $O(f(n)) = O(n^2)$

This example is not as obvious:

```python
for i in range(n):
    j = i
    for j in range(n):
        print(i, ":", j)
```

* $f(n) = \frac{n(n+1)}{2}$
* $O(f(n)) = O(\frac{n^2}{2} + \frac{n}{2}) = O(n^2)$

### Logarithmic Time (Binary Search)

[Binary Search](/algorithms/binarySearch/BinarySearch.md) finds the index of a particular value in a sorted array

```python
low, high = 0, n-1
while low <= high:
    mid = (low+high) // 2

    if arr[mid] == target:
        return mid
    else if arr[mid] > target: high = mid-1
    else if arr[mid] < target: low = mid + 1

return -1 # no value found
```

* $f(n) = log_2(n)$
* $O(f(n)) = O(log(n))$

### Quadratic example

This example is more to show how we translate from what the code is doing into a function of $n$, and then simplify down into a $O(n)$.

```python
i = 0
while i < n:
    j = 0
    while j < (3 * n):
        j += 1
    while j < (2 * n):
        j += 1
    i += 1
```

* $f(n) = n * (3n + 2n) = 5n^2$
* $O(f(n)) = O(n^2)$

### Complex Example

This example serves as a more complex one to show the connection between code -> $f(n)$ -> $O(f(n))$

```python
i = 0
while i < (3 * n):
    j = 10
    while j <= 50:
        j += 1
    j = 0
    while j < (n * n * n):
        j += 2
    i += 1
```

* $f(n) = 3n * (40 + \frac{n^3}{2}) = 3n*40 + \frac{3n^4}{2}$
* $O(f(n)) = O(n^4)$

Remember we are respecting $n$ in this case, so the second loop would always execute 40 times no matter what $n$ is. The third loop halves its iterations because the value has 2 added every time. Then we can simplify $f(n)$ by distribution to make it easier to work with.

## Classic Examples

These examples are memorable

### Finding all subsets of a set

$O(2^n)$

Because there are $2^n$ subsets...math

### Finding all permutations fo a string

$O(n!)$

### Sorting using mergesort

$O(nlog(n))$

### Iterating over all cells in a matrix of size $n$ by $m$

$O(nm)$

## General Rules

* Multiply loops that are on different levels
* Add loops that are on the same level
* Consider ___exactly___ how much work is to be done
