def Euclids(m,n):
    while n % m != 0:
        r = n % m
        n = m
        m = r
    return m
m = 988
n = 1764
# swapping
if n < m:
    tem = m
    n = m 
    m = n
print(Euclids(m,n))
    
