import merge
def mergeSort(lis):
    n = len(lis)
    if n < 2:
        return
    else:
        mid = int(n/2)
        left = [0] * mid
        right = [0] * (n-mid)
    for i in range(mid):
        left[i] = lis[i]
    for i in range(n - mid):
        right[i] = lis[mid + i]
    mergeSort(left)
    mergeSort(right)
    merge.merge(left,right,lis)


arr = [100,544,3333,6554,766,89,865]
mergeSort(arr)
print(arr)
