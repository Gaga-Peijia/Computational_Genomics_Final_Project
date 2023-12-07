import threading
import time
import random

from concurrent.futures import ProcessPoolExecutor
def merge_sort(arr,layer=0):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Use ProcessPoolExecutor with a maximum of 16 processes
    if layer <=4:
        with ProcessPoolExecutor(max_workers=16) as executor:
            left_sorted, right_sorted = executor.map(merge_sort, [left_half, right_half],[layer+1,layer+1])
    else:
        left_sorted, right_sorted = map(merge_sort, [left_half, right_half],[layer+1,layer+1])

    return merge(left_sorted, right_sorted)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result
def merge_sort_single(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively sort both halves
        merge_sort_single(left_half)
        merge_sort_single(right_half)

        # Merge the sorted halves
        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def benchmark_sorting(sort_function, arr):
    arr_copy = arr.copy()
    start_time = time.time()
    sort_function(arr_copy)
    end_time = time.time()
    return end_time - start_time
if __name__=="__main__":
    # Generating a random list for benchmarking
    # random_list = [random.randint(0, 1000000) for _ in range(1000000)]
    #random dna(ACGT) with length 30
    # random_list = [[random.choice('ACGT') for _ in range(30)]]
    random_list=[]
    for i in range(10000000):
        random_str = [random.choice('ACGT') for _ in range(30)]
        random_str = "".join(random_str)
        random_list.append(random_str)
    # print(random_list)


    # # Benchmarking the multi-threaded merge sort
    time_taken = benchmark_sorting(merge_sort, random_list)
    print(f"Multi-threaded merge sort took {time_taken} seconds.")
    #single thread
    time_taken = benchmark_sorting(sorted, random_list)
    print(f"Single-threaded merge sort took {time_taken} seconds.")

