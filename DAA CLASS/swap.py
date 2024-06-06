# SwapTimeEfficient
a =10
b =20
print(f"Hello I Am Variable a {a}")
print(f"Hello I Am Variable b {b}")
temp = a
a = b
b = temp
print("***SWAP TIME EFF***")
print(f"Hello I Am Variable a {a}")
print(f"Hello I Am Variable b {b}")

# Swap Space Efficient
print("***SWAP SPACE EFF***")
a = a + b
b = a - b
a = a - b

print(f"Hello I Am Variable a {a}")
print(f"Hello I Am Variable b {b}")