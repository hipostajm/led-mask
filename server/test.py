from functions.rotate_matrix import rotate_matrix
from functions.flip_matrix_horizontal import flip_matrix

a = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
    ]

print(*a, sep="\n")
print()
print(*rotate_matrix(a, 2), sep="\n")
print()
print(*flip_matrix(a, 2), sep="\n")