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

We start by passing the first element:
```
Sorted array: []
Value to insert: 8
```
Then the second one untill the whole input is done:
```
Sorted array: [8]
Value to insert: 4
```

-|


\ /

```
Sorted array: [4, 8, 16, 23, 42]
Value to insert: 15
```

For the implementation, kindly check [Here!](insertion_sort.py) 