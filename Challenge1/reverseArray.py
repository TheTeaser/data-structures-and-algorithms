# Arr=[1,2,3,4,5,6]

# def reverse_array(Arr):
#     reversed_array=[]
#     for i in range(len(Arr)):
#         reversed_array= add_first_element(reversed_array, Arr[i-1])


# def add_first_element(Arr, element):
#     new_array=[element]+Arr
#     return new_array

# print(reverse_array(Arr))

def reverse_array(Arr):
    length=len(Arr)-1
    new_array=[]
    for items in Arr:
        new_array.append(Arr[length])
        length-=1
    print(new_array)


reverse_array([1, 2, 3, 4, 5, 6])
reverse_array([89, 2354, 3546, 23, 10, -923, 823, -12]	)
reverse_array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]	)
