def fibonanci(n):
    if n < 2:
        return 1
    else:
        return fibonanci(n-1) + fibonanci(n-2)

print(fibonanci(6))

# Time Complexity O(2 power n)