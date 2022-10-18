def main(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    div_factor : float
    for j in range(cols):
        current_factor = matrix[0][j] / matrix[1][j]


if __name__ == "__main__":
    matrix = [
                [2,  4, -2, 4], 
                [9, -8,  4, 5]
                                ]
    main(matrix)