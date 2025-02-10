def binsearch(arr, target):
    l_ptr, r_ptr = 0, len(arr) - 1

    while l_ptr < r_ptr:
        mid = (l_ptr+r_ptr) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l_ptr = mid + 1
        elif arr[mid] > target:
            r_ptr = mid - 1

    return -1


if __name__ == "__main__":
    a = [4, 5, 1, 4, 7, 2, 9]
    a.sort()

    assert binsearch(a, 7) == 5

    assert binsearch(a, 15) == -1

    # O(nlogn) because of sort
