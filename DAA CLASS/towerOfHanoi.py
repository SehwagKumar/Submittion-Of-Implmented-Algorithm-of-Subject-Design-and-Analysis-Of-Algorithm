def towerOfHanoi(n,beg,aux,end):
    if n==0:
        return
    towerOfHanoi(n-1,beg,end,aux)
    print("Move Disk",n,"from",beg,"to",end)
    towerOfHanoi(n-1,aux,beg,end)

n = 5
towerOfHanoi(n,'A','B','C')