cdef extern from "sorts/merge.h":
    void merge(int arr[], int left, int mid, int right)
    void c_mergeSort(int arr[], int left, int right)

def c_merge(arr, left, right):
    # convert python array to a cython array
    cdef int[:] arr_view = arr
    # passing a pointer as arr param
    return c_mergeSort(&arr_view[0], left, right)
