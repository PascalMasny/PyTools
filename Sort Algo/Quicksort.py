import random, time

def partition(arr, low, high):
    i = (low - 1)
    pivote = arr[high]

    for j in range(low, high):
        if arr[j] <= pivote:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
        
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)

def QuickSort(arr, low, high):
    if len(arr) == 1:
        return arr

    if low < high:
        pi = partition(arr, low, high)

        QuickSort(arr, low, pi - 1)
        QuickSort(arr, pi + 1, high)

def randomArr(arr_len):
    for i in range(arr_len):
        arr.append(random.randint(0,1000))
        i = i + 1

    return arr
        


arr_len = 1000
arr = []
n = arr_len

randomArr(arr_len)
print(arr)


startTime = time.time()

QuickSort(arr, 0, n - 1)

executionTime = (time.time() - startTime)


print ("Sorted array is:")
for i in range(len(arr)):
    print ("%d" %arr[i]),

print("Execution Time:", executionTime)