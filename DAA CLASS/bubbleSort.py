def bubbleSort(a,n):
    for k in (1,n-1):
        for i in (1,n-k):
            if a[i]>a[i+1]:
                tem = a[i]
                a[i] = a[i+1]
                a[i+1] = tem
    return

arr = [100,544,3333,6554,766,89,865]
bubbleSort(arr,len(arr)-1)
print(arr)