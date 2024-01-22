def binarySearch(fila, x, low, high):
    while low <= high:
        mid = low + (high-low) // 2

        if fila.data[mid] == x:
            return True
        elif fila.data[mid] < x:
            low = mid + 1
        else:
            high = mid -1

    return False 

# def sortFila(fila):
#     if fila.len_fila() <= 1:
#         return fila
#     for i in range(fila.len_fila()):
#         
#     return [0, 1, 2, 3, 4]

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2

        left = arr[:mid]
        right = arr[mid:]

        mergeSort(left)
        mergeSort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1

            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
        

def isOrdered(arr):
    return True
