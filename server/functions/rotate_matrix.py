def rotate_matrix(matrix, mode: int) -> list:
    
    width = len(matrix[0])
    height = len(matrix)
    
    match mode:
        case 1:
    
            new_matrix = [[[]]*height for _ in range(width)]
            
            for y in range(height):
                for x in range(width):
                    new_matrix[x][height-y-1] = matrix[y][x]
            
            return new_matrix

        case 2:
            
            new_matrix = [[[]]*width for _ in range(height)]
            
            for y in range(height):
                for x in range(width):
                    new_matrix[height-y-1][width-x-1] = matrix[y][x]
                    
            return new_matrix

        case 3:
            
            new_matrix = [[[]]*height for _ in range(width)]
            
            for y in range(height):
                for x in range(width):
                    new_matrix[width-x-1][y] = matrix[y][x]
                    
            return new_matrix