def selectionSort(a):
    for i in range(len(a)):
        least = a[i]
        p = i
        for j in range(i+1,len(a)):
            if a[j] < a[p]:
                least = a[j]
                p = j
        tem = a[i]
        a[i] = a[p]
        a[p] = tem
    return

arr = [100,544,3333,6554,766,89,865]
selectionSort(arr)
print(arr)