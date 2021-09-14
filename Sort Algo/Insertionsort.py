import random, time

def insertionSort(arr):
    for i in range(1, len(arr)):
        n = arr[i]
        j = i - 1

        while j >= 0 and n < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = n

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

insertionSort(arr)

executionTime = (time.time() - startTime)


print ("Sorted array is:")
for i in range(len(arr)):
    print ("%d" %arr[i]),

print("Execution Time:", executionTime)