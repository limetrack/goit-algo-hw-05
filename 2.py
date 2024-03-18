def binary_search_with_upper_bound(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = left + (right - left) // 2

        if arr[mid] == target:
            upper_bound = arr[mid]
            break
        elif arr[mid] < target:
            left = mid + 1
            upper_bound = arr[mid] if mid + 1 < len(arr) and arr[mid + 1] >= target else upper_bound
        else:
            right = mid - 1
            upper_bound = arr[mid]

    if upper_bound is None and left < len(arr):
        upper_bound = arr[left]

    return iterations, upper_bound

# Test the function
arr = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6]
target = 3.5
result = binary_search_with_upper_bound(arr, target)
print(result)  # Should print the number of iterations and the upper bound
