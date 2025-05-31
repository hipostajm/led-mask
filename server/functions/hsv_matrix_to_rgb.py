from functions.hsv_to_rgb import hsv_to_rgb

def hsv_matrix_to_rgb(matrix):
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            matrix[y][x] = hsv_to_rgb(matrix[y][x])

    return matrix