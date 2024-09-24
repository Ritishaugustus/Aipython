from numpy import array
from numpy import tensordot as T

# A Array
A = array([
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[11, 12, 13], [14, 15, 16], [17, 18, 19]],
    [[21, 22, 23], [24, 25, 26], [27, 28, 29]]
])

print("A Matrix is \n", A)
print("Shape of A:", A.shape)

# B Array
B = array([
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[11, 12, 13], [14, 15, 16], [17, 18, 19]],
    [[21, 22, 23], [24, 25, 26], [27, 28, 29]]
])

print("B Matrix is \n", B)
print("Shape of B:", B.shape)

# Tensor addition
C = A + B
print("Tensor addition result C Matrix\n", C)

# Tensor Subtraction
S = A - B
print("Tensor Subtraction result S Matrix\n", S)

# Tensor Multiplication
M = A * B
print("Tensor Multiplication result M Matrix\n", M)

# Tensor division
DI = A / B
print("Tensor division result DI Matrix\n", DI)

print( "Tensordot example")
D = array([1, 2])
E = array([3, 4])

# When axes=0
F = T(D, E, axes=0)
print("Result when axes=0\n", F)

# When axes=1
F = T(D, E, axes=1)
print("Result when axes=1\n", F)