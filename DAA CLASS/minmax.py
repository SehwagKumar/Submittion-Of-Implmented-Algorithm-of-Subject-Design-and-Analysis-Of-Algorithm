def MinMax(arr, i, j, min_val, max_val):
    if i == j:
        min_val[0] = arr[i]
        max_val[0] = arr[i]
    elif i == j-1:
        if arr[i] < arr[j]:
            min_val[0] = arr[i]
            max_val[0] = arr[j]
        else:
            min_val[0] = arr[j]
            max_val[0] = arr[i]
    else:
        mid = (i + j)//2
        min_left = [int()]
        max_left = [int()]
        MinMax(arr, i, mid, min_left, max_left)
        min_right = [int()]
        max_right = [int()]
        MinMax(arr, mid+1, j, min_right, max_right)
        if min_left[0] < min_right[0]:
            min_val[0] = min_left[0]
        else:
            min_val[0] = min_right[0]
        if max_left[0] > max_right[0]:
            max_val[0] = max_left[0]
        else:
            max_val[0] = max_right[0]

arr = [100,544,3333,6554,766,89,865]
min_val = [int()]
max_val = [int()]

MinMax(arr, 0, len(arr)-1, min_val, max_val)
print("Min:", min_val[0])
print("Max:", max_val[0])