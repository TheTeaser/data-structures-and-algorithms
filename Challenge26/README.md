# Insertion Sort:

In this article, we will explore the Insertion Sort algorithm, a simple and efficient sorting algorithm that builds a sorted array one element at a time. 

## The Code:

```
Insert(int[] sorted, int value)
  initialize i to 0
  WHILE value > sorted[i]
    set i to i + 1
  WHILE i < sorted.length
    set temp to sorted[i]
    set sorted[i] to value
    set value to temp
    set i to i + 1
  append value to sorted

InsertionSort(int[] input)
  LET sorted = New Empty Array
  sorted[0] = input[0]
  FOR i from 1 up to input.length
    Insert(sorted, input[i])
  return sorted

```

The Insert function takes a sorted array and a value as input, then it finds the correct position to insert the value into the sorted array and shifts the elements accordingly. 


## Example:

 We will sort the following array: [8,4,23,42,16,15]

Initial State:

```
sorted: []
input: [8, 4, 23, 42, 16, 15]
```

Iteration 1:  

We start with an empty sorted array and append the first element from the input array, which is (8).
```
sorted: [8]
input: [4, 23, 42, 16, 15]
```
Iteration 2:

First we compare the second element of the input array (4) with the elements in the sorted array.
Since (4) is less than (8), we shift (8) to the right and insert (4) at the beginning of the sorted array.
```
sorted: [4, 8]
input: [23, 42, 16, 15]
```

Iteration 3:

We compare the third element of the input array (23) with the elements in the sorted array;

Since (23) is greater than (8) and (4), we insert (23)  8 in the right of (8) in the sorted array.
```
sorted: [4, 8, 23]
input: [42, 16, 15]
```
Iteration 4:

Same as in the previous iteration, (42) is bigger than all the elements in the sorted array, thus we append it on the right of (23)

```
sorted: [4, 8, 23, 42]
input: [16, 15]
```
Iteration 5:

We iterate through each element starting from the first element of the sorted array and compare the input element (16), with the sorted array,since (16) is bigger than both (4) and (8) but smaller than (23); therefore, we will set (16) on the place of (23) and append the rest (i+1) on their spot.
```
sorted: [4, 8, 16, 23, 42]
input: [15]
```
Iteration 6:

Same as the previous iteration.
```
sorted: [4, 8, 15, 16, 23, 42]
input: []
```
Sorting Complete:

Sorted array: [4, 8, 15, 16, 23, 42]

## Big O:

Time Complexity:  O(n^2)

Space Complexity:  O(1)

## Implementation: 

For the implementation, kindly check [Here!](insertion_sort.py) 

## Testing:

For the testing, kindly check [Here!](./tests/test_insertionSort.py) 