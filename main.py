def anti_diagonals(matrix):
    n = len(matrix)
    result = []
    for i in range(n):
        diagonal = []
        row, col = i, 0
        while row >= 0 and col < n:
            diagonal.append(matrix[row][col])
            row -= 1
            col += 1
        result.append(diagonal)
    for j in range(1, n):
        diagonal = []
        row, col = n - 1, j
        while row >= 0 and col < n:
            diagonal.append(matrix[row][col])
            row -= 1
            col += 1
        result.append(diagonal)
    return result
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
output = anti_diagonals(A)
for diagonal in output:
    print(*diagonal)
