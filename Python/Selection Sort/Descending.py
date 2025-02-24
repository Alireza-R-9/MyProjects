def selection_sort_descending(arr):
    # Traverse through all array elements
    for i in range(len(arr)):
        # Find the maximum element in remaining unsorted array
        max_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] > arr[max_idx]:
                max_idx = j

        # Swap the found maximum element with the first element
        arr[i], arr[max_idx] = arr[max_idx], arr[i]

    return arr


# Input parsing
input_data = input()  # گرفتن ورودی از کاربر
coins = list(map(int, input_data.split()))  # تبدیل ورودی به لیست اعداد

# Sorting the array in descending order using Selection Sort
sorted_coins = selection_sort_descending(coins)

# Print the result
print(' '.join(map(str, sorted_coins)))
