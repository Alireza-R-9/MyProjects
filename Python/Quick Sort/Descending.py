def quick_sort(arr):

    if len(arr) <= 1:
        return arr
    else:

        pivot = arr[0]

        left = [x for x in arr[1:] if x >= pivot]
        right = [x for x in arr[1:] if x < pivot]

        return quick_sort(left) + [pivot] + quick_sort(right)


input_data = input()
numbers = list(map(int, input_data.split()))

sorted_numbers = quick_sort(numbers)

print(' '.join(map(str, sorted_numbers)))
