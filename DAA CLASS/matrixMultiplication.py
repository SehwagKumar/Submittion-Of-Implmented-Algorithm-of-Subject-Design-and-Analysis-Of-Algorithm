def matrixMultiplication(a,b,c):
   for i in range(len(a)):
      for j in range(len(a[0])):
         for k in range(len(a)):
            c[i][j] = c[i][j] + a[i][k] * b[k][j]

a = [[1,2],
     [3,4]]
b = [[1,2],
     [3,4]]

c = [[0,0],
     [0,0]]
matrixMultiplication(a,b,c)
print(c)







# Time Complexity IS O(n power 3)