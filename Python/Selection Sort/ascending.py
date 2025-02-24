def selection_sort_ascending(arr):
    # Traverse through all array elements
    for i in range(len(arr)):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


# Input parsing
input_data = input()  # گرفتن ورودی از کاربر
coins = list(map(int, input_data.split()))  # تبدیل ورودی به لیست اعداد

# Sorting the array in ascending order using Selection Sort
sorted_coins = selection_sort_ascending(coins)

# Print the result
print(' '.join(map(str, sorted_coins)))
