# def merge(left,right,a):
#     nL = len(left)
#     nR = len(right)
#     i = 0
#     j = 0
#     k = 0
#     while(i < nL and j < nR):
#         if left[i] < right[j]:
#             a[k] = left[i]
#             i = i+1
#             k = k+1
#         else:
#             a[k] = right[j]
#             j = j+1
#             k = k+1
#     while i < nL:
#             a[k] = left[i]
#             i = i+1
#             k = k+1
#     while j < nR:
#             a[k] = right[j]
#             j = j+1
#             k = k+1
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