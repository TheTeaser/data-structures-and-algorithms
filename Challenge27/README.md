# Merge Sort:

In this article, we will explore the Merge Sort algorithm. 

The Merge Sort algorithm follows a divide-and-conquer approach, recursively dividing the input array into smaller subarrays, sorting them, and then merging them back together.

## The Code:
```
ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length

    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left
```

***The Mergesort function*** takes an array arr and recursively divides it into smaller subarrays until the base case of having subarrays of length 1 is reached. It then merges the sorted subarrays back together using the Merge function.

***The Merge function*** takes two sorted subarrays left and right, and merges them together into a single sorted array arr. It compares the elements from left and right and places them in the correct order in arr.

## Example:

 We will sort the following array: [8,4,23,42,16,15]

 Initial State:

    arr: [8, 4, 23, 42, 16, 15]

Iteration 1:  

Since the length of the array is greater than 1, we proceed with the MSA, We find the midpoint of the array, which is n/2 = 6/2 = 3. [N: Number of elements in the array.]

 We divide the array into two halves:
Left side:

    [8, 4, 23]
Right side:

     [42, 16, 15]


Iteration 2:

---
- Left Side

    Recursively apply Merge Sort on the left side.
    Split the left side into two halves:
    Left side of the left side: 
        
        [8]
    Right side of the left side: 
    
        [4, 23]
    Recursively apply Merge Sort on both subarrays.
    Merge the sorted subarrays:
    Sorted left side of the left side: 
    
        [8]
    Sorted right side of the left side:
        
         [4, 23]
    Merged result: 
    
        [4, 8, 23]
    
---
- Right Side

    Recursively apply Merge Sort on the right side.
    Split the right side into two halves:
    Left side of the right side:
         
         [42]

    Right side of the right side: 
    
        [16, 15]
    Recursively apply Merge Sort on both subarrays.
    Merge the sorted subarrays:
    Sorted left side of the right side: 
        
        [42]
    Sorted right side of the right side:
        
         [15, 16]
    Merged result:
    
         [15, 16, 42]
---

Step 3:

Merge the sorted left and right sides of the original array.
Merge [4, 8, 23] (sorted left side) and [15, 16, 42] (sorted right side).
Final sorted array:

     [4, 8, 15, 16, 23, 42]
---

## Big O:

**Time Complexity:**  O(N Log N), N for number of inputs; Log N for the division in the this algorithm nature.

**Space Complexity:**  O(N)

## Implementation: 

For the implementation, kindly check [Here!](merge_sort.py) 

## Testing:

For the testing, kindly check [Here!](./tests/test_merge_sort.py)