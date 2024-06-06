def merge(left,right,a):
    nL = len(left)
    nR = len(right)
    i = 0
    j = 0
    k = 0
    while(i < nL and j < nR):
        if left[i] < right[j]:
            a[k] = left[i]
            i = i+1
        else:
            a[k] = right[j]
            j = j+1
        k = k+1
    while i < nL:
            a[k] = left[i]
            i = i+1
            k = k+1
    while j < nR:
            a[k] = right[j]
            j = j+1
            k = k+1
