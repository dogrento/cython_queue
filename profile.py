
from src.simple_queue import Fila, fill_fila
from px_bin_search import mergeSort as pxMergeSort
from cy_binary_search import mergeSort as cyMergeSort
from src.binary_search.binary_search import mergeSort
from wrapper import c_merge

def pure_py(fila1):
    # fila = fill_test(1000) 
    mergeSort()

def compiled_py(fila2):
    # fila = fill_test(1000) 
    cyMergeSort()

def px_py(fila3):
    # fila = fill_test(1000) 
    pxMergeSort()

def merge_c(fila4):
    # fila = fill_test(1000)
    c_merge()

def just_fill():
    fila = fill_test(1000)

def fill_test(n):
    arr = []
    while len(arr) < n:
        random_value = random.randint(0, n)

        if random_value not in arr:
            arr.append(random_value)

    return arr

def main():
    fila1 = fill_test(1000) 
    fila2 = fill_test(1000) 
    fila3 = fill_test(1000) 
    fila4 = fill_test(1000) 

    pure_py()
    compiled_py()
    px_py()
    merge_c()


if __name__ == "__main__":
    main()
