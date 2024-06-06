def partition(a,start,end):
    pivot = a[end]
    index = start -1
    for i in range(start,end):
        if a[i] < pivot:
            index = index + 1
            temp = a[i]
            a[i] = a[index]
            a[index] = temp
    temp2 = a[end]
    a[end] = a[index +1]
    a[index +1] =  temp2
    return index +1
def quickSort(a,start,end):
    if start<end:
        q = partition(a,start,end)
        quickSort(a,start,q-1)
        quickSort(a,q+1,end)

arr = [100,544,3333,6554,766,89,865]
quickSort(arr,0,len(arr)-1)
print(arr)