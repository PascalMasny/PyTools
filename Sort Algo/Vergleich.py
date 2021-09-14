import itertools, threading, time, sys, random

#Random Array Generator
def randomArr(arr_len):
    for i in range(arr_len):
        arr.append(random.randint(0,1000))
        i = i + 1

    return arr

#Bubblesort
def bubbleSort(arr):
    n = len(arr)

    for i in range(n):

        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j+1], arr[j]    

#Shakersort
def shakerSort(arr):
    n = len(arr)

    for i in range(n):

        for j in range(i, 0, -1):

            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]

        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

#Quicksort
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

#Insertionsort
def insertionSort(arr):
    for i in range(1, len(arr)):
        n = arr[i]
        j = i - 1

        while j >= 0 and n < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = n

#Selectionsort
def SelectionSort(arr):
    for i in range(1, len(arr)):
        min_idx = i

        for j in range(i + 1, len(arr)):
                if arr[min_idx] > arr[j]:
                    min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Loading Animation
done = False
def animate():
    for c in itertools.cycle(["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\nDone ✔️     ' + '\n')

# Array length => Dificulty
arr_len = 10000
arr = []
n = arr_len # for Insertionsort
sys.setrecursionlimit(arr_len - 1)


# Generate Arry
randomArr(arr_len)
print("\rBuild Arrray: Done ✔️")

#Sorting
t = threading.Thread(target=animate) #Start Loading Animation
t.start()

#Bubblesort
startTime = time.time()
bubbleSort(arr)
executionTime_Bubblesort = (time.time() - startTime)
print("\rBubblesort: Done ✔️")

#Shakersort
startTime = time.time()
shakerSort(arr)
executionTime_Shakersort = (time.time() - startTime)
print("\rShakersort: Done ✔️")

randomArr(arr_len)
CONSTANT = 0
sys.setrecursionlimit(max(sys.getrecursionlimit(), len(arr)+CONSTANT))

#QuickSort
startTime = time.time()
n = arr_len
QuickSort(arr, 0, n - 1)
executionTime_Quicksort = (time.time() - startTime)
print("\rQuicksort: Done ✔️")

randomArr(arr_len)

#Insertionsort
startTime = time.time()
insertionSort(arr)
executionTime_Insertionsort = (time.time() - startTime)
print("\rInsertionsort: Done ✔️")

randomArr(arr_len)



#Selectuionsort
startTime = time.time()
SelectionSort(arr)
executionTime_Selectionsort = (time.time() - startTime)
print("\rSelectionsort: Done ✔️")



time.sleep(1)
done = True

print("\n")
print("\rExecution Bubblesort Time:", executionTime_Bubblesort)
print("\rExecution Shakersort Time:", executionTime_Shakersort)
print("\rExecution Quicksort Time:", executionTime_Quicksort)
print("\rExecution Insertionsort Time:", executionTime_Insertionsort)
print("\rExecution Selectionsort Time:", executionTime_Selectionsort)
