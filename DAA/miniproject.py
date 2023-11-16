import threading

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

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

    # Use append, not extend, to add single elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result

def multi_threaded_merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left_thread = threading.Thread(target=multi_threaded_merge_sort, args=(left,))
    right_thread = threading.Thread(target=multi_threaded_merge_sort, args=(right,))

    left_thread.start()
    right_thread.start()

    left_thread.join()
    right_thread.join()

    return merge(left, right)

if __name__ == "__main__":
    unsorted_list = [12, 11, 13, 5, 6, 7]
    sorted_list = multi_threaded_merge_sort(unsorted_list)
    sorted_list_1 = merge_sort(unsorted_list)
    print("Sorted array (Multithreaded):", sorted_list)
    print("Sorted array (Normal):", sorted_list_1)