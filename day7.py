# Given matrix
A = [
    [0, 0, 0, 4],
    [0, 4, 0, 2],
    [0, 1, 0, 2],
    [0, 3, 0, 2]
]

def max_pooling(mat, kernel_size, stride):
    pooled_matrix = []
    for i in range(0, len(mat) - kernel_size + 1, stride):
        row = []
        for j in range(0, len(mat[0]) - kernel_size + 1, stride):
            max_val = max([mat[i+m][j+n] for m in range(kernel_size) for n in range(kernel_size)])
            row.append(max_val)
        pooled_matrix.append(row)
    return pooled_matrix

def average_pooling(mat, kernel_size, stride):
    pooled_matrix = []
    for i in range(0, len(mat) - kernel_size + 1, stride):
        row = []
        for j in range(0, len(mat[0]) - kernel_size + 1, stride):
            avg_val = sum([mat[i+m][j+n] for m in range(kernel_size) for n in range(kernel_size)]) / (kernel_size * kernel_size)
            row.append(avg_val)
        pooled_matrix.append(row)
    return pooled_matrix

# Parameters
kernel_size = 2
stride = 2

# Max pooling
max_pooled = max_pooling(A, kernel_size, stride)
print("Max Pooling Output:")
print(max_pooled)

# Average pooling
average_pooled = average_pooling(A, kernel_size, stride)
print("Average Pooling Output:")
print(average_pooled)