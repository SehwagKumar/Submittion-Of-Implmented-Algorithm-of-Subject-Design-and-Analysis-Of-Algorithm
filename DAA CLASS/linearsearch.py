def linear(a,find):
    for i in range(len(a)):
        if a[i] == find:
            return i

arr = [1,2,3,4,5,6,9]
print(linear(arr,6))
