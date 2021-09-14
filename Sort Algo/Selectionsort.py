import random, time

def SelectionSort(arr):
    for i in range(1, len(arr)):
        min_idx = i

        for j in range(i + 1, len(arr)):
                if arr[min_idx] > arr[j]:
                    min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

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

SelectionSort(arr)

executionTime = (time.time() - startTime)


print ("Sorted array is:")
for i in range(len(arr)):
    print ("%d" %arr[i]),

print("Execution Time:", executionTime)