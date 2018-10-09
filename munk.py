from munkres import Munkres, print_matrix
matrix = [[11,4,11,6,11],
          [7,5,6,7,12],
          [9,7,8,10,10],
          [9,11,6,10,9],
          [7,10,4,8,8]]
m = Munkres()
indexes = m.compute(matrix)
print_matrix(matrix, msg='Lowest cost through this matrix:')
total = 0
for row, column in indexes:
    value = matrix[row][column]
    total += value
    print('(%d, %d) -> %d' % (row, column, value))
print('total cost: %d' % total)