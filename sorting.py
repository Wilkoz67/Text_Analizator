def bubble_sort(data, key_index, reverse=False):
    arr = data[:]
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if reverse:
                if arr[j][key_index] < arr[j+1][key_index]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
            else:
                if arr[j][key_index] > arr[j+1][key_index]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
