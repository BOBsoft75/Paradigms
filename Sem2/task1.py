init_matrix = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]]
d_sum = 0
size = len(init_matrix)
for diag in range(size):
    d_sum += init_matrix[diag][diag]
print(d_sum)
