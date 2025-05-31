def flip_matrix_vertical(matrix: list) -> list:
    
    width = len(matrix[0])
    height = len(matrix)
    
    new_matrix = [[[]]*width for _ in range(height)]
    
    for y in range(height):
        for x in range(width):
            new_matrix[y][width-x-1] = matrix[y][x]
                    
    return new_matrix