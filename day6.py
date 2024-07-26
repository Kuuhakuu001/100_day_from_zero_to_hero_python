A = [
    [0, 0, 0],
    [0, 4, 0],
    [0, 1, 0]
]

B = [
    [1, 1],
    [1, 1]
]

C = [
    [0, 1, 0],
    [0, 1, 0],
    [0, 1, 0]
]

def zero_pad(matrix, pad):
    padded_matrix = []
    row_length = len(matrix[0]) + 2 * pad
    for _ in range(pad):
        padded_matrix.append([0] * row_length)
    
    for row in matrix:
        padded_matrix.append([0] * pad + row + [0] * pad)
    
    for _ in range(pad):
        padded_matrix.append([0] * row_length)
    
    return padded_matrix

def convolve2d(matrix, kernel):
    kernel_height = len(kernel)
    kernel_width = len(kernel[0])
    matrix_height = len(matrix)
    matrix_width = len(matrix[0])
    
    output_height = matrix_height - kernel_height + 1
    output_width = matrix_width - kernel_width + 1
    
    output = [[0] * output_width for _ in range(output_height)]
    
    for i in range(output_height):
        for j in range(output_width):
            sum = 0
            for m in range(kernel_height):
                for n in range(kernel_width):
                    sum += matrix[i + m][j + n] * kernel[m][n]
            output[i][j] = sum
            
    return output

padded_A = zero_pad(A, 1)
output_1 = convolve2d(padded_A, B)
output_2 = convolve2d(padded_A, C)

print(output_1)
print(output_2)
