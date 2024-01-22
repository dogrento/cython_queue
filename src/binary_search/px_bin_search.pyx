cpdef void mergeSort(list[int] arr):
    cdef int mid
    cdef list[int] left
    cdef list[int] right
    cdef int i, j, k
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
        

cpdef isOrdered(list[int] arr):
    cdef int i = 0
    for i in range(len(arr) - 1): 
        if arr[i] > arr[i+1]:
            return False
    return True
