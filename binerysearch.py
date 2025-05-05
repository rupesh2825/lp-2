def binary_search(arr, key):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Fixed sorted array
arr = [2, 4, 6, 8, 10, 12, 14]

key = int(input("Enter element to search: "))
result = binary_search(arr, key)

if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found.")
