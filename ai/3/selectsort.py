def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        # Assume the current index is the minimum
        min_index = i

        # Check the rest of the array for a smaller element
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first element of the unsorted part
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


# Get input from the user
try:
    input_str = input("Enter numbers separated by spaces: ")
    # Convert input string to a list of integers
    arr = list(map(int, input_str.split()))

    print("Original array:", arr)
    sorted_arr = selection_sort(arr)
    print("Sorted array:", sorted_arr)

except ValueError:
    print("Please enter valid integers only.")