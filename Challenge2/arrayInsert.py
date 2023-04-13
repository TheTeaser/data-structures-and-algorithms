# Did not use Snakecase in function name as the question stated to name the function like this.

# def insertShiftArray(Arr, Val):
#     middle= len(Arr)//2     # it gave an error when I used a single / as we need an integer location, thus you need // to give a floor answer.
#     Arr.insert(middle, Val) #insert(poistion, value) can be used in lists and arrays.
#     print(Arr)

# Redone the code to not include the insert function and not to use any library.
def insertShiftArray(Arr, value):
    middle = (len(Arr)+1) // 2
    new_arr = [0] * (len(Arr)+1)
    for i in range(middle):
        new_arr[i] = Arr[i]
    new_arr[middle] = value
    for i in range(middle+1, len(Arr)+1):
        new_arr[i] = Arr[i-1]
    print(new_arr)



insertShiftArray([2,4,6,8],5)
insertShiftArray([42,8,15,23,42],16)


# Stretch goal solved.

def removeMiddle(Arr):
    middle= len(Arr)//2
    Arr.pop(middle)
    print(Arr)

removeMiddle([1,2,3,4,5])
removeMiddle([1,2,3,4])