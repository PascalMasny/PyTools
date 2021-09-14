import random, time

def shakerSort(arr):
    n = len(arr)

    for i in range(n):

        for j in range(i, 0, -1):

            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]

        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    

            


def randomArr(arr_len):
    for i in range(arr_len):
        arr.append(random.randint(0,1000))
        i = i + 1

    return arr
        


arr_len = 10000
arr = []


randomArr(arr_len)
print(arr)


startTime = time.time()

shakerSort(arr)

executionTime = (time.time() - startTime)

 
print ("Sorted array is:")
for i in range(len(arr)):
    print ("%d" %arr[i]),

print("Execution Time:" executionTime)