import random

def partition(arr, low, high):
    pivot = arr[low]
    left = low + 1
    right = high

    done = False
    while not done:
        while left <= right and arr[left] <= pivot:
            left = left + 1
        while arr[right] >= pivot and right >= left:
            right = right - 1
        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]

    arr[low], arr[right] = arr[right], arr[low]

    return right

def quick_sort(arr, low, high, randomized=False):
    if low < high:
        if randomized:
            random_index = random.randint(low, high)
            arr[low], arr[random_index] = arr[random_index], arr[low]
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1, randomized)
        quick_sort(arr, pivot_index + 1, high, randomized)

# Function to choose and perform sorting based on user input
def sort_array(arr, randomized=False):
    copy_arr = arr.copy()
    quick_sort(copy_arr, 0, len(copy_arr) - 1, randomized)
    return copy_arr

# Example usage:
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

choice = int(input("Enter 0 for deterministic Quick Sort, 1 for randomized Quick Sort: "))
randomized = choice == 1

sorted_arr = sort_array(arr, randomized)
print("Sorted Array:", sorted_arr)
