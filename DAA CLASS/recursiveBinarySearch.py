def recursiveBinarySearch(a,start,end,item):
    if start > end:
        return
    else:
        mid = int ((start+end)/2)
        if item == a[mid]:
            return mid
        elif item < a[mid]:
            return recursiveBinarySearch(a,start,mid-1,item)
        else:
            return recursiveBinarySearch(a,mid+1,end,item)
        


arr = [1,2,3,4,5,6,7]
print(recursiveBinarySearch(arr,0,len(arr)-1,7))
