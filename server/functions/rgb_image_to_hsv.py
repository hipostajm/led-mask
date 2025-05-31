from functions.rgb_to_hsv import rgb_to_hsv

def rgb_matrix_to_hsv(matrix) -> list[list[int,int,int]]:
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            matrix[y][x] = rgb_to_hsv(matrix[y][x])
    
    return matrix