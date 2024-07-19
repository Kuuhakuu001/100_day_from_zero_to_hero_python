# Define the matrices and kernels
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

kernel_B = [
    [2, 4],
    [1, 3]
]

kernel_C = [
    [1, 1, 1],
    [0, 0, 0],
    [1, 1, 1]
]

def convolution(matrix, kernel):
    kernel_height = len(kernel)
    kernel_width = len(kernel[0])
    matrix_height = len(matrix)
    matrix_width = len(matrix[0])
    
    output_height = matrix_height - kernel_height + 1
    output_width = matrix_width - kernel_width + 1
    
    output = []
    for i in range(output_height):
        row = []
        for j in range(output_width):
            conv_sum = 0
            for m in range(kernel_height):
                for n in range(kernel_width):
                    conv_sum += matrix[i+m][j+n] * kernel[m][n]
            row.append(conv_sum)
        output.append(row)
    return output

# Perform convolution for kernel B and C
result_B = convolution(A, kernel_B)
result_C = convolution(A, kernel_C)

print("Câu 1:", result_B)
print("Câu 2:", result_C)