def insertionSort(a):
    for i in range(len(a)):
        key = a[i]
        j=i-1
        while j >= 0 and key < a[j]:
            a[j+1] = a[j]
            j = j-1

        a[j+1] = key

arr = [100,544,3333,6554,766,89,865]
insertionSort(arr)
print(arr)