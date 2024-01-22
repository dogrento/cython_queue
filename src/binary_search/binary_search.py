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


